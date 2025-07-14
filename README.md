# Real Estate Portal

A comprehensive real estate platform built with Django backend, jQuery/Dojo frontend, and PostgreSQL database.

## 🏠 Features

- **Property Listings**: Browse properties with images, detailed information, and map views
- **Booking System**: Schedule appointments with real estate agents
- **Agent Dashboard**: Manage properties, appointments, and client inquiries
- **Interactive Map**: View properties on an interactive map using Leaflet
- **REST API**: Full REST API for all functionality
- **Responsive Design**: Mobile-friendly interface using Bootstrap

## 🛠️ Technology Stack

- **Backend**: Django 4.2.11, Django REST Framework
- **Frontend**: jQuery, Dojo Toolkit, Bootstrap 5
- **Database**: SQLite (default), PostgreSQL (optional)
- **Maps**: Leaflet.js
- **Deployment**: Gunicorn, WhiteNoise, Docker

## Installation

### Prerequisites

- Python 3.9+
- PostgreSQL (optional, SQLite included by default)
- Node.js (for frontend dependencies - optional)

### Quick Setup (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd real_estate_portal
```

2. Run the setup script:
```bash
./setup.sh
```

3. Start the development server:
```bash
source venv/bin/activate
python manage.py runserver
```

## 🚀 Usage

### Accessing the Application

After starting the development server, you can access:

- **Main Application**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **API Documentation**: http://localhost:8000/api/

### Default Login Credentials

If you used the setup script, the following admin account is created:
- **Username**: admin
- **Password**: admin123
- **Email**: admin@example.com

### 📱 Using the Application

#### For Property Buyers/Renters:
1. **Browse Properties**: Visit the homepage to view all available properties
2. **Search & Filter**: Use the search bar and filters to find properties that match your criteria
3. **View Details**: Click on any property to see detailed information, images, and location
4. **Map View**: Use the map view to see properties in specific locations
5. **Book Viewing**: Schedule appointments with agents to view properties
6. **Contact Agents**: Send inquiries directly to property agents

#### For Real Estate Agents:
1. **Login**: Access the admin panel with your credentials
2. **Manage Properties**: Add, edit, or delete your property listings
3. **Handle Inquiries**: Respond to client inquiries and booking requests
4. **Track Appointments**: View and manage your scheduled property viewings
5. **Update Profile**: Keep your agent profile and contact information current

#### For Administrators:
1. **User Management**: Add and manage agent accounts
2. **Property Approval**: Review and approve property listings
3. **System Settings**: Configure application settings and features
4. **Reports**: View analytics and generate reports

### 🔧 Common Tasks

#### Adding a New Property
1. Login to the admin panel
2. Navigate to Properties > Add Property
3. Fill in property details (title, description, price, location, etc.)
4. Upload property images
5. Set property features and amenities
6. Publish the property

#### Managing Appointments
1. Go to Bookings > Appointments
2. View all scheduled appointments
3. Confirm or reschedule appointments
4. Add notes or follow-up actions

#### Responding to Inquiries
1. Navigate to Bookings > Inquiries
2. Read client inquiries
3. Respond directly through the system
4. Mark inquiries as resolved

### 📋 Key Features Explained

#### Property Search & Filtering
- **Location-based**: Search by city, state, or zip code
- **Price Range**: Filter properties within your budget
- **Property Type**: House, apartment, condo, commercial, etc.
- **Bedrooms/Bathrooms**: Filter by number of rooms
- **Amenities**: Pool, parking, gym, etc.

#### Interactive Map
- **Cluster View**: Properties are clustered for better performance
- **Custom Markers**: Different markers for different property types
- **Info Popups**: Click markers to see basic property information
- **Zoom Controls**: Navigate and zoom to specific areas

#### Booking System
- **Appointment Scheduling**: Choose date and time for property viewings
- **Email Notifications**: Automatic confirmations and reminders
- **Agent Coordination**: Direct communication with property agents
- **Inquiry Management**: Track all client inquiries in one place

### Manual Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Collect static files:
```bash
python manage.py collectstatic
```

6. Run the development server:
```bash
python manage.py runserver
```

### PostgreSQL Setup (Optional)

1. Install PostgreSQL and create database:
```sql
CREATE DATABASE real_estate_db;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE real_estate_db TO postgres;
```

2. Update `.env` file with database credentials:
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/real_estate_db
```

