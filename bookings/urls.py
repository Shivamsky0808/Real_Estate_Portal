from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    # API endpoints
    path('api/appointments/', views.AppointmentListView.as_view(), name='appointment-list-api'),
    path('api/appointments/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail-api'),
    path('api/appointments/create/', views.AppointmentCreateView.as_view(), name='appointment-create-api'),
    path('api/appointments/<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment-update-api'),
    path('api/inquiries/', views.InquiryListView.as_view(), name='inquiry-list-api'),
    path('api/inquiries/create/', views.InquiryCreateView.as_view(), name='inquiry-create-api'),
    
    # Web views
    path('appointments/', views.appointment_list_view, name='appointment-list'),
    path('book/<int:property_id>/', views.book_appointment_view, name='book-appointment'),
    path('inquire/<int:property_id>/', views.inquiry_create_view, name='inquiry-create'),
]
