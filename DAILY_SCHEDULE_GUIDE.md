# Daily Schedule Planner Guide

## Overview
The Daily Schedule Planner helps you organize your study schedule hour-by-hour with tasks, subjects, and priorities.

## Features
✅ **Hourly Task Planning** - Schedule tasks with specific times
✅ **Duration Tracking** - Set how long each task takes (5-480 minutes)
✅ **Priority Levels** - Mark tasks as Low, Medium, or High priority
✅ **Task Completion** - Check off tasks as you complete them
✅ **Subject Organization** - Tag tasks with subjects
✅ **Daily Summary** - See total tasks, completed, and study time
✅ **Real-time Sync** - Changes saved to database instantly

## How to Use

### 1. Open Daily Schedule
- Click the **⏰ Schedule** icon in the navigation
- Or access from the main menu

### 2. Select a Date
- Use the date picker to choose which day to plan
- Click **"Today"** button to quickly jump to today's date
- All tasks shown are for the selected date

### 3. Add a Task
Fill in the task details:

| Field | Description | Example |
|-------|-------------|---------|
| **Time** | When the task starts | 14:00 (2:00 PM) |
| **Task Name** | What to study | Physics Review |
| **Subject** | Which subject (optional) | Physics |
| **Duration** | How long in minutes | 60 |
| **Priority** | Importance level | High/Medium/Low |

### 4. Manage Tasks
- **Track Progress**: Check the checkbox when task is done
- **Delete**: Remove tasks with Delete button
- **Visual Feedback**: Completed tasks appear faded with strikethrough

### 5. View Summary
At the bottom, see:
- **Total Tasks** - How many tasks scheduled
- **Completed** - Green number of finished tasks
- **Total Duration** - Orange total study time in minutes

## Priority Colors
- **High** (🟧 Orange) - Important tasks, exams prep
- **Medium** (🟦 Blue) - Regular study sessions
- **Low** (🟩 Green) - Light reading, break

## Example Daily Schedule

```
09:00 - Physics Mechanics (60 min) [High]
10:00 - Break (15 min) [Low]
10:15 - Mathematics Calculus (90 min) [High]
11:45 - Chemistry Organic (60 min) [Medium]
12:45 - Lunch Break (45 min) [Low]
13:30 - Quiz Practice (45 min) [High]
14:15 - Notes Review (30 min) [Medium]
14:45 - Revision (60 min) [Medium]
```

## Tips & Tricks

1. **Time Blocking**: Create 50-60 minute study blocks with 10 minute breaks
2. **Priority First**: Schedule high-priority tasks when you're fresh
3. **Buffer Time**: Add 5-10 minutes between tasks for breaks
4. **Subjects**: Always tag with subjects for easier organization
5. **Realistic**: Don't overload - leave breathing room

## Best Practices

### Morning (6 AM - 12 PM)
- Hard & conceptual subjects
- New topics
- Problem solving

### Afternoon (12 PM - 6 PM)
- Practice tests
- Revision
- Medium difficulty tasks

### Evening (6 PM - 10 PM)
- Light reading
- Consolidation
- Next day prep

## Time Management Tips

**PomodoroTechnique Example:**
```
09:00 - Study (50 min)
09:50 - Short Break (10 min)
10:00 - Study (50 min)
10:50 - Medium Break (15 min)
```

**Time Block Example:**
```
Morning: 06:00 - 12:00   (6 hours)
Afternoon: 13:00 - 17:00 (4 hours)
Evening: 19:00 - 22:00   (3 hours)
Total: 13 hours
```

## Integration with Other Features

### With Calendar
1. View monthly calendar
2. Create events for exams
3. Link daily tasks to exam dates

### With Study Planner
1. Generate exam-specific plans
2. Breakdown into daily subtasks
3. Add tasks to daily schedule

### With Focus Timer
1. See scheduled task durations
2. Use timer for each task
3. Check off when timer completes

### With Notes
1. Link task to note section
2. Take notes during task
3. Cross-reference with schedule

## Keyboard Shortcuts
- **Date Navigation**: Use date picker arrows
- **Add Task**: Fill form, press Enter in duration field
- **Complete Task**: Click checkbox
- **Delete Task**: Click Delete button
- **Today**: Jump to current date button

## Database Storage

Each task stores:
```
{
  date: "2026-03-31",
  time: "14:00",
  task: "Physics Problem Set",
  subject: "Physics",
  duration: 60,
  completed: false,
  priority: "high"
}
```

All data is per-user and persists across sessions.

## Performance Tips

1. **Daily View**: Works best with 10-15 tasks per day
2. **Planned Ahead**: Plan entire week on Sunday
3. **Flexible**: Adjust schedule as the day progresses
4. **Realistic**: Allow for unexpected delays
5. **Review**: Check schedule every morning

## Troubleshooting

**Tasks not appearing?**
- Verify you're logged in
- Check date is correct
- Ensure backend is running

**Can't create task?**
- Fill all required fields (time, task name)
- Select a valid date
- Check Node.js server status

**Changes not saving?**
- Verify Flask backend is running
- Check internet connection
- Refresh browser page

## Future Updates
- 🔔 Notifications/Reminders
- 📊 Weekly view
- 🔁 Recurring tasks
- 📱 Mobile sync
- 🎯 Goal tracking
- 📈 Analytics dashboard

## Getting Started

1. Click ⏰ Schedule icon
2. Select today's date
3. Add first task:
   - Time: 09:00
   - Task: Study Math
   - Duration: 50 min
   - Priority: High
4. Click "Add Task"
5. Repeat for all daily tasks
6. Check off tasks as you complete them

**You're ready to take control of your study schedule!** 📚✏️
