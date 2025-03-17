# Shivalik Vidyalaya Report Card System

A web-based system for managing student report cards and marks lists for Shivalik Vidyalaya. This system allows teachers to:
- Add new students with their personal and academic details
- Generate and view individual student report cards
- View class-wise marks lists
- Download class marks lists in Excel format

## Setup Instructions

1. Install Python 3.8 or higher if not already installed

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and visit: http://localhost:5000

## Features

1. **Student Management**
   - Add new students with personal details
   - Record academic performance across subjects
   - Track co-curricular activities

2. **Report Card Generation**
   - Automatic calculation of total marks and grades
   - Professional layout matching school format
   - Print-friendly report card design

3. **Class Management**
   - View all students in a class
   - Download class marks list in Excel format
   - Quick access to individual student report cards

## File Structure

- `app.py` - Main application file with all routes and database models
- `requirements.txt` - Python package dependencies
- `templates/` - HTML templates for the web interface
  - `base.html` - Base template with common layout
  - `index.html` - Homepage
  - `add_student.html` - Form for adding new students
  - `view_class.html` - Class-wise student list
  - `report_card.html` - Individual student report card

## Usage

1. Start by adding students through the "Add Student" page
2. View class-wise lists through the homepage
3. Generate individual report cards by clicking "View Report Card"
4. Download class marks lists using the "Download Marks List" button

## Database

The system uses SQLite database (school.db) which will be automatically created when you first run the application.
