# Job Portal Backend API

A RESTful backend API for a Job Portal platform built with Django and Django REST Framework.

This project was developed as part of an internship task and focuses on building a secure backend system for Candidates and Employers, including authentication, job management, job applications, role-based access control, and API documentation.

---

## 🚀 Features

### Authentication & User Management

- User registration
- JWT-based authentication
- JWT access and refresh tokens
- Candidate and Employer roles
- Secure password hashing
- Protected API endpoints
- Role-based permissions

### Job Management

Employers can:

- Create job postings
- View their job postings
- Update their job postings
- Delete their job postings

Candidates can:

- View available jobs
- Search jobs
- Filter jobs
- View job details

### Job Search & Filtering

Jobs can be searched and filtered using:

- Job title
- Company
- Location
- Description
- Requirements
- Job type

Example:

```text
GET /api/jobs/?search=python
```

```text
GET /api/jobs/?location=Dhaka
```

```text
GET /api/jobs/?job_type=internship
```

Filters can also be combined:

```text
GET /api/jobs/?search=django&location=Dhaka&job_type=internship
```

### Job Applications

Candidates can:

* Apply to jobs
* View their applications
* Track application status

Employers can:

* View applications received for their jobs
* Update application status

Application statuses:

```text
Applied
Shortlisted
Rejected
```

Duplicate applications to the same job are prevented.

### Role-Based Access Control

The API separates permissions between Candidates and Employers.

| Action                     | Candidate | Employer |
| -------------------------- | --------: | -------: |
| View jobs                  |         ✅ |        ✅ |
| Search jobs                |         ✅ |        ✅ |
| View job details           |         ✅ |        ✅ |
| Create job                 |         ❌ |        ✅ |
| Update own job             |         ❌ |        ✅ |
| Delete own job             |         ❌ |        ✅ |
| Apply to job               |         ✅ |        ❌ |
| View own applications      |         ✅ |        ❌ |
| View received applications |         ❌ |        ✅ |
| Update application status  |         ❌ |        ✅ |

Employers can only modify jobs and applications belonging to them.

---

## 🛠️ Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### Authentication

* JWT
* djangorestframework-simplejwt

### Database

* MySQL

### API Documentation

* OpenAPI
* Swagger UI
* drf-spectacular

### Filtering

* django-filter
* Django REST Framework SearchFilter

### Development Tools

* Postman
* MySQL Workbench
* Git
* GitHub

---

## 📁 Project Structure

```text
job-portal-backend/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── jobs/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── applications/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🔐 Authentication

The API uses JWT authentication.

### Signup

```http
POST /api/auth/signup/
```

Example:

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "StrongPassword123",
    "role": "candidate"
}
```

Available roles:

```text
candidate
employer
```

### Login

```http
POST /api/auth/login/
```

Example:

```json
{
    "email": "john@example.com",
    "password": "StrongPassword123"
}
```

The API returns:

