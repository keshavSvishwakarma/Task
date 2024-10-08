This is a simple Django application designed to manage and display a list of students. The application includes features to search for students by name and toggle the visibility of the student list.

## How It Works

### Features

1. **Show/Hide Student List:**
   - The student list is hidden by default. Click the "Show Students" button to display the list of all students. Click "Hide Students" to hide the list again.

2. **Search Students:**
   - You can search for students by their first or last name using the search box. The list will filter based on the search query.

### User Interaction

- **Show Students**: When the "Show Students" button is clicked, the student list becomes visible.
- **Hide Students**: When the "Hide Students" button is clicked, the student list is hidden.
- **Search**: Enter a student's first or last name in the search box and click "Search" to filter the displayed list.

## How to Run the Project

### Prerequisites

- Python 3.x
- Django 3.x or higher

### Setup and Running

1. **Clone the Repository:**
   git clone https://github.com/keshavSvishwakarma/Task.git
   cd  Task

2. **Set Up a Virtual Environment:**
    python -m venv venv
    `venv\Scripts\activate`
3. **Install Dependencies:**
    pip install -r requirements.txt

4. **Superuser:** 
    login Superuser 
    username : admin
    pass : admin

4. **Run the Development Server:**
    python manage.py runserver

