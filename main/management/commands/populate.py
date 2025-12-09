from django.core.management.base import BaseCommand
from main.models import Section, Content

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        # Create sections
        new_project = Section.objects.create(name='New Project', order=1)
        deployment = Section.objects.create(name='Deployment', order=2)
        redeployment = Section.objects.create(name='Redeployment', order=3)

        # New Project contents
        Content.objects.create(
            section=new_project,
            title='1. Create the Django Project',
            body=r'''
<ol>
<li>Open VS Code and open the terminal (View > Terminal).</li>
<li>Navigate to your desired directory:
<ul>
<li class="description">macOS/Linux:</li>
<pre><code>cd '/Users/davidhearl/Documents/08 - Programming/GitHub'</code></pre>
<li>Windows:</li>
<pre><code>cd "C:\Users\davidhearl\iCloudDrive\Documents\Programming\GitHub"</code></pre>
</ul>
</li>
<li>Create the project directory</li>
<pre><code>mkdir myproject</code></pre>
<pre><code>cd myproject</code></pre>
<li>Create a virtual environment:</li>
<pre><code>python -m venv virtual_environment</code></pre>
<li>Activate the virtual environment:</li>
<ul>
<li class="description">Windows:</li>
<pre><code>virtual_environment\Scripts\activate</code></pre>
<li class="description">macOS/Linux:</li>
<pre><code>source virtual_environment/bin/activate</code></pre>
</ul>
<li>Optional: Upgrade pip to the latest version to avoid warnings and improve package management:</li>
<pre><code>python -m pip install --upgrade pip</code></pre>
<li>Install Django and save requirements:</li>
<pre><code>pip install Django</code></pre>
<pre><code>pip freeze > requirements.txt</code></pre>
<li>Create a new Django project:</li>
<pre><code>django-admin startproject myproject .</code></pre>
<li>Migrate changes</li>
<pre><code>python3 manage.py migrate</code></pre>
<li>Optional: Open the project in Visual Studio Code:</li>
<pre><code>code .</code></pre>
<p class="description">Note: This requires the 'code' command to be installed in your PATH.</p>
<li>Navigate into your project:</li>
<pre><code>cd myproject</code></pre>
<li>Run the development server:</li>
<pre><code>python3 manage.py runserver</code></pre>
</ol>
''',
            order=1
        )

        Content.objects.create(
            section=new_project,
            title='2. Create a Django App',
            body='''
<ol>
<li>Create the app:</li>
<pre><code>python manage.py startapp myapp</code></pre>
<li>Open the <code>settings.py</code></li>
<li>Add <code>'myapp'</code> to <code>INSTALLED_APPS</code> in <code>settings.py</code>.</li>
<pre class="file-content">
<code>INSTALLED_APPS = [
    ...
    'myapp',
]</code></pre>
<li>Create a superuser:
<pre><code>python manage.py createsuperuser</code></pre>
</li>
</ol>
''',
            order=2
        )

        # Add more contents similarly for other parts.

        # For brevity, I'll add placeholders for others.

        Content.objects.create(
            section=new_project,
            title='3. Django Settings to Change',
            body=r'''
<p>Edit <code>myproject/settings.py</code>:</p>
<ul>
<li>Create a <code>.env</code> file in the project root using the terminal:</li>
<pre><code>touch .env</code></pre>
<pre><code>echo "SECRET_KEY=your-very-secret-key" >> .env</code></pre>
<li>Install python-dotenv to load environment variables:</li>
<pre><code>pip install python-dotenv</code></pre>
<pre><code>pip freeze > requirements.txt</code></pre>
<li>Turn off debug in production:</li>
<pre class="file-content"><code>DEBUG = False</code></pre>
<li>Set allowed hosts:</li>
<pre class="file-content"><code>ALLOWED_HOSTS = ['yourdomain.com', 'localhost']</code></pre>
<li>Adjust timezone and language:</li>
<pre class="file-content"><code>TIME_ZONE = 'Europe/Dublin'
LANGUAGE_CODE = 'en-us'</code></pre>
<li>Use environment variable for secret key:</li>
<pre class="file-content"><code>import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')</code></pre>
</ul>
''',
            order=3
        )
        Content.objects.create(
            section=new_project,
            title='4. Link the Project to GitHub',
            body=r'''
<ol>
<li>Initialize a Git repository:</li>
<pre><code>git init</code></pre>
<li>Create a <code>.gitignore</code> file in the project root and add:</li>
<pre><code>touch .gitignore</code></pre>
<li>Add items to the .gitignore files</li>
<pre class="file-content"><code>virtual_environment/
__pycache__/
*.pyc
*.sqlite3
.env
.code</code></pre>
<li>Install GitHub CLI</li>
<ul>
<li>macOS/linux</li>
<pre><code>brew install gh</code></pre>
<li>Windows:</li>
<pre><code>winget install --id GitHub.cli</code></pre>
</ul>
<li>Login to GitHub</li>
<pre><code>gh auth login</code></pre>
<li>Initialize Git and make the first commit:</li>
<pre><code>git add .</code></pre>
<pre><code>git commit -m "Initial commit"</code></pre>
<li>Create a new private or public repository on GitHub from the terminal:</li>
<pre><code>gh repo create your-repo-name --public --source=. --remote=origin --push</code></pre>
<p class="description">This creates the repo, links it, and pushes your code in one step.</p>
<li>Optional: Rename branch to main if needed:</li>
<pre><code>git branch -M main</code></pre>
<pre><code>git push -u origin main</code></pre>
</ol>
''',
            order=4
        )
        Content.objects.create(
            section=new_project,
            title='5. Setting up the MVT',
            body=r'''
<ol>
<li>Create the first view in <code>myapp/views.py</code>:</li>
<pre class="file-content"><code>from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')</code></pre>
<li>Create the app-specific <code>templates/myapp</code> directory and <code>home.html</code>:</li>
<pre><code>mkdir -p myapp/templates/myapp</code></pre>
<pre><code>touch myapp/templates/myapp/home.html</code></pre>
<li>Update <code>settings.py</code> to look for templates in the project root:</li>
<pre class="file-content"><code>TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]</code></pre>
<li>Create a static directory and a CSS file for styling:</li>
<pre><code>mkdir -p static/css</code></pre>
<pre><code>touch static/css/styles.css</code></pre>
<li>Make sure <code>settings.py</code> is configured to find static files:</li>
<pre class="file-content"><code>STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']</code></pre>
<li>Create <code>myapp/urls.py</code> and define the route:</li>
<pre><code>touch myapp/urls.py</code></pre>
<pre class="file-content"><code>from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]</code></pre>
<li>Include the app URLs in your project-level <code>urls.py</code>:</li>
<pre class="file-content"><code>from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]</code></pre>
</ol>
''',
            order=5
        )
        Content.objects.create(
            section=new_project,
            title='6. Common Django Commands',
            body=r'''
<pre><code>python manage.py runserver</code></pre>
<pre><code>python manage.py makemigrations</code></pre>
<pre><code>python manage.py migrate</code></pre>
<pre><code>python manage.py startapp appname</code></pre>
<pre><code>python manage.py createsuperuser</code></pre>
<pre><code>python manage.py shell</code></pre>
<pre><code>python manage.py collectstatic</code></pre>
<pre><code>python manage.py check</code></pre>
''',
            order=6
        )

        # Deployment
        Content.objects.create(
            section=deployment,
            title='Deploying a Django Application on Debian',
            body='''
<h3>1. System Update and Dependencies</h3>
<pre><code>sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git curl build-essential libpq-dev -y</code></pre>
<h3>2. Create a Dedicated User (Optional)</h3>
<pre><code>sudo adduser django
sudo usermod -aG sudo django
su - django</code></pre>
<h3>3. Clone Your Django Project</h3>
<pre><code>git clone https://github.com/yourusername/yourproject.git
cd yourproject</code></pre>
<h3>4. Set Up Python Virtual Environment</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt</code></pre>
<h3>5. Configure Django for Production</h3>
<ul>
<li>Set <code>DEBUG = False</code></li>
<li>Set <code>ALLOWED_HOSTS</code> to match your server</li>
<li>Use a secure <code>SECRET_KEY</code></li>
</ul>
<pre><code>python manage.py collectstatic
python manage.py migrate</code></pre>
<h3>6. Create Gunicorn Systemd Service</h3>
<pre><code>[Unit]
Description=gunicorn daemon for Django project
After=network.target
[Service]
User=django
Group=www-data
WorkingDirectory=/home/django/yourproject
ExecStart=/home/django/yourproject/venv/bin/gunicorn --workers 3 --bind unix:/home/django/yourproject/gunicorn.sock yourproject.wsgi:application
[Install]
WantedBy=multi-user.target</code></pre>
<pre><code>sudo systemctl start gunicorn
sudo systemctl enable gunicorn</code></pre>
<h3>7. Install and Configure Nginx</h3>
<pre><code>sudo apt install nginx -y</code></pre>
<pre><code>server {
    listen 80;
    server_name your.server.ip.or.domain;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/django/yourproject;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/django/yourproject/gunicorn.sock;
    }
}</code></pre>
<pre><code>sudo ln -s /etc/nginx/sites-available/yourproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx</code></pre>
<h3>8. Adjust Firewall (If Needed)</h3>
<pre><code>sudo ufw allow 'Nginx Full'</code></pre>
<h3>9. Set Up HTTPS with Certbot (Optional)</h3>
<pre><code>sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com</code></pre>
<h3>10. Final Checks</h3>
<ul>
<li>Visit your IP or domain</li>
<li>Ensure static files, admin panel, and views load</li>
<li>Check logs:
<pre><code>sudo journalctl -u gunicorn
sudo journalctl -xe</code></pre>
</li>
</ul>
''',
            order=1
        )

        # Redeployment
        Content.objects.create(
            section=redeployment,
            title='Redeployment Deployment',
            body=r'''
<h3>1.1 Firstly, check if the application has been deployed</h3>
<pre><code>sudo docker ps -a</code></pre>

<h3>1.2 Collect Static</h3>
<pre><code>sudo docker-compose run --rm web python manage.py collectstatic --noinput</code></pre>

<h3>1.3 If the application is not running</h3>
<pre><code>docker-compose build --no-cache</code></pre>

<h3>1.4 If the application is not running run it with</h3>
<pre><code>sudo docker-compose up -d</code></pre>

<h3>Troubleshooting</h3>
<ol>
<li><code>sudo docker-compose down</code></li>
<li>Go to 1.3</li>
</ol>
''',
            order=1
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))