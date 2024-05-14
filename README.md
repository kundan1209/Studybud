# StudyBud: Django SQLite3 Study Chat Rooms Project

## Description
StudyBud is a project built using Django and SQLite3 aimed at facilitating study sessions through chat rooms. It allows users to create chat rooms based on different subjects, join existing rooms, and collaborate with others to study effectively.

## Features
- User authentication: Users can sign up, log in, and log out securely.
- Chat rooms: Users can create new chat rooms, join existing ones, and engage in real-time discussions.
- Subject categorization: Chat rooms can be categorized based on different subjects or topics for easier navigation.
- Profile management: Users can manage their profiles, including updating personal information and changing passwords.
- Admin panel: Administrators have access to an admin panel to manage users, chat rooms, and site settings.

## Installation
To run this project locally, follow these steps:
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On macOS and Linux: `source env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Create a superuser (admin account): `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`
9. Access the application in your browser at `http://localhost:8000`.

## Usage
Once the server is running, users can do the following:
- Sign up for a new account or log in with existing credentials.
- Create new chat rooms or join existing ones.
- Participate in real-time discussions within chat rooms.
- Manage their profiles, including updating personal information.
- Administrators can access the admin panel at `http://localhost:8000/admin` to manage users, chat rooms, and site settings.
