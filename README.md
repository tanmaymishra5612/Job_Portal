# 🏢 Job Application Portal

A full-stack **Job Application Portal** built with Python and Django, where candidates can browse and apply for jobs, and admins can manage everything from a dedicated backend panel.

---

## 🚀 Live Demo

> Run locally using the steps below.

---

## 📸 Features

### 👨‍💼 For Candidates
- Browse all available job openings
- Filter jobs by role/title
- Apply for jobs with a simple form (Name, Email, Phone)
- Duplicate application prevention per job

### 🔧 For Admins
- Dedicated Admin Panel at `/admin-panel/`
- Add, Edit, Delete job postings
- View all received applications
- Filter applicants by job role
- Django's built-in superuser admin at `/admin/`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Database | SQLite (Django ORM) |
| Frontend | HTML5, Bootstrap 5 |
| Security | CSRF Protection, Django Auth |

---

## 📁 Project Structure

```
job_portal/
├── job_portal/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py
├── jobs/
│   ├── templates/
│   │   └── jobs/
│   │       ├── base.html              # Base layout with navbar
│   │       ├── job_list.html          # Home — all job listings
│   │       ├── apply.html             # Candidate application form
│   │       ├── admin_dashboard.html   # Admin panel
│   │       └── job_form.html          # Add/Edit job form
│   ├── migrations/
│   ├── admin.py           # Model registration
│   ├── forms.py           # Django forms
│   ├── models.py          # Job & Applicant models
│   ├── urls.py            # App URL routing
│   └── views.py           # Business logic
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/job-portal.git
cd job-portal
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🌐 URL Routes

| URL | Description |
|-----|-------------|
| `/` | Job listings page |
| `/apply/<job_id>/` | Apply for a specific job |
| `/admin-panel/` | Admin dashboard |
| `/admin-panel/add/` | Add new job posting |
| `/admin-panel/edit/<job_id>/` | Edit existing job |
| `/admin-panel/delete/<job_id>/` | Delete a job |
| `/admin/` | Django built-in admin |

---

## 🗃️ Models

### Job
| Field | Type |
|-------|------|
| title | CharField |
| description | TextField |
| skills | CharField |
| location | CharField |
| created_at | DateTimeField |

### Applicant
| Field | Type |
|-------|------|
| job | ForeignKey (Job) |
| name | CharField |
| email | EmailField |
| phone | CharField |
| applied_at | DateTimeField |

> **Note:** `unique_together = ('job', 'email')` prevents duplicate applications per job.

---

## 🔐 Security Features

- ✅ CSRF protection on all forms
- ✅ Duplicate application prevention via database constraints
- ✅ Superuser authentication for admin access
- ✅ Django's built-in form validation

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Tanmay Mishra**  
[![GitHub](https://img.shields.io/badge/GitHub-tanmaymishra5612-black?logo=github)](https://github.com/tanmaymishra5612)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Tanmay_Mishra-blue?logo=linkedin)](https://www.linkedin.com/in/tanmay-mishra-0ab1b2279/
)
[![Email](https://img.shields.io/badge/Email-tanmaymishra5612@gmail.com-red?logo=gmail)](mailto:tanmaymishra5612@gmail.com)

---

⭐ **If you found this project helpful, please give it a star!**
