#!/bin/bash

# Real Estate Portal Setup Script
echo "🏠 Setting up Real Estate Portal..."

# Remove corrupted virtual environment
if [ -d "venv" ]; then
    echo "Removing corrupted virtual environment..."
    rm -rf venv
fi

# Create new virtual environment
echo "Creating new virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
echo "Creating superuser (optional)..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')" | python manage.py shell

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create media directory
mkdir -p media/property_images
mkdir -p media/agent_profiles

echo "✅ Setup completed successfully!"
echo ""
echo "To run the development server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Admin credentials:"
echo "  Username: admin"
echo "  Password: admin123"
echo "  URL: http://localhost:8000/admin/"
echo ""
echo "Application URL: http://localhost:8000/"