```json
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

Use the access token for protected endpoints:

```http
Authorization: Bearer <access_token>
```

### Refresh Token

```http
POST /api/auth/token/refresh/
```

---

# 💼 Job API

## List Jobs

```http
GET /api/jobs/
```

Authentication required.

## Create Job

```http
POST /api/jobs/
```

Employer only.

Example:

```json
{
    "title": "Python Backend Developer",
    "company": "Example Company",
    "location": "Dhaka",
    "salary": 30000,
    "description": "Backend development using Django.",
    "requirements": "Python, Django, DRF, MySQL",
    "job_type": "full_time"
}
```

## Get Job Details

```http
GET /api/jobs/<id>/
```

## Update Job

```http
PUT /api/jobs/<id>/
```

Employer only.

An employer can only update their own jobs.

## Delete Job

```http
DELETE /api/jobs/<id>/
```

Employer only.

An employer can only delete their own jobs.

---

# 🔎 Job Search & Filtering

### Search

```http
GET /api/jobs/?search=python
```

Searches across relevant job fields such as:

* Title
* Company
* Location
* Description
* Requirements

### Filter by Location

```http
GET /api/jobs/?location=Dhaka
```

### Filter by Job Type

```http
GET /api/jobs/?job_type=internship
```

### Filter by Company

```http
GET /api/jobs/?company=Example Company
```

### Combined Filters

```http
GET /api/jobs/?search=django&location=Dhaka&job_type=internship
```

---

# 📩 Application API

## Apply to a Job

```http
POST /api/applications/jobs/<job_id>/apply/
```

Candidate only.

No request body is required.

The authenticated candidate is automatically associated with the application.

---

## My Applications

```http
GET /api/applications/my-applications/
```

Candidate only.

Returns applications submitted by the authenticated candidate.

---

## Employer Applications

```http
GET /api/applications/job-applications/
```

Employer only.

Returns applications for jobs owned by the authenticated employer.

---

## Update Application Status

```http
PATCH /api/applications/<id>/status/
```

Employer only.

Example:

```json
{
    "status": "shortlisted"
}
```

Available statuses:

```text
applied
shortlisted
rejected
```

An employer can only update applications belonging to their own jobs.

---

# 📚 API Documentation

Interactive API documentation is available through Swagger UI when running the project locally.

```text
http://127.0.0.1:8000/api/docs/
```

OpenAPI schema:

```text
http://127.0.0.1:8000/api/schema/
```

Swagger allows developers to explore and test the available API endpoints.

---

# 🗄️ Database

The project uses MySQL as the primary database.

Main entities include:

```text
User
 │
 ├── Candidate
 │
 └── Employer
       │
       └── Jobs
             │
             └── Applications
                    │
                    └── Candidate
```

### Main Models

#### User

Stores:

* Name
* Email
* Password
* Role
* Account information

#### Job

Stores:

* Title
* Company
* Location
* Salary
* Description
* Requirements
* Job type
* Employer
* Creation date

#### Application

Stores:

* Candidate
* Job
* Application status
* Application date

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jubair65/Job-Portal-Backend.git
```

```bash
cd job-portal-backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file based on `.env.example`.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=job_portal_db
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=127.0.0.1
DB_PORT=3306
```

Do not commit `.env` to GitHub.

### 5. Create the Database

Create a MySQL database:

```sql
CREATE DATABASE job_portal_db;
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create Admin User

```bash
python manage.py createsuperuser
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

Swagger:

```text
http://127.0.0.1:8000/api/docs/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

# 🧪 API Testing

The API was tested using Postman.

Testing covered:

### Authentication

* Candidate signup
* Employer signup
* Login
* JWT token generation
* Duplicate email validation
* Invalid credentials

### Jobs

* Create job
* List jobs
* View job details
* Update job
* Delete job
* Search
* Filtering

### Applications

* Apply to job
* Duplicate application prevention
* View candidate applications
* View employer applications
* Update application status

### Security

* Authentication requirements
* Candidate restrictions
* Employer restrictions
* Job ownership
* Invalid JWT
* Missing JWT
* Invalid resources

---

# 🔒 Security

The backend includes:

* JWT authentication
* Password hashing through Django's authentication system
* Role-based permissions
* Protected API endpoints
* Employer ownership validation
* Duplicate application protection
* Input validation
* Environment-based secret configuration

Sensitive configuration such as database passwords and Django secret keys should be stored in `.env` and must not be committed to GitHub.

---

# 📌 Project Status

```text
Core Backend                 ✅
JWT Authentication           ✅
Candidate/Employer Roles     ✅
Job CRUD                     ✅
Job Search                   ✅
Job Filtering                ✅
Job Applications             ✅
Application Status           ✅
Role-Based Access Control    ✅
Ownership Protection         ✅
Django Admin                 ✅
Swagger Documentation        ✅
Postman Testing              ✅
requirements.txt             ✅
Environment Configuration    ✅
GitHub Repository            ✅
```

---

# 🎯 Internship Project

This project was developed as part of an internship backend development task.

The main objective was to design and implement a secure REST API for a job portal with separate Candidate and Employer functionality.

The project focuses on:

* REST API development
* Authentication
* Authorization
* Database design
* Role-based access control
* API testing
* Backend architecture
* Documentation

---

## 👨‍💻 Author

**Jubair Bin Hasan**

Computer Science & Engineering
University of Asia Pacific

---

## 📄 License

This project was developed for educational and internship purposes.
