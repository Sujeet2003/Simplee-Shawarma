## Simplee Shawarma Web Page
This is a Shawarma web app built using `Django`, `Python`, `HTML`, `CSS`, `Bootstrap`, and `JavaScript`. The project is containerized using `Docker` and employs `GitHub Actions` for `CI/CD automation`.

### 🚀 Technologies Used
- `Backend`: Python, Django
- `Frontend`: HTML, CSS, Bootstrap, JavaScript
- `Database`: PostgreSQL
- `Containerization`: Docker
- `CI/CD`: GitHub Actions
- `Testing`: Unit Tests (Django TestCase), Automated Testing (Selenium)

### 📂 Project Structure
`tree /F /A > structure.txt`
SIMPLEE
|   .dockerignore
|   .gitignore
|   chromedriver.exe
|   db.sqlite3
|   Dockerfile
|   manage.py
|   README.md
|   requirements.txt
|   selenium.py
|   structure.txt
|   tests.py
|   
+---.github
|   \---workflows
|           main.yml
|           
+---Base
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |   
|   +---migrations
|   |   |   0001_initial.py
|   |   |   __init__.py
|   |   |   
|   |   \---__pycache__
|   |           0001_initial.cpython-312.pyc
|   |           0002_menuitems_delete_starter.cpython-312.pyc
|   |           0003_addon_combosforone_combosfortwo_healthyshawarma_and_more.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   \---__pycache__
|           admin.cpython-312.pyc
|           apps.cpython-312.pyc
|           forms.cpython-312.pyc
|           models.cpython-312.pyc
|           tests.cpython-312.pyc
|           urls.cpython-312.pyc
|           views.cpython-312.pyc
|           __init__.cpython-312.pyc
|           
+---logs
|       main.log
|       
+---Simplee
|   |   asgi.py
|   |   settings.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
|   |   
|   \---__pycache__
|           settings.cpython-312.pyc
|           urls.cpython-312.pyc
|           wsgi.cpython-312.pyc
|           __init__.cpython-312.pyc
|           
+---static
|   +---css
|   |       style.css
|   |       
|   +---images
|   |       24-hours.png
|   |       discount.png
|   |       logo.png
|   |       parking-img.png
|   |       shawarma-1.jpg
|   |       shawarma-2.jpg
|   |       shawarma-4.jpg
|   |       wifi.png
|   |       
|   \---js
|           custom.js
|           
+---templates
|       about.html
|       contact.html
|       contents.html
|       home.html
|       index.html
|       menu.html
|       
\---__pycache__
        tests.cpython-312.pyc
        
### ⚙️ Docker Setup
FROM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

`Run Docker Command`
- docker build -t simplee-shawarma .
- docker run -p 8000:8000 simplee-shawarma

### 🛠️ CI/CD with GitHub Actions
The project includes an automated CI/CD pipeline using GitHub Actions to:
- Run Django tests
- Build and push a Docker image to Docker Hub
Corresponding File is: `.github/workflows/main.yml`

### 🧪 Unit Testing
Implemented unit tests using Django's TestCase over the `Models (Databases)`, `Views` and `URLs`.

Corresponding File is: `tests.py`

### 🔍 Manual Testing with Selenium
Implemented manual tests over all the functionalities used in website.

Corresponding File is: `selenium.py`

### 🎯 Conclusion
Simplee Shawarma is a full-stack Django-based web application with automated testing and deployment. It follows best practices for CI/CD, unit testing, and Dockerization to ensure a scalable and maintainable website.