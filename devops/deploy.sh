#!/bin/bash

# Exit immediately if a command fails
set -e

echo "Starting backend deployment..."

# Navigate to the backend directory
cd /home/ubuntu/drf-boilerplate

echo "Pulling latest changes from the repository..."
git pull origin main

echo "Activating the virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements/production.txt

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Restarting backend services..."
sudo systemctl restart drf-boilerplate
sudo systemctl restart nginx

echo "Restarting RQ worker services..."
sudo systemctl restart rqworker1 rqworker2 rqworker3 rqworker4 rqscheduler

echo "Backend deployment successful!"
