Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo apt update && \
    sudo apt install nginx git python3 python3-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/superlists.spencerogden.com/g" \
    | sudo tee /etc/nginx/sites-available/superlists.spencerogden.com

sudo ln -s /etc/nginx/sites-available/superlists.spencerogden.com \
    /etc/nginx/sites-enabled/superlists.spencerogden.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

cat ./deploy_tools/gunicorn-systemd.template.service \
    | sed "s/DOMAIN/superlists.spencerogden.com/g" \
    | sudo tee /etc/systemd/system/gunicorn-superlists.spencerogden.com.service
    
Restart services
sudo systemctl daemon-reload && \
    sudo systemctl reload nginx && \
    sudo systemctl enable gunicorn-superlists.spencerogden.com && \
    sudo systemctl start  gunicorn-superlists.spencerogden.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc