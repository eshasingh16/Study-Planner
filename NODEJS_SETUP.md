# Quick Start - Node.js Backend

## What is it?
Node.js/Express API Gateway that proxies requests to Flask backend.

## Why?
- Better API management and caching
- Load balancing capabilities
- Easy to add custom logic
- Faster development

## Installation

### 1. Install Node.js
```
https://nodejs.org/
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Start the Server
```bash
npm start
```

## Development Mode (Auto-Reload)
```bash
npm run dev
```

## Environment Variables
Edit `.env`:
```
PORT=3001
FLASK_URL=http://localhost:5000
NODE_ENV=development
```

## Available Endpoints
- Health check: `GET http://localhost:3001/health`
- All API routes: `GET/POST http://localhost:3001/api/*`

## Server Status
```bash
# Check Node.js is running
curl http://localhost:3001/health

# Should return:
# {"status":"Node.js API Server Running 🚀"}
```

## Troubleshooting

**Port 3001 already in use?**
```bash
# Find process using port
netstat -ano | findstr :3001

# Kill process (Windows PowerShell as admin)
taskkill /PID <PID> /F

# Or change PORT in .env
```

**Flask backend not connecting?**
```bash
# Make sure Flask is running first
python app.py

# Then update FLASK_URL in .env if needed
```

**Module errors?**
```bash
# Clear cache and reinstall
rm -r node_modules package-lock.json
npm install
```

## Quick Commands
```bash
npm start          # Run server
npm run dev        # Run with auto-reload
npm install        # Install dependencies
npm list           # Show installed packages
```

Happy coding! 🚀
