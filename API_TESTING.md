# API Testing Guide

## Test with curl (Windows PowerShell)

### 1. Register User
```powershell
$body = @{
    username = "testuser"
    password = "password123"
    email = "test@example.com"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3001/api/register" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

### 2. Login User
```powershell
$body = @{
    username = "testuser"
    password = "password123"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3001/api/login" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

### 3. Save Notes
```powershell
$body = @{
    notes = "This is my study note about calculus"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3001/api/save-notes/testuser" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

### 4. Get Notes
```powershell
Invoke-WebRequest -Uri "http://localhost:3001/api/get-notes/testuser"
```

### 5. Get Profile
```powershell
Invoke-WebRequest -Uri "http://localhost:3001/api/profile/testuser"
```

### 6. Update Profile
```powershell
$body = @{
    name = "Test User"
    bio = "A passionate student"
    target_exam = "JEE"
    email = "test@example.com"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3001/api/profile/testuser" `
    -Method PUT `
    -ContentType "application/json" `
    -Body $body
```

### 7. Generate Study Plan
```powershell
$body = @{
    exam = "JEE Main"
    days = "30"
    hours = "8"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:3001/api/generate-plan" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body
```

### 8. Update Stats
```powershell
Invoke-WebRequest -Uri "http://localhost:3001/api/update-stats/testuser" `
    -Method POST `
    -ContentType "application/json"
```

## Test with Postman

### 1. Create Collection
- Name: "Aurelia API"
- Base URL: `{{base_url}}`

### 2. Add Environment
- Variable: `base_url` = `http://localhost:3001`

### 3. Add Requests

**Register**
- Method: POST
- URL: `{{base_url}}/api/register`
- Body (JSON):
```json
{
  "username": "postmanuser",
  "password": "pass123",
  "email": "postman@test.com"
}
```

**Login**
- Method: POST
- URL: `{{base_url}}/api/login`
- Body:
```json
{
  "username": "postmanuser",
  "password": "pass123"
}
```

**Save Notes**
- Method: POST
- URL: `{{base_url}}/api/save-notes/postmanuser`
- Body:
```json
{
  "notes": "Important notes about physics"
}
```

**Get Notes**
- Method: GET
- URL: `{{base_url}}/api/get-notes/postmanuser`

**Get Profile**
- Method: GET
- URL: `{{base_url}}/api/profile/postmanuser`

**Update Profile**
- Method: PUT
- URL: `{{base_url}}/api/profile/postmanuser`
- Body:
```json
{
  "name": "John Doe",
  "bio": "Aspiring engineer",
  "target_exam": "JEE",
  "email": "john@test.com"
}
```

**Generate Plan**
- Method: POST
- URL: `{{base_url}}/api/generate-plan`
- Body:
```json
{
  "exam": "NEET UG",
  "days": "60",
  "hours": "6"
}
```

**Update Stats**
- Method: POST
- URL: `{{base_url}}/api/update-stats/postmanuser`

## Quick Terminal Tests

```bash
# Check servers running
curl http://localhost:3001/health
curl http://localhost:5000

# Test login in one line
$body = @{username="admin";password="password"} | ConvertTo-Json; Invoke-WebRequest -Uri http://localhost:3001/api/login -Method POST -ContentType application/json -Body $body

# Get current user profile
curl http://localhost:3001/api/profile/admin
```

## Response Format

All responses return JSON:

**Success (200, 201)**
```json
{
  "message": "Success message",
  "data": {}
}
```

**Error (400, 401, 404, 500)**
```json
{
  "error": "Error message"
}
```

## Expected Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created |
| 400 | Bad Request - Invalid data |
| 401 | Unauthorized - Invalid credentials |
| 404 | Not Found - User not found |
| 500 | Server Error - Backend error |

## Frontend Integration

Already configured in `index.html`:
- All API calls use `http://localhost:3001/api/*`
- Automatic fallback to localhost:5000 if Node.js unavailable
- Error handling and user feedback

Test it by:
1. Opening index.html
2. Creating an account
3. Saving notes
4. Logging out and back in
5. Notes should still be there!

Happy testing! 🧪
