# Aurelia Complete Architecture

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend (React)                          │
│                  index.html / Next.js                       │
│                  (Port: 5173 or Local)                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ HTTP Requests
                           ▼
┌─────────────────────────────────────────────────────────────┐
│           Node.js/Express API Gateway                        │
│                  (Port: 3001)                              │
│    • Request routing & validation                          │
│    • CORS handling                                         │
│    • Request logging                                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Proxies to
                           ▼
┌─────────────────────────────────────────────────────────────┐
│           Flask Backend (Python)                             │
│                  (Port: 5000)                              │
│    • Business logic                                        │
│    • Authentication                                        │
│    • Database queries                                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ ORM (SQLAlchemy)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│           PostgreSQL Database                               │
│   Users | Notes | Stats | Sessions                         │
└─────────────────────────────────────────────────────────────┘
```

## 📂 Project Structure

```
ADD Project/
├── index.html              # React Frontend UI
├── style.css               # Frontend Styles
├── app.py                  # Flask Backend (Python)
├── server.js               # Node.js/Express Gateway
├── package.json            # Node.js Dependencies
├── requirements.txt        # Python Dependencies
├── .env                    # Environment Variables
├── SETUP.md                # Complete Setup Guide
├── NODEJS_SETUP.md         # Node.js Quick Start
└── ARCHITECTURE.md         # This file
```

## 🚀 Startup Sequence

### Step 1: Start PostgreSQL
```bash
# PostgreSQL should already be running as a service
# Verify: pg_isready
```

### Step 2: Start Flask Backend
```bash
# Terminal 1
python app.py
# Output: Running on http://localhost:5000
```

### Step 3: Start Node.js API Gateway
```bash
# Terminal 2
npm install  # First time only
npm start
# Output: Node.js API Server running on http://localhost:3001
```

### Step 4: Open Frontend
```bash
# Browser
http://localhost/ADD\ Project/index.html
# Or just open index.html in your browser
```

## 🔄 Data Flow Example: User Login

```
1. User enters credentials in Frontend
   └─> username: "john", password: "pass123"
   
2. Frontend sends to Node.js API
   └─> POST http://localhost:3001/api/login
   
3. Node.js forwards to Flask
   └─> POST http://localhost:5000/login
   
4. Flask queries PostgreSQL
   └─> Check User table
   
5. Flask returns response (success/error)
   └─> Node.js receives response
   
6. Node.js forwards to Frontend
   └─> Frontend updates UI
```

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    name VARCHAR(120),
    bio TEXT,
    target_exam VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Notes Table
```sql
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER FOREIGN KEY REFERENCES users(id),
    content TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Stats Table
```sql
CREATE TABLE stats (
    id SERIAL PRIMARY KEY,
    user_id INTEGER FOREIGN KEY REFERENCES users(id),
    sessions INTEGER DEFAULT 0,
    totalHours FLOAT DEFAULT 0.0,
    streak INTEGER DEFAULT 1
);
```

## 🔌 API Endpoints (via Node.js)

```
Authentication:
  POST   /api/register          - Register new user
  POST   /api/login             - Login user

Profile:
  GET    /api/profile/:username - Get user profile
  PUT    /api/profile/:username - Update profile

Notes:
  GET    /api/get-notes/:username    - Retrieve notes
  POST   /api/save-notes/:username   - Save notes

Stats:
  POST   /api/update-stats/:username - Update session stats

Study Planner:
  POST   /api/generate-plan     - Generate study plan
```

## 🔐 Security Features

- ✅ Password hashing using werkzeug
- ✅ CORS enabled for cross-origin requests
- ✅ Input validation on backend
- ✅ Per-user data isolation
- ✅ Environment variables for sensitive data

## 📈 Scaling Tips

To add more features:

1. **Add to Flask** (app.py)
   - New database models
   - New business logic
   - New routes

2. **Add to Node.js** (server.js)
   - Proxy the new endpoint
   - Add middleware if needed
   - Handle errors gracefully

3. **Update Frontend** (index.html)
   - Call the new API endpoints
   - Update UI components
   - Add state management

## 🐛 Debugging

### Check Flask Backend
```bash
curl http://localhost:5000
```

### Check Node.js Gateway
```bash
curl http://localhost:3001/health
```

### Check PostgreSQL
```bash
psql -U postgres -c "SELECT 1;"
```

### Monitor Logs
```bash
# Flask logs show in terminal
# Node.js logs show in terminal
# PostgreSQL logs at /var/log/postgresql/
```

## 📝 Environment Variables

Create `.env` file:
```
# Node.js
PORT=3001
NODE_ENV=development

# Flask Connection
FLASK_URL=http://localhost:5000

# Database (configure in app.py)
DATABASE_URL=postgresql://postgres:password@localhost:5432/aurelia_db
```

## 🎯 Next Steps

1. ✅ Install Node.js and PostgreSQL
2. ✅ Run `npm install` to install packages
3. ✅ Start all three services
4. ✅ Open `index.html` in browser
5. ✅ Create an account and test features!

## 💬 Support

Need help? Check:
- [SETUP.md](SETUP.md) - Detailed installation
- [NODEJS_SETUP.md](NODEJS_SETUP.md) - Node.js troubleshooting
- Flask docs: https://flask.palletsprojects.com/
- Express docs: https://expressjs.com/

Happy coding! 🚀
