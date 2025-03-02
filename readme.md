# Suborno Deb Bappon Portfolio Website

This Django-based portfolio website showcases all aspects of my resume including Summary, Technical Skills, Experience, Education, Projects, Publications, Certifications, Awards, Extracurricular Activities, and more. It uses Bootstrap for an attractive UI and django‑distill to export a static version for free deployment on GitHub Pages.

## Project Structure

portfolio_project/
├── manage.py
├── portfolio_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py        
├── portfolio/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py       
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── portfolio/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── about.html
│   │       ├── experience.html
│   │       ├── education.html
│   │       ├── projects.html
│   │       ├── publications.html
│   │       ├── certifications.html
│   │       ├── awards.html
│   │       ├── extracurricular.html
│   │       └── contact.html
│   └── static/
│       └── portfolio/
│           ├── css/
│           │   └── style.css
│           ├── js/
│           │   └── main.js
│           └── images/  
├── requirements.txt
└── README.md


