# Safi College of Medical Sciences - Website

A complete Flask website for **Safi College of Medical Sciences, Mandani, Charsadda, KPK, Pakistan**.

## Website URL

**https://www.scms.edu.pk**

## Features

- Modern, responsive design built with Bootstrap 5 and custom CSS
- Home page with hero section, programs preview, stats counter, news, and CTA
- About page with mission, vision, values, and timeline
- Programs listing with all 10 paramedical courses
- Individual program detail pages with fee structure
- Faculty directory
- Facilities showcase with gallery
- Admissions page with process and FAQ
- Contact page with form and email addresses
- News, gallery, scholarships, downloads, and custom 404 pages

## Email Addresses

- admin@scms.edu.pk
- contact@scms.edu.pk
- admissions@scms.edu.pk
- principal@scms.edu.pk

## Programs Offered

1. BS Nursing (Generic) - 4 Years
2. BS Nursing (Post RN) - 2 Years
3. BS Medical Laboratory Technology - 4 Years
4. BS Radiology & Imaging Technology - 4 Years
5. BS Physiotherapy - 4 Years
6. BS Pharmacy (Pharm-D) - 5 Years
7. BS Optometry & Vision Sciences - 4 Years
8. BS Dental Technology - 4 Years
9. BS Cardiac Perfusion Technology - 4 Years
10. BS Dialysis Technology - 4 Years

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure email settings in `app.py`:

```python
app.config['MAIL_SERVER'] = 'your-smtp-server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'admin@scms.edu.pk'
app.config['MAIL_PASSWORD'] = 'your-email-password'
```

3. Run the application:

```bash
python app.py
```

4. Open `http://localhost:5000` in your browser.

## Directory Structure

```text
scms_website/
|-- app.py
|-- requirements.txt
|-- README.md
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- about.html
|   |-- programs.html
|   |-- program_detail.html
|   |-- faculty.html
|   |-- facilities.html
|   |-- admissions.html
|   |-- contact.html
|   |-- news.html
|   |-- gallery.html
|   |-- scholarships.html
|   |-- downloads.html
|   `-- 404.html
`-- static/
    |-- css/
    |-- js/
    `-- images/
```

## Affiliation

- Khyber Medical University (KMU), Peshawar
- Pakistan Nursing Council (PNC)
- Higher Education Commission (HEC)

## Deployment Notes

For production, set `debug=False`, configure real SMTP credentials through a safer configuration method, and run the app behind a production WSGI server and HTTPS reverse proxy.

Copyright 2026 Safi College of Medical Sciences. All Rights Reserved.
