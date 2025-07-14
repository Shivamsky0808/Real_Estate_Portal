from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment, Inquiry
from .serializers import AppointmentSerializer, AppointmentCreateSerializer, InquirySerializer, InquiryCreateSerializer


class AppointmentListView(generics.ListAPIView):
    """List appointments with filtering"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['appointment_type', 'status', 'scheduled_date']
    search_fields = ['client_name', 'client_email', 'property__title']
    ordering_fields = ['scheduled_date', 'scheduled_time', 'created_at']
    ordering = ['scheduled_date', 'scheduled_time']


class AppointmentDetailView(generics.RetrieveAPIView):
    """Retrieve a specific appointment"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]


class AppointmentCreateView(generics.CreateAPIView):
    """Create a new appointment"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    permission_classes = [AllowAny]


class AppointmentUpdateView(generics.UpdateAPIView):
    """Update an appointment (for agents)"""
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class InquiryListView(generics.ListAPIView):
    """List inquiries with filtering"""
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['inquiry_type', 'is_responded']
    search_fields = ['name', 'email', 'property__title']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class InquiryCreateView(generics.CreateAPIView):
    """Create a new inquiry"""
    queryset = Inquiry.objects.all()
    serializer_class = InquiryCreateSerializer
    permission_classes = [AllowAny]


def appointment_list_view(request):
    """Render the appointment listing page"""
    return render(request, 'bookings/appointment_list.html')


def book_appointment_view(request, property_id):
    """Render the book appointment page"""
    return render(request, 'bookings/book_appointment.html', {'property_id': property_id})


def inquiry_create_view(request, property_id):
    """Render the inquiry creation page"""
    return render(request, 'bookings/inquiry_create.html', {'property_id': property_id})
