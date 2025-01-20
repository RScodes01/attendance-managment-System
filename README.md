# Attendance Tracker - College Management System

## Overview
The **Attendance Tracker** project is a web-based application designed to help professors manage and track student attendance for a college. Professors can log in to the system, view student lists for different divisions, mark attendance (Present/Absent), and generate reports for individual students. The system also allows adding and removing students from the database, making it easy to manage attendance data.

This project is built using **Python**, **Flask**, **SQLite**, and **Bootstrap**.

## Features
- **Professor Login:** Secure login for professors to access the system.
- **Student Management:** Add and remove students from the system.
- **Mark Attendance:** Professors can mark attendance as Present or Absent for each student.
- **Attendance Report:** Generate reports showing each student's attendance for a given month, displaying the number of days present and absent.
- **Responsive UI:** A modern, mobile-friendly interface using **Bootstrap**.
- **SQLite Database:** Simple and lightweight database to store professor, student, and attendance information.

## Tech Stack
- **Frontend:**
  - HTML
  - CSS
  - Bootstrap
- **Backend:**
  - Python (Flask)
  - SQLite (Database)
- **Other:**
  - Jinja2 (Template engine for Flask)

## Requirements
- Python 3.7 or higher
- Flask
- SQLite (SQLite comes pre-installed with Python)
  
To install the required Python packages, run the following command:
```bash
pip install flask
