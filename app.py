from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

# PostgreSQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/aurelia_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# User Model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), default='')
    bio = db.Column(db.Text, default='')
    target_exam = db.Column(db.String(50), default='')
    notes = db.relationship('Note', backref='author', lazy=True, cascade='all, delete-orphan')
    stats = db.relationship('Stats', backref='user', uselist=False, cascade='all, delete-orphan')
    events = db.relationship('Event', backref='user', lazy=True, cascade='all, delete-orphan')
    daily_tasks = db.relationship('DailyTask', backref='user', lazy=True, cascade='all, delete-orphan')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'bio': self.bio,
            'target_exam': self.target_exam,
            'created_at': self.created_at.isoformat()
        }

# Note Model
class Note(db.Model):
    __tablename__ = 'notes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Stats Model
class Stats(db.Model):
    __tablename__ = 'stats'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sessions = db.Column(db.Integer, default=0)
    totalHours = db.Column(db.Float, default=0.0)
    streak = db.Column(db.Integer, default=1)
    
    def to_dict(self):
        return {
            'sessions': self.sessions,
            'totalHours': self.totalHours,
            'streak': self.streak
        }

# Event/Schedule Model
class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, default='')
    category = db.Column(db.String(50), default='study')  # study, exam, break, etc
    time = db.Column(db.String(5), default='09:00')  # HH:MM format
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'time': self.time,
            'created_at': self.created_at.isoformat()
        }

# Daily Task/Schedule Model
class DailyTask(db.Model):
    __tablename__ = 'daily_tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(5), nullable=False)  # HH:MM format
    task = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(100), default='')
    duration = db.Column(db.Integer, default=30)  # in minutes
    completed = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(20), default='medium')  # low, medium, high
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'time': self.time,
            'task': self.task,
            'subject': self.subject,
            'duration': self.duration,
            'completed': self.completed,
            'priority': self.priority,
            'created_at': self.created_at.isoformat()
        }

# Home route
@app.route('/')
def home():
    return "Aurelia Backend Running 🚀"

