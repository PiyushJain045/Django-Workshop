# Module 1

## 🛠️ Module 1

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

```bash
.\venv\Scripts\activate
```

### 3. Install Django using requirements.txt

Create a requirements.txt file:
```bash
django
```

Then install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Create a Django Project

```bash
django-admin startproject backend_core
cd backend_core
```

### 5. Create a Django App

```bash
python manage.py startapp e_commerce
```

**What is a Django app?**  
A Django app is like a mini-program.  
Your Django project is the entire website.  
Each app is a piece of that website.  
Example: 'Authentication' feature, 'Cart' feature, checkout feature.  
In our case, we will include all the features inside a single app to keep the project beginner-friendly.

### 6. Register the App in settings.py

```python
INSTALLED_APPS = [
    ...
    'e_commerce',
]
```

### 7. Set Up Templates, Static Files, and urls.py in app directory

### 8. Apply migrations

```bash
python manage.py makemigrations  # Tells Django to detect changes in your models.py
python manage.py migrate        # Applies those migrations
```

### 9. Local development server

```
http://127.0.0.1:8000/
```
- Local development server address  
- 8000 is the port number
```