from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from properties.models import Property, PropertyImage, PropertyFeature
from agents.models import Agent, AgentReview
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample users and agents
        agents_data = [
            {
                'username': 'rajesh_sharma',
                'first_name': 'Rajesh',
                'last_name': 'Sharma',
                'email': 'rajesh.sharma@realestate.in',
                'agency_name': 'Prime Properties Mumbai',
                'phone': '+919876543210',
                'license': 'RERA001MH',
                'years_experience': 8,
                'specialization': 'residential',
                'bio': 'Experienced residential real estate agent serving Mumbai and Navi Mumbai with 8+ years in the industry.'
            },
            {
                'username': 'priya_singh',
                'first_name': 'Priya',
                'last_name': 'Singh',
                'email': 'priya.singh@luxuryhomes.in',
                'agency_name': 'Elite Homes Delhi',
                'phone': '+919876543211',
                'license': 'RERA002DL',
                'years_experience': 10,
                'specialization': 'luxury',
                'bio': 'Luxury real estate specialist with expertise in premium properties across Delhi NCR.'
            },
            {
                'username': 'arjun_patel',
                'first_name': 'Arjun',
                'last_name': 'Patel',
                'email': 'arjun.patel@commercialspaces.in',
                'agency_name': 'Commercial Hub Bangalore',
                'phone': '+919876543212',
                'license': 'RERA003KA',
                'years_experience': 12,
                'specialization': 'commercial',
                'bio': 'Commercial real estate expert specializing in IT parks and office spaces in Bangalore.'
            }
        ]
        
        agents = []
        for agent_data in agents_data:
            user, created = User.objects.get_or_create(
                username=agent_data['username'],
                defaults={
                    'first_name': agent_data['first_name'],
                    'last_name': agent_data['last_name'],
                    'email': agent_data['email'],
                    'is_staff': True
                }
            )
            if created:
                user.set_password('password123')
                user.save()
            
            agent, created = Agent.objects.get_or_create(
                user=user,
                defaults={
                    'phone_number': agent_data['phone'],
                    'license_number': agent_data['license'],
                    'agency_name': agent_data['agency_name'],
                    'bio': agent_data['bio'],
                    'years_experience': agent_data['years_experience'],
                    'specialization': agent_data['specialization'],
                    'is_verified': True,
                    'rating': Decimal(str(random.uniform(3.5, 5.0)))
                }
            )
            agents.append(agent)
        
        # Create sample properties
        properties_data = [
            {
                'title': 'Luxury 4BHK Villa in Bandra',
                'description': 'Stunning 4-bedroom villa with modern amenities, parking, and terrace garden in prime Bandra location.',
                'property_type': 'house',
                'listing_type': 'sale',
                'price': Decimal('35000000'),  # 3.5 Crore INR
                'bedrooms': 4,
                'bathrooms': Decimal('3.5'),
                'area': Decimal('2800'),
                'address': 'Carter Road, Bandra West',
                'city': 'Mumbai',
                'state': 'Maharashtra',
                'zip_code': '400050',
                'latitude': Decimal('19.0596'),
                'longitude': Decimal('72.8295'),
            },
            {
                'title': 'Premium 3BHK Apartment in Gurgaon',
                'description': 'Modern luxury apartment in DLF Phase 2 with city views, club facilities, and 24/7 security.',
                'property_type': 'apartment',
                'listing_type': 'rent',
                'price': Decimal('85000'),  # 85k INR per month
                'bedrooms': 3,
                'bathrooms': Decimal('2.0'),
                'area': Decimal('1650'),
                'address': 'DLF Phase 2, Sector 25',
                'city': 'Gurgaon',
                'state': 'Haryana',
                'zip_code': '122002',
                'latitude': Decimal('28.4595'),
                'longitude': Decimal('77.0266'),
            },
            {
                'title': 'Cozy 2BHK in Koramangala',
                'description': 'Well-maintained 2BHK apartment in IT hub Koramangala with modern amenities.',
                'property_type': 'apartment',
                'listing_type': 'sale',
                'price': Decimal('12500000'),  # 1.25 Crore INR
                'bedrooms': 2,
                'bathrooms': Decimal('2.0'),
                'area': Decimal('1200'),
                'address': '5th Block, Koramangala',
                'city': 'Bangalore',
                'state': 'Karnataka',
                'zip_code': '560095',
                'latitude': Decimal('12.9352'),
                'longitude': Decimal('77.6245'),
            },
            {
                'title': 'Spacious 3BHK Independent House',
                'description': 'Three-story independent house with parking, garden, and terrace in peaceful locality.',
                'property_type': 'house',
                'listing_type': 'rent',
                'price': Decimal('45000'),  # 45k INR per month
                'bedrooms': 3,
                'bathrooms': Decimal('2.5'),
                'area': Decimal('1800'),
                'address': 'Sector 40, Noida',
                'city': 'Noida',
                'state': 'Uttar Pradesh',
                'zip_code': '201303',
                'latitude': Decimal('28.5706'),
                'longitude': Decimal('77.3272'),
            },
            {
                'title': 'Modern IT Office Space in Hitech City',
                'description': 'Prime commercial space perfect for IT companies with modern infrastructure and ample parking.',
                'property_type': 'commercial',
                'listing_type': 'rent',
                'price': Decimal('250000'),  # 2.5 Lakh INR per month
                'bedrooms': 0,
                'bathrooms': Decimal('4.0'),
                'area': Decimal('3500'),
                'address': 'HITEC City, Madhapur',
                'city': 'Hyderabad',
                'state': 'Telangana',
                'zip_code': '500081',
                'latitude': Decimal('17.4485'),
                'longitude': Decimal('78.3908'),
            },
            {
                'title': 'Affordable 2BHK Starter Home',
                'description': 'Perfect starter home with vastu compliance, modular kitchen, and good connectivity.',
                'property_type': 'apartment',
                'listing_type': 'sale',
                'price': Decimal('4500000'),  # 45 Lakh INR
                'bedrooms': 2,
                'bathrooms': Decimal('2.0'),
                'area': Decimal('950'),
                'address': 'Wakad, Hinjewadi Road',
                'city': 'Pune',
                'state': 'Maharashtra',
                'zip_code': '411057',
                'latitude': Decimal('18.5974'),
                'longitude': Decimal('73.7898'),
            }
        ]
        
        for i, prop_data in enumerate(properties_data):
            agent = agents[i % len(agents)]
            
            property_obj, created = Property.objects.get_or_create(
                title=prop_data['title'],
                defaults={
                    **prop_data,
                    'agent': agent.user,
                    'status': 'active'
                }
            )
            
            if created:
                # Add sample features
                features = [
                    ('Parking', 'Covered'),
                    ('Power Backup', 'Generator'),
                    ('Air Conditioning', 'Split AC'),
                    ('Flooring', 'Vitrified Tiles'),
                    ('Kitchen', 'Modular'),
                    ('Water Supply', '24x7'),
                    ('Security', '24x7 Guards'),
                    ('Lift', 'High Speed'),
                    ('Vastu Compliant', 'Yes'),
                    ('Swimming Pool', 'Community'),
                    ('Gym', 'Equipped'),
                    ('Children Play Area', 'Available'),
                ]
                
                for feature_name, feature_value in random.sample(features, 3):
                    PropertyFeature.objects.create(
                        property=property_obj,
                        feature_name=feature_name,
                        feature_value=feature_value
                    )
        
        # Add sample reviews for agents
        for agent in agents:
            for i in range(3):
                AgentReview.objects.get_or_create(
                    agent=agent,
                    reviewer_name=f'Client {i+1}',
                    reviewer_email=f'client{i+1}@example.com',
                    rating=random.randint(4, 5),
                    comment=f'Great service from {agent.user.first_name}! Very professional and helpful.'
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(agents)} agents and {len(properties_data)} properties')
        )
