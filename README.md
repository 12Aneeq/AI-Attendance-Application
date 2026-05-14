# AI Attendance Application

An AI-powered Attendance Management System built using Python and Streamlit that uses both **Face Recognition** and **Voice Recognition** for secure and smart attendance marking.

The application provides separate interfaces for **Students** and **Teachers**, enabling efficient attendance management, subject handling, and authentication in an interactive web application.

---

## Features

### Student Interface
- Secure student login and authentication
- Face recognition–based identity verification
- Voice recognition for attendance confirmation
- Automated attendance marking
- Simple and interactive dashboard

### Teacher Interface
- Dedicated teacher dashboard
- Create and manage subjects
- View and manage attendance records
- Monitor student attendance efficiently
- Subject-wise attendance tracking

### AI & Security Features
- Dual biometric attendance system (Face + Voice)
- Secure password hashing using bcrypt
- Machine learning–based recognition system
- Real-time attendance verification

---

## Project Structure

```bash
AI-Attendance-Application/
│
├── assets/              # Images and static assets
├── src/                 # Source code modules
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignored files and folders
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/12Aneeq/AI-Attendance-Application.git
cd AI-Attendance-Application
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Technologies Used

- Python
- Streamlit
- Supabase
- Scikit-learn
- bcrypt
- NumPy
- Pandas

---

## Future Improvements

- Real-time analytics dashboard
- Attendance report export
- Mobile-friendly interface
- Multi-user classroom support
- Cloud deployment enhancements
- Advanced biometric accuracy improvements

---

## Author

**Aneeq**

GitHub: https://github.com/12Aneeq
