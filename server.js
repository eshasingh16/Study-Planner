// Node.js/Express API Server for Aurelia
const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const axios = require('axios');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Flask Backend URL
const FLASK_URL = process.env.FLASK_URL || 'http://localhost:5000';

// Health Check
app.get('/health', (req, res) => {
  res.json({ status: 'Node.js API Server Running 🚀' });
});

// Proxy Routes to Flask Backend
app.post('/api/register', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/register`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.post('/api/login', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/login`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.post('/api/save-notes/:username', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/save-notes/${req.params.username}`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.get('/api/get-notes/:username', async (req, res) => {
  try {
    const response = await axios.get(`${FLASK_URL}/get-notes/${req.params.username}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.get('/api/profile/:username', async (req, res) => {
  try {
    const response = await axios.get(`${FLASK_URL}/profile/${req.params.username}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.put('/api/profile/:username', async (req, res) => {
  try {
    const response = await axios.put(`${FLASK_URL}/profile/${req.params.username}`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.post('/api/update-stats/:username', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/update-stats/${req.params.username}`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.post('/api/generate-plan', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/generate-plan`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

// Calendar/Event Routes
app.post('/api/create-event/:username', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/create-event/${req.params.username}`, req.body);
    res.status(201).json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.get('/api/get-events/:username/:date', async (req, res) => {
  try {
    const response = await axios.get(`${FLASK_URL}/get-events/${req.params.username}/${req.params.date}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.get('/api/get-all-events/:username/:year/:month', async (req, res) => {
  try {
    const response = await axios.get(`${FLASK_URL}/get-all-events/${req.params.username}/${req.params.year}/${req.params.month}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.delete('/api/delete-event/:username/:event_id', async (req, res) => {
  try {
    const response = await axios.delete(`${FLASK_URL}/delete-event/${req.params.username}/${req.params.event_id}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

// Daily Task Routes
app.post('/api/create-daily-task/:username', async (req, res) => {
  try {
    const response = await axios.post(`${FLASK_URL}/create-daily-task/${req.params.username}`, req.body);
    res.status(201).json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.get('/api/get-daily-tasks/:username/:date', async (req, res) => {
  try {
    const response = await axios.get(`${FLASK_URL}/get-daily-tasks/${req.params.username}/${req.params.date}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.put('/api/update-daily-task/:username/:task_id', async (req, res) => {
  try {
    const response = await axios.put(`${FLASK_URL}/update-daily-task/${req.params.username}/${req.params.task_id}`, req.body);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

app.delete('/api/delete-daily-task/:username/:task_id', async (req, res) => {
  try {
    const response = await axios.delete(`${FLASK_URL}/delete-daily-task/${req.params.username}/${req.params.task_id}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

// Progress Report Route
app.get('/api/get-progress-report/:username/:days', async (req, res) => {
  try {
    const response = await axios.get(`${FLASK_URL}/get-progress-report/${req.params.username}/${req.params.days}`);
    res.json(response.data);
  } catch (error) {
    res.status(error.response?.status || 500).json(error.response?.data || { error: 'Server error' });
  }
});

// Error Handling Middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal Server Error' });
});

// Start Server
app.listen(PORT, () => {
  console.log(`📡 Node.js API Server running on http://localhost:${PORT}`);
  console.log(`🔗 Connected to Flask backend at ${FLASK_URL}`);
});
