#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies and build Tailwind CSS
if [ -f "package.json" ]; then
    npm ci
    npm run build
fi

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate