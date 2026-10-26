# Chatter – Django Tweet App

Chatter is a social media web application I built using Python and Django. The idea behind this project was to build something practical where users can share their thoughts, interact with other posts, and manage their own content.

While building this project, I got hands-on experience with Django views, models, forms, authentication, database relationships, and connecting the frontend with the backend.

## Features

- User registration, login, and logout
- Create tweets with text and images
- Edit and delete your own tweets
- Like and unlike tweets
- Add, edit, and delete comments
- View individual tweets on a separate detail page
- Responsive layout for different screen sizes
- Django admin support for managing application data

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite / PostgreSQL, depending on the environment
- **Image Handling:** Pillow
- **Version Control:** Git and GitHub

## Getting Started

If you want to run this project on your local machine, follow these steps.

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Now open `http://127.0.0.1:8000/` in your browser.

**Note:** If your project is configured to use PostgreSQL or environment variables, set up the required database credentials before running migrations.

## What I Learned

Working on Chatter helped me understand how a Django application works in practice. I worked with Django models and relationships, handled user authentication, implemented CRUD operations, and used forms to process user input.

I also learned how to handle image uploads, manage user permissions, and use Git to keep track of project changes.

## Future Improvements

There are still a few things I would like to add in the future, such as user profiles, a search feature, and a follow system.

## Author

**Shaik Abdul Mateen**

GitHub: [shaikabdulmateen](https://github.com/shaikabdulmateen)
