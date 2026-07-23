# Aurelia Backend + PostgreSQL + Node.js Setup Guide

## Architecture
- **Flask** (Python) - Database & Core APIs
- **Node.js/Express** - API Gateway/Proxy Layer
- **Next.js** (Frontend) - React UI
- **PostgreSQL** - Database

## Prerequisites
1. PostgreSQL installed and running
2. Python 3.8+
3. Node.js 16+ and npm

## Installation Steps

### 1. Install PostgreSQL
- Download from: https://www.postgresql.org/download/
- During installation, set password for `postgres` user (recommended: `password`)
- Make sure PostgreSQL runs on localhost:5432 (default)

### 2. Create Database
Open PostgreSQL shell and run:
```sql
CREATE DATABASE aurelia_db;
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Connection
Update the database URL in `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:YOUR_PASSWORD@localhost:5432/aurelia_db'
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 5. Run the Backend
```bash
python app.py
```

You should see:
```
Database tables created!
Running on http://localhost:5000
```

## Node.js Setup (Express API Gateway)

### 1. Install Node.js
- Download from: https://nodejs.org/ (LTS recommended)
- Verify installation: `node -v` and `npm -v`

### 2. Install Dependencies
```bash
npm install
```

### 3. Run Node.js Server
```bash
npm start
```

Or for development with auto-reload:
```bash
npm run dev
```

You should see:
```
📡 Node.js API Server running on http://localhost:3001
🔗 Connected to Flask backend at http://localhost:5000
```

### 4. Verify Both Servers
- Flask: `curl http://localhost:5000` 
- Node.js: `curl http://localhost:3001/health`

## Database Schema

### Users Table
- username (unique)
- password (hashed)
- email (unique)
- name, bio, target_exam
- created_at timestamp

### Notes Table
- content (user's notes)
- user_id (foreign key)
- created_at, updated_at timestamps

### Stats Table
- sessions (count)
- totalHours (float)
- streak (count)
- user_id (foreign key)

## API Endpoints

### Node.js API Gateway (Recommended - Use These!)
All endpoints are proxied through Node.js on port `3001`:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/register` | POST | Register new user |
| `/api/login` | POST | Login user |
| `/api/profile/<username>` | GET | Get user profile |
| `/api/profile/<username>` | PUT | Update profile |
| `/api/save-notes/<username>` | POST | Save notes |
| `/api/get-notes/<username>` | GET | Get notes |
| `/api/update-stats/<username>` | POST | Update study stats |
| `/api/generate-plan` | POST | Generate study plan |

**Frontend should call:** `http://localhost:3001/api/*`

### Direct Flask Endpoints (Backup)
If Node.js is down, you can call Flask directly on port `5000`:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/register` | POST | Register new user |
| `/login` | POST | Login user |
| `/profile/<username>` | GET | Get user profile |
| `/profile/<username>` | PUT | Update profile |
| `/save-notes/<username>` | POST | Save notes |
| `/get-notes/<username>` | GET | Get notes |
| `/update-stats/<username>` | POST | Update study stats |
| `/generate-plan` | POST | Generate study plan |

**Direct Flask call:** `http://localhost:5000/*`

## Troubleshooting

**Database connection error?**
- Check PostgreSQL is running: `pg_isready`
- Verify credentials in `app.py`
- Make sure `aurelia_db` exists

**Modules not found (Python)?**
- Run: `pip install -r requirements.txt`

**Node.js modules not found?**
- Run: `npm install`
- Delete `node_modules` and `package-lock.json`, then run `npm install` again

**Port 5000 already in use?**
- Change in `app.py`: `app.run(debug=True, port=5001)`

**Port 3001 already in use?**
- Change in `.env`: `PORT=3002`
- Update frontend API calls to `http://localhost:3002`

**Can't connect Flask to Node.js?**
- Make sure Flask is running first: `python app.py`
- Check `.env` has correct Flask URL: `FLASK_URL=http://localhost:5000`
- Restart Node.js server: `npm start`

## Running Everything

### Terminal 1 - PostgreSQL
```bash
pg_isready
```
(Should already be running as a service)

### Terminal 2 - Flask Backend
```bash
python app.py
```

### Terminal 3 - Node.js API
```bash
npm start
```

Now all services are running! 🎉
