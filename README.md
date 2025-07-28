# SCT_CS_4
# 🧠 Futuristic Keylogger Interface – Full Stack Edition

This project is a full-stack simulation of a **neural keystroke monitoring system**, combining a Python keylogger backend with a futuristic cyberpunk-style React frontend.

---

## 🚀 Features

- ✅ Real-time keylogging with [`pynput`](https://pynput.readthedocs.io/)
- ✅ Flask API backend serving keystroke logs
- ✅ Cyberpunk-themed terminal UI using React
- ✅ Animated scanlines, glowing borders, and terminal cursor effects
- ✅ Live data updates every 2 seconds from backend

---

## 📁 Project Structure

project/
├── backend/
│ └── app.py # Flask + pynput keylogger
├── frontend/
│ └── index.html # React-based futuristic terminal
├── keylog.txt # Local file for key logs

---

## 🛠️ Technologies Used

- **Frontend:** HTML, React (via Babel), Vanilla CSS (Cyberpunk-themed)
- **Backend:** Python, Flask, Flask-CORS, pynput
- **Logging File:** `keylog.txt`

---

## ⚙️ How to Run

### 🔧 Backend (Python)

1. Install dependencies:
   ```bash
   pip install flask flask-cors pynput
Run the Flask server:
     python backend/app.py

💻 Frontend (React)
Open frontend/index.html in your browser.

Make sure the backend is running at http://localhost:5000.

You’ll see live key logs updating every 2 seconds.