## API Endpoints

### Properties
- `GET /properties/api/properties/` - List all properties
- `GET /properties/api/properties/{id}/` - Get property details
- `POST /properties/api/properties/create/` - Create new property (authenticated)
- `PUT /properties/api/properties/{id}/update/` - Update property (owner only)
- `DELETE /properties/api/properties/{id}/delete/` - Delete property (owner only)

### Agents
- `GET /agents/api/agents/` - List all agents
- `GET /agents/api/agents/{id}/` - Get agent details
- `POST /agents/api/agents/reviews/` - Add agent review

### Bookings
- `GET /bookings/api/appointments/` - List appointments
- `POST /bookings/api/appointments/create/` - Create appointment
- `POST /bookings/api/inquiries/create/` - Create inquiry

## Deployment

### Using Maven

```bash
mvn clean package
```

### Using Ant

```bash
ant clean build package
```

### Using Docker

```bash
docker build -t real-estate-portal .
docker run -p 8000:8000 real-estate-portal
```

## Project Structure

```
real_estate_portal/
├── agents/                 # Agent management app
├── bookings/              # Booking and appointment app
├── properties/            # Property listing app
├── templates/             # HTML templates
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploaded files
├── real_estate_portal/   # Main project settings
├── requirements.txt      # Python dependencies
├── pom.xml              # Maven configuration
├── build.xml            # Ant configuration
├── Dockerfile           # Docker configuration
└── manage.py            # Django management script
```

## Features Overview

### Property Management
- Add, edit, and delete property listings
- Upload multiple images per property
- Set property features and amenities
- Geo-location support with map integration

### Booking System
- Schedule property viewings
- Agent appointment management
- Client inquiry handling
- Email notifications

### Agent Dashboard
- Manage property listings
- View and respond to inquiries
- Track appointments and bookings
- Performance analytics

### Map Integration
- Interactive property map
- Filter properties by location
- Clustering for better performance
- Custom markers and popups

## Configuration

### Database Configuration
Update `real_estate_portal/settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Email Configuration
For booking notifications, configure email settings in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

## 🔧 Troubleshooting

### Common Issues

#### TemplateDoesNotExist Error
If you encounter template errors, ensure all required templates are in place:
```bash
# Check if templates directory exists
ls -la templates/
# Templates should include:
# - base.html
# - home.html
# - properties/property_list.html
# - properties/property_map.html
# - properties/property_detail.html
# - agents/agent_list.html
# - agents/agent_detail.html
```

#### Database Migration Issues
```bash
# Reset migrations if needed
python manage.py migrate --fake-initial
# Or recreate migrations
rm -rf */migrations/
python manage.py makemigrations
python manage.py migrate
```

#### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --clear
# Check STATIC_URL and STATIC_ROOT in settings.py
```

#### Port Already in Use
```bash
# Use a different port
python manage.py runserver 8001
# Or kill processes using port 8000
lsof -ti:8000 | xargs kill -9
```

### Getting Help

1. **Check the console**: Look for error messages in the terminal
2. **Check browser console**: Open developer tools for JavaScript errors
3. **Review logs**: Check Django debug information
4. **Database issues**: Verify database connection and migrations
5. **Dependencies**: Ensure all packages are installed correctly

### Performance Tips

1. **Database Optimization**: Add indexes for frequently queried fields
2. **Image Optimization**: Compress property images before upload
3. **Caching**: Enable Django caching for better performance
4. **Static Files**: Use CDN for static files in production

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request
