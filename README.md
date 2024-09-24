# Job Portal Project

## 1. Problem Statement

The proposed job portal aims to address the challenges faced by the working class and job seekers. Despite their willingness to work and contribute, they encounter barriers such as limited access to suitable job opportunities, inadequate support for career advancement, and socio-economic disparities.

To bridge these gaps, a dedicated job portal is essential. It should provide access to a wide range of job opportunities, offer support services such as career guidance and skills development, and address socio-economic disparities.

By empowering job seekers to find meaningful employment that supports their well-being and that of their families, the portal aims to contribute to socio-economic advancement.


---


## 2. Features

1. **Multilingual Support:** Access the portal in multiple languages to cater to diverse users.
2. **Live Job Listings:** Stay updated with real-time job opportunities.
3. **Advanced Job Filtering:** Tailor job searches according to personal preferences.
4. **Limit on Pending Applications:** Job seekers can have up to five pending job applications at a time.
5. **Resume Upload Requirement:** Apply for jobs only after uploading a resume.
6. **Application Status Insights:** Receive detailed feedback on application acceptance or rejection.
7. **Recruiter Verification:** Recruiters can post jobs after administrative approval to ensure accuracy and reliability.
8. **Comprehensive Job Management:** Recruiters can oversee and manage all their posted job listings.
9. **Administrative Oversight:** Admin has the authority to delete job seeker accounts if any discrepancies are found.
10. **Recruiter Approval Process:** Only admin can accept or reject recruiters, determining their access to the portal.

---


## 3. Technologies Used

### 1. HTML (HyperText Markup Language)
HTML is the standard language used to create web pages. It structures the content on a webpage using elements such as headings, paragraphs, images, links, and forms.

In this project, HTML is used to define the structure of various pages on the job portal, including:
- **Job Listings:** Display the list of available job opportunities.
- **Job Application Forms:** Allow job seekers to apply for jobs.
- **User Dashboard:** Structure the recruiter and admin dashboards.

### 2. CSS (Cascading Style Sheets)
CSS is used to control the visual appearance and layout of HTML elements. It is responsible for making the web pages aesthetically pleasing, responsive, and user-friendly.

In this project, CSS is applied to:
- **Job Portal Theme:** Create a clean and professional look for the job portal.
- **Responsive Design:** Ensure the job portal is accessible on different devices, including desktops, tablets, and mobile phones.
- **Custom Styling:** Enhance the user experience with styled buttons, forms, and navigation bars.

### 3. Django (Backend Framework)
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is used to manage the backend functionality of the job portal.

Key Django functionalities in this project include:
- **User Authentication:** Handle login, registration, and session management for job seekers, recruiters, and admins.
- **Database Management:** Use Django ORM to interact with the database, store job listings, user profiles, and application data.
- **Email Notifications:** Send application status updates and recruiter verification via email.
- **Admin Interface:** Provide an intuitive admin interface for managing users, job postings, and recruiters.

### 4. JavaScript (Interactive Features)
JavaScript is a dynamic programming language used to add interactivity to web pages. It enhances user experience by enabling real-time updates, form validation, and dynamic content rendering without refreshing the page.

In this project, JavaScript is used for:
- **Form Validation:** Ensure job applications and user registration forms are correctly filled before submission.
- **Asynchronous Requests (AJAX):** Load job listings, update application statuses, and submit forms without page reload.



These technologies work together to build a robust and interactive job portal, ensuring a smooth user experience for job seekers, recruiters, and administrators.

---




## 4. Project Setup and Running Instructions

Follow the steps below to set up and run this project on your local machine.

### Prerequisites

- Python 3.x installed
- `pip` package manager installed
- Django installed (included in `requirements.txt`)

--- 

## 5. Steps to Run the Project

### Step 1: Clone the Repository

First, clone the project repository (or ensure you have the project files on your machine).

```bash
git clone <repository-url>
cd /path/to/project
```

### Step 2: Create a Virtual Environment
To avoid conflicts between global and project-specific dependencies, create a virtual environment.

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment
On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:
``` bash
source venv/bin/activate
```

### Step 4: Install Dependencies
Install all the necessary dependencies listed in the requirements.txt file.
```bash
pip install -r requirements.txt
```

### Step 5: Configure the Database
Before applying migrations, ensure that the database settings in settings.py are configured correctly. By default, this project uses SQLite, but you can configure any other database by updating the DATABASES section in settings.py.


### Step 6: Run Migrations
Once the database is configured, apply the migrations to set up your database schema.
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create a Superuser (Optional)
```bash
To access the Django admin panel, create a superuser:
```
Follow the on-screen instructions to enter a username, email, and password.

### Step 8: Run the Server
Start the Django development server using the following command:

```bash
python manage.py runserver
```

This will start the server, and you can now access the portal in your browser at http://127.0.0.1:8000/.

### Step 9: Access the Admin Panel
If you created a superuser, you can access the Django admin panel at http://127.0.0.1:8000/admin/ to manage users, recruiters, and job listings.

---


## 6. Credentials
Use these credentials for testing the project.
### Recruiter
```markdown
Email Id -> 322niranjan0023@dbit.in
Password -> Jobs123!
```
### Job Seeker
```markdown
Email Id -> aakhya@313.gmail.com
Password -> Jobs123!
```
### Admin
```markdown
Email Id -> admin@dbit.com
Password -> Dbit123!
```

## Email Service
To send email notifications (e.g., password resets or job application status), configure the email service in the settings.py file with the following settings by creating your gmail account app password:
```markdown
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
```

Make sure to set the correct password for EMAIL_HOST_PASSWORD in your local environment or use environment variables to keep it secure.

