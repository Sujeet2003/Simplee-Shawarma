## Simplee Shawarma Web Page
This is a Shawarma web app built using `Django`, `Python`, `HTML`, `CSS`, `Bootstrap`, and `JavaScript`. The project is containerized using `Docker` and employs `GitHub Actions` for `CI/CD automation`.

### 🚀 Technologies Used
- `Backend`: Python, Django
- `Frontend`: HTML, CSS, Bootstrap, JavaScript
- `Database`: PostgreSQL
- `Containerization`: Docker
- `CI/CD`: GitHub Actions
- `Testing`: Unit Tests (Django TestCase), Automated Testing (Selenium)

### 🌐 Hosted On

The application is deployed on an AWS EC2 instance and can be accessed at:

Live Link: http://13.55.126.170:8000/

### 📂 Project Structure
Run command in command prompt: `tree /F /A > structure.txt`
        
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
