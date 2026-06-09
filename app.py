from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'scms-secret-key-2026'

# Flask-Mail Configuration (Update with your SMTP settings)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'admin@scms.edu.pk'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_DEFAULT_SENDER'] = 'admin@scms.edu.pk'

mail = Mail(app)

# College Information
COLLEGE_INFO = {
    'name': 'Safi College of Medical Sciences',
    'short_name': 'SCMS',
    'tagline': 'Excellence in Healthcare Education',
    'location': 'Mandani, Charsadda, Khyber Pakhtunkhwa, Pakistan',
    'address': 'Mandani Road, Charsadda, KPK, Pakistan',
    'maps_url': 'https://maps.app.goo.gl/hqrkXv3j3TMb9wRv6',
    'phone': '+92-91-6640558',
    'mobile': '+92-333-9297743',
    'email': 'admin@scms.edu.pk',
    'contact_email': 'contact@scms.edu.pk',
    'admissions_email': 'admissions@scms.edu.pk',
    'principal_email': 'principal@scms.edu.pk',
    'website': 'https://www.scms.edu.pk',
    'facebook_url': 'https://www.facebook.com/profile.php?id=61561925787504',
    'established': '2026',
    'affiliation': 'Khyber Medical University (KMU), Peshawar',
    'recognition': 'Pakistan Nursing Council (PNC) & Higher Education Commission (HEC)',
}

OWNER_INFO = {
    'name': 'Dr Siyyar Ahmad Safi',
    'designation': 'Owner & Founder',
    'qualification': 'MBBS, FCPS, MHPE',
    'specialty': 'ENT and Rhinoplasty Surgeon',
    'image': 'drsiyyar.jpeg',
}

# Programs Data
PROGRAMS = [
    {
        'id': 'bsn-generic',
        'title': 'BS Nursing (Generic)',
        'duration': '4 Years',
        'seats': 50,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'A comprehensive 4-year Bachelor of Science in Nursing program designed to produce competent, compassionate, and professional nurses equipped with modern healthcare knowledge and clinical skills.',
        'icon': 'fa-user-nurse',
        'color': 'primary'
    },
    {
        'id': 'bsn-post-rn',
        'title': 'BS Nursing (Post RN)',
        'duration': '2 Years',
        'seats': 30,
        'eligibility': 'Diploma in Nursing & Midwifery with valid PNC license',
        'affiliation': 'KMU Peshawar',
        'description': 'A 2-year post-registration program for registered nurses seeking to advance their education to the bachelors level, enhancing their clinical and leadership capabilities.',
        'icon': 'fa-stethoscope',
        'color': 'success'
    },
    {
        'id': 'bs-mlt',
        'title': 'BS Medical Laboratory Technology',
        'duration': '4 Years',
        'seats': 40,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'A 4-year degree program training students in diagnostic laboratory procedures, medical testing, and laboratory management for accurate disease diagnosis.',
        'icon': 'fa-microscope',
        'color': 'info'
    },
    {
        'id': 'bs-radiology',
        'title': 'BS Radiology & Imaging Technology',
        'duration': '4 Years',
        'seats': 30,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'Comprehensive training in medical imaging techniques including X-ray, CT scan, MRI, and ultrasound technology for modern diagnostic healthcare.',
        'icon': 'fa-x-ray',
        'color': 'warning'
    },
    {
        'id': 'bs-physiotherapy',
        'title': 'BS Physiotherapy',
        'duration': '4 Years (DPT Equivalent)',
        'seats': 30,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'A professional degree program focused on physical rehabilitation, therapeutic exercises, and manual therapy techniques to restore patient mobility and function.',
        'icon': 'fa-walking',
        'color': 'danger'
    },
    {
        'id': 'bs-pharmacy',
        'title': 'BS Pharmacy (Pharm-D)',
        'duration': '5 Years',
        'seats': 50,
        'eligibility': 'FSc Pre-Medical with at least 60% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'A 5-year Doctor of Pharmacy program preparing students for careers in pharmaceutical care, drug therapy management, and clinical pharmacy practice.',
        'icon': 'fa-pills',
        'color': 'primary'
    },
    {
        'id': 'bs-optometry',
        'title': 'BS Optometry & Vision Sciences',
        'duration': '4 Years',
        'seats': 25,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'Specialized training in eye care, vision testing, contact lens fitting, and management of visual disorders for comprehensive ophthalmic care.',
        'icon': 'fa-eye',
        'color': 'success'
    },
    {
        'id': 'bs-dental',
        'title': 'BS Dental Technology',
        'duration': '4 Years',
        'seats': 25,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'Training in dental laboratory technology, prosthodontics, and dental materials science for supporting modern dental healthcare services.',
        'icon': 'fa-tooth',
        'color': 'info'
    },
    {
        'id': 'bs-cardiac',
        'title': 'BS Cardiac Perfusion Technology',
        'duration': '4 Years',
        'seats': 20,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'Advanced training in cardiac perfusion, operating heart-lung machines during open-heart surgeries, and critical cardiac care support.',
        'icon': 'fa-heartbeat',
        'color': 'danger'
    },
    {
        'id': 'bs-dialysis',
        'title': 'BS Dialysis Technology',
        'duration': '4 Years',
        'seats': 20,
        'eligibility': 'FSc Pre-Medical with at least 50% marks',
        'affiliation': 'KMU Peshawar',
        'description': 'Specialized education in renal dialysis procedures, hemodialysis machine operation, and patient care for individuals with kidney disease.',
        'icon': 'fa-tint',
        'color': 'warning'
    }
]

