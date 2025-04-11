# Face Recognition Based Attendance System

This project is a **Face Recognition Powered Attendance System** that allows users to mark their attendance simply by logging in and presenting their face. It uses computer vision to identify registered users and records attendance automatically.

---

## 🎯 Objective

To automate the attendance process using facial recognition technology — eliminating the need for manual marking or ID-based check-ins.

---

## 🔐 Login Form

The `Login_Form` folder contains the **user authentication interface**. Only authorized users can access the face recognition and attendance functionality.

### Features:
- Secure login for registered users  
- Input validation for user credentials  
- Smooth and clean UI  
- Gateway to facial recognition attendance module  

---

## 🧠 How It Works

1. **User logs in** via the login form.  
2. Upon successful authentication, the system activates the webcam.  
3. The user's face is captured and matched with the trained dataset.  
4. If recognized, attendance is marked automatically with date and time.  
5. A log is maintained for future reference.  

---

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, OpenCV, `face_recognition` (for face detection & recognition)  
- **Database**: MySQL  

---

## 📁 Project Structure (Simplified)

FaceIn/ ├── Login_Form/ │ ├── index.html │ ├── style.css │ ├── login.js / login.php │ └── README.md ├── FaceRecognition/ │ ├── train_model.py │ ├── recognize_face.py │ └── attendance_log.csv

yaml
Copy
Edit

---

## ✅ Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SmritiSah/FaceIn.git
Navigate to the project directory:

bash
Copy
Edit
cd FaceIn
Run the face recognition script:

bash
Copy
Edit
python recognize_face.py
Open the login form:

Navigate to Login_Form/index.html

Open it in your browser

Authenticate and mark attendance:

Log in with your credentials

Present your face to the webcam

If matched, attendance will be recorded automatically

🧪 Future Enhancements
Mask detection

Emotion tracking

Cloud sync of attendance

Mobile app integration
