# Calendar & Schedule Feature Guide

## Overview
Aurelia now includes a fully functional calendar where you can:
- ✅ View monthly calendar
- ✅ Mark dates with events
- ✅ Create study schedules
- ✅ Plan exams and breaks
- ✅ Color-coded by event type

## How to Use

### 1. Open Calendar
- Click the **📅 Calendar** icon in the navigation
- Or click on **"Schedule & Calendar"** in the main menu

### 2. Navigate Months
- Click **Prev** button to go to previous month
- Click **Next** button to go to next month
- Current month/year displays at the top

### 3. Create Event
1. Click on any date in the calendar
2. Enter event details:
   - **Title** (required) - Name of the event
   - **Time** - When the event starts (24-hour format)
   - **Description** - Additional notes
   - **Category** - Type of event (Study, Exam, Break, Revision)
3. Click **"Add Event"** button
4. Event appears immediately on the calendar

### 4. View Events
- **Green dot (●)** on calendar date = Event scheduled
- Click date to view all events for that day
- Events display with:
  - Time
  - Title
  - Category
  - Description

## Event Categories

| Category | Color | Use Case |
|----------|-------|----------|
| Study | Blue | Regular study sessions |
| Exam | Orange | Exam dates |
| Break | Green | Rest days |
| Revision | Cyan | Revision sessions |

## Color Indicators

- **Blue border** - Currently selected date
- **Green dot** - Date has events
- **Green background** - Active event date
- **Orange/Blue/Green border** - Event type in list

## Features

### Smart Calendar Grid
- Shows full month at a glance
- Sunday to Saturday layout
- Automatically fills empty slots
- Responsive grid layout

### Event Management
- **Add** events to any date
- **View** all events for selected date
- **Delete** events (coming soon)
- **Edit** event details (coming soon)

### Data Persistence
- All events saved to PostgreSQL database
- Events synced across devices
- Persist after logout
- Per-user events (each user has own calendar)

## Backend API Endpoints

```
POST   /api/create-event/<username>          - Create new event
GET    /api/get-events/<username>/<date>     - Get events for specific date
GET    /api/get-all-events/<username>/<year>/<month> - Get month's events
DELETE /api/delete-event/<username>/<event_id>      - Delete event
```

## Example Usage

### Create Study Session
```
Date: 2026-03-31
Title: Physics Chapter 5
Time: 14:00
Category: Study
Description: Electromagnetic induction and laws
```

### Create Exam Reminder
```
Date: 2026-04-15
Title: JEE Main Exam
Time: 08:00
Category: Exam
Description: Full mock test
```

### Create Break Day
```
Date: 2026-04-10
Title: Weekly Break
Time: 00:00
Category: Break
Description: Rest and rejuvenate
```

## Tips & Tricks

1. **Color Coding**: Use categories to quickly identify event types
2. **Time Planning**: Add multiple events per day for structured schedule
3. **Study Plan**: Create events for each subject
4. **Exam Prep**: Mark important dates and milestones
5. **Break Schedule**: Add break days to maintain balance

## Keyboard Shortcuts
- Navigate: Use arrow buttons for month navigation
- Select Date: Click on any date in calendar
- Create Event: Click date, fill form, click Add Event

## Troubleshooting

**Events not showing?**
- Make sure backend server is running
- Check Flask connection status
- Refresh browser page

**Can't create event?**
- Ensure title is entered
- Select a date first
- Check Node.js server is running

**Calendar not loading?**
- Verify you're logged in
- Check internet connection
- Try refreshing the page

## Future Features (Coming Soon)
- Edit existing events
- Delete events with confirmation
- Event notifications/reminders
- Recurring events
- Export calendar to PDF
- Share calendar with friends
- Color customization

## Integration with Study Plan

Calendar works with AI Study Planner:
1. Generate a study plan in **Planner** tab
2. Create events in **Calendar** for each subject
3. Track your progress with **Stats**
4. Review study sessions with **Focus Timer**

All features are fully synced in real-time! 🗓️