# Register User
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email", "")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(
        username=username,
        password=generate_password_hash(password),
        email=email
    )
    
    stats = Stats(user=user)
    db.session.add(user)
    db.session.add(stats)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Login User
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Save Notes API
@app.route('/save-notes/<username>', methods=['POST'])
def save_notes(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    note_content = data.get("notes", "")
    
    # Get or create note for user
    note = Note.query.filter_by(user_id=user.id).first()
    if note:
        note.content = note_content
    else:
        note = Note(user_id=user.id, content=note_content)
        db.session.add(note)
    
    db.session.commit()
    return jsonify({"message": "Notes saved successfully"})

# Get Notes API
@app.route('/get-notes/<username>', methods=['GET'])
def get_notes(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    note = Note.query.filter_by(user_id=user.id).first()
    notes_content = note.content if note else ""
    
    return jsonify({"notes": notes_content})

# Get User Profile
@app.route('/profile/<username>', methods=['GET'])
def get_profile(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    stats = Stats.query.filter_by(user_id=user.id).first()
    
    return jsonify({
        "username": user.username,
        "email": user.email,
        "name": user.name,
        "bio": user.bio,
        "target_exam": user.target_exam,
        "sessions": stats.sessions if stats else 0,
        "totalHours": stats.totalHours if stats else 0,
        "streak": stats.streak if stats else 1
    }), 200

# Update User Profile
@app.route('/profile/<username>', methods=['PUT'])
def update_profile(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    user.name = data.get("name", user.name)
    user.bio = data.get("bio", user.bio)
    user.target_exam = data.get("target_exam", user.target_exam)
    user.email = data.get("email", user.email)
    
    db.session.commit()
    
    return jsonify({"message": "Profile updated successfully", "profile": {
        "username": user.username,
        "email": user.email,
        "name": user.name,
        "bio": user.bio,
        "target_exam": user.target_exam
    }}), 200

# Generate Study Plan API
@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    data = request.json
    exam = data.get("exam")
    days = data.get("days")
    hours = data.get("hours")

    schedule = {
        'JEE': 'Physics (2h), Chemistry (2h), Maths (3h)',
        'NEET': 'Biology (3h), Physics (2h), Chemistry (2h)',
        'UPSC': 'History (3h), Polity (2h), Current Affairs (2h)',
        'GATE': 'Maths (2h), Core Subject (3h), Aptitude (1h)',
        'AL': 'Mathematics (2h), Physics (2h), Chemistry (2h), Core Subject (1h)'
    }

    base = schedule.get(exam.split()[0], "Core Subjects (4h), Practice (2h)")
    
    plan = f"""
📅 {days}-Day Plan for {exam}
Daily Study: {hours} hrs

- {base}

Tip: 10 min break after 50 min study.
"""

    return jsonify({"plan": plan})

# Update Stats
@app.route('/update-stats/<username>', methods=['POST'])
def update_stats(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    stats = Stats.query.filter_by(user_id=user.id).first()
    if stats:
        stats.sessions += 1
        stats.totalHours += 0.5
        db.session.commit()
    
    return jsonify(stats.to_dict()) if stats else jsonify({"error": "Stats not found"}), 200

# Create Event
@app.route('/create-event/<username>', methods=['POST'])
def create_event(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    event = Event(
        user_id=user.id,
        date=data.get("date"),
        title=data.get("title"),
        description=data.get("description", ""),
        category=data.get("category", "study"),
        time=data.get("time", "09:00")
    )
    
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Event created", "event": event.to_dict()}), 201

# Get Events by Date
@app.route('/get-events/<username>/<date>', methods=['GET'])
def get_events(username, date):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    from datetime import datetime as dt
    event_date = dt.strptime(date, '%Y-%m-%d').date()
    events = Event.query.filter_by(user_id=user.id, date=event_date).all()
    
    return jsonify({"events": [event.to_dict() for event in events]}), 200

# Get All Events for Month
@app.route('/get-all-events/<username>/<year>/<month>', methods=['GET'])
def get_all_events(username, year, month):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    from datetime import datetime as dt, date
    start_date = date(int(year), int(month), 1)
    if int(month) == 12:
        end_date = date(int(year) + 1, 1, 1)
    else:
        end_date = date(int(year), int(month) + 1, 1)
    
    events = Event.query.filter(
        Event.user_id == user.id,
        Event.date >= start_date,
        Event.date < end_date
    ).all()
    
    return jsonify({"events": [event.to_dict() for event in events]}), 200

# Delete Event
@app.route('/delete-event/<username>/<int:event_id>', methods=['DELETE'])
def delete_event(username, event_id):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    event = Event.query.filter_by(id=event_id, user_id=user.id).first()
    if not event:
        return jsonify({"error": "Event not found"}), 404
    
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted"}), 200

# Daily Task Endpoints

# Create Daily Task
@app.route('/create-daily-task/<username>', methods=['POST'])
def create_daily_task(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    task = DailyTask(
        user_id=user.id,
        date=data.get("date"),
        time=data.get("time"),
        task=data.get("task"),
        subject=data.get("subject", ""),
        duration=data.get("duration", 30),
        priority=data.get("priority", "medium")
    )
    
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created", "task": task.to_dict()}), 201

# Get Daily Tasks for Date
@app.route('/get-daily-tasks/<username>/<date>', methods=['GET'])
def get_daily_tasks(username, date):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    from datetime import datetime as dt
    task_date = dt.strptime(date, '%Y-%m-%d').date()
    tasks = DailyTask.query.filter_by(user_id=user.id, date=task_date).order_by(DailyTask.time).all()
    
    return jsonify({"tasks": [task.to_dict() for task in tasks]}), 200

# Update Task (Mark Complete)
@app.route('/update-daily-task/<username>/<int:task_id>', methods=['PUT'])
def update_daily_task(username, task_id):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    task = DailyTask.query.filter_by(id=task_id, user_id=user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.json
    task.completed = data.get("completed", task.completed)
    task.priority = data.get("priority", task.priority)
    task.duration = data.get("duration", task.duration)
    
    db.session.commit()
    return jsonify({"message": "Task updated", "task": task.to_dict()}), 200

# Delete Daily Task
@app.route('/delete-daily-task/<username>/<int:task_id>', methods=['DELETE'])
def delete_daily_task(username, task_id):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    task = DailyTask.query.filter_by(id=task_id, user_id=user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200

# Initialize Database
with app.app_context():
    db.create_all()
    print("Database tables created!")

# Initialize Database
with app.app_context():
    db.create_all()
    print("Database tables created!")

# Progress Report Endpoint
@app.route('/get-progress-report/<username>/<days>', methods=['GET'])
def get_progress_report(username, days):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    from datetime import datetime as dt, timedelta, date
    
    days_count = int(days)
    start_date = date.today() - timedelta(days=days_count)
    end_date = date.today()
    
    # Get completed tasks
    completed_tasks = DailyTask.query.filter(
        DailyTask.user_id == user.id,
        DailyTask.date >= start_date,
        DailyTask.date <= end_date,
        DailyTask.completed == True
    ).all()
    
    # Get all tasks
    all_tasks = DailyTask.query.filter(
        DailyTask.user_id == user.id,
        DailyTask.date >= start_date,
        DailyTask.date <= end_date
    ).all()
    
    # Get events
    all_events = Event.query.filter(
        Event.user_id == user.id,
        Event.date >= start_date,
        Event.date <= end_date
    ).all()
    
    # Calculate stats
    total_completed = len(completed_tasks)
    total_tasks = len(all_tasks)
    completion_rate = (total_completed / total_tasks * 100) if total_tasks > 0 else 0
    
    # Calculate total study duration
    total_study_minutes = sum(task.duration for task in completed_tasks)
    total_study_hours = total_study_minutes / 60
    
    # Get stats
    stats = Stats.query.filter_by(user_id=user.id).first()
    
    # Daily breakdown
    daily_breakdown = {}
    for task in all_tasks:
        date_str = task.date.isoformat()
        if date_str not in daily_breakdown:
            daily_breakdown[date_str] = {
                'total': 0,
                'completed': 0,
                'duration': 0,
                'tasks': []
            }
        daily_breakdown[date_str]['total'] += 1
        if task.completed:
            daily_breakdown[date_str]['completed'] += 1
            daily_breakdown[date_str]['duration'] += task.duration
        daily_breakdown[date_str]['tasks'].append(task.to_dict())
    
    # Subject breakdown
    subject_breakdown = {}
    for task in completed_tasks:
        subject = task.subject or 'No Subject'
        if subject not in subject_breakdown:
            subject_breakdown[subject] = {'count': 0, 'duration': 0}
        subject_breakdown[subject]['count'] += 1
        subject_breakdown[subject]['duration'] += task.duration
    
    return jsonify({
        "username": user.username,
        "period_days": days_count,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "stats": {
            "total_completed_tasks": total_completed,
            "total_tasks": total_tasks,
            "completion_rate": round(completion_rate, 2),
            "total_study_hours": round(total_study_hours, 2),
            "total_study_minutes": total_study_minutes,
            "total_events": len(all_events),
            "sessions": stats.sessions if stats else 0,
            "total_hours": stats.totalHours if stats else 0,
            "streak": stats.streak if stats else 0
        },
        "daily_breakdown": daily_breakdown,
        "subject_breakdown": subject_breakdown
    }), 200

# Run server
if __name__ == '__main__':
    app.run(debug=True)