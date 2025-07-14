from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    # API endpoints
    path('api/properties/', views.PropertyListView.as_view(), name='property-list-api'),
    path('api/properties/<int:pk>/', views.PropertyDetailView.as_view(), name='property-detail-api'),
    path('api/properties/create/', views.PropertyCreateView.as_view(), name='property-create-api'),
    path('api/properties/<int:pk>/update/', views.PropertyUpdateView.as_view(), name='property-update-api'),
    path('api/properties/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property-delete-api'),
    path('api/my-properties/', views.AgentPropertiesView.as_view(), name='agent-properties-api'),
    
    # Web views
    path('', views.property_list_view, name='property-list'),
    path('property/<int:property_id>/', views.property_detail_view, name='property-detail'),
    path('map/', views.property_map_view, name='property-map'),
]