@app.context_processor
def inject_programs():
    return {'programs': PROGRAMS, 'owner': OWNER_INFO}

# Faculty Data
FACULTY = [
    {
        'name': OWNER_INFO['name'],
        'designation': OWNER_INFO['designation'],
        'qualification': OWNER_INFO['qualification'],
        'experience': 'ENT and Rhinoplasty Surgeon',
        'department': 'Administration',
        'image': OWNER_INFO['image']
    }
]

# News/Announcements
NEWS = [
    {
        'title': 'Admissions Open Fall 2026',
        'date': '2026-05-20',
        'category': 'Admissions',
        'summary': 'Applications are now open for all BS programs for the Fall 2026 semester. Last date to apply: July 15, 2026.',
        'link': '#'
    },
    {
        'title': 'SCMS Signs MOU with KMU Peshawar',
        'date': '2026-04-15',
        'category': 'Academic',
        'summary': 'Safi College of Medical Sciences has officially signed an affiliation agreement with Khyber Medical University for all degree programs.',
        'link': '#'
    },
    {
        'title': 'New State-of-the-Art Simulation Lab Inaugurated',
        'date': '2026-03-10',
        'category': 'Facilities',
        'summary': 'A modern nursing simulation laboratory equipped with high-fidelity mannequins and virtual reality training systems has been inaugurated.',
        'link': '#'
    },
    {
        'title': 'Free Medical Camp at Mandani',
        'date': '2026-02-28',
        'category': 'Community',
        'summary': 'SCMS organized a free medical camp providing healthcare services to over 500 patients in Mandani and surrounding areas.',
        'link': '#'
    }
]

# Facilities
FACILITIES = [
    {
        'title': 'Modern Classrooms',
        'description': 'Spacious, air-conditioned classrooms equipped with multimedia projectors, smart boards, and high-speed internet connectivity.',
        'icon': 'fa-chalkboard-teacher'
    },
    {
        'title': 'Advanced Laboratories',
        'description': 'State-of-the-art labs for MLT, Radiology, Pharmacy, and Nursing with modern equipment and diagnostic tools.',
        'icon': 'fa-flask'
    },
    {
        'title': 'Simulation Center',
        'description': 'High-fidelity nursing simulation lab with patient mannequins, virtual reality training, and clinical skill stations.',
        'icon': 'fa-hospital'
    },
    {
        'title': 'Digital Library',
        'description': 'Comprehensive library with thousands of medical textbooks, journals, e-books, and online database access.',
        'icon': 'fa-book'
    },
    {
        'title': 'Clinical Training',
        'description': 'Affiliated with top hospitals in Peshawar and Charsadda for hands-on clinical training and internships.',
        'icon': 'fa-user-md'
    },
    {
        'title': 'Hostel Accommodation',
        'description': 'Separate, secure hostel facilities for male and female students with mess, Wi-Fi, and recreational areas.',
        'icon': 'fa-bed'
    },
    {
        'title': 'Sports Complex',
        'description': 'Indoor and outdoor sports facilities including cricket, football, badminton, and gymnasium.',
        'icon': 'fa-running'
    },
    {
        'title': 'Transport Service',
        'description': 'College buses covering major routes in Charsadda, Peshawar, and surrounding areas for student convenience.',
        'icon': 'fa-bus'
    }
]

@app.route('/')
def home():
    return render_template('index.html', college=COLLEGE_INFO, programs=PROGRAMS[:6], news=NEWS[:3], facilities=FACILITIES[:4])

@app.route('/about')
def about():
    return render_template('about.html', college=COLLEGE_INFO)

@app.route('/programs')
def programs():
    return render_template('programs.html', college=COLLEGE_INFO, programs=PROGRAMS)

@app.route('/program/<program_id>')
def program_detail(program_id):
    program = next((p for p in PROGRAMS if p['id'] == program_id), None)
    if not program:
        return redirect(url_for('programs'))
    return render_template('program_detail.html', college=COLLEGE_INFO, program=program)

@app.route('/faculty')
def faculty():
    return render_template('faculty.html', college=COLLEGE_INFO, faculty=FACULTY)

@app.route('/facilities')
def facilities():
    return render_template('facilities.html', college=COLLEGE_INFO, facilities=FACILITIES)

@app.route('/admissions')
def admissions():
    return render_template('admissions.html', college=COLLEGE_INFO, programs=PROGRAMS)

@app.route('/news')
def news():
    return render_template('news.html', college=COLLEGE_INFO, news=NEWS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        try:
            msg = Message(
                subject=f"Contact Form: {subject}",
                recipients=[COLLEGE_INFO['contact_email']],
                body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}",
                reply_to=email
            )
            mail.send(msg)
            flash('Thank you for contacting us! We will get back to you soon.', 'success')
        except Exception as e:
            flash('Message received. We will contact you shortly.', 'info')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html', college=COLLEGE_INFO)

@app.route('/downloads')
def downloads():
    return render_template('downloads.html', college=COLLEGE_INFO)

@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html', college=COLLEGE_INFO)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', college=COLLEGE_INFO)

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', college=COLLEGE_INFO), 404

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
