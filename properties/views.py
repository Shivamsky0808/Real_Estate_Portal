from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Property, PropertyImage, PropertyFeature
from .serializers import PropertySerializer, PropertyListSerializer


class PropertyListView(generics.ListAPIView):
    """List all properties with filtering and search"""
    queryset = Property.objects.filter(status='active')
    serializer_class = PropertyListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['property_type', 'listing_type', 'city', 'state', 'bedrooms', 'bathrooms']
    search_fields = ['title', 'description', 'address', 'city', 'state']
    ordering_fields = ['price', 'created_at', 'bedrooms', 'bathrooms', 'area']
    ordering = ['-created_at']


class PropertyDetailView(generics.RetrieveAPIView):
    """Retrieve a specific property with all details"""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]


class PropertyCreateView(generics.CreateAPIView):
    """Create a new property (authenticated agents only)"""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)


class PropertyUpdateView(generics.UpdateAPIView):
    """Update an existing property (property owner only)"""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Property.objects.filter(agent=self.request.user)


class PropertyDeleteView(generics.DestroyAPIView):
    """Delete a property (property owner only)"""
    queryset = Property.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Property.objects.filter(agent=self.request.user)


class AgentPropertiesView(generics.ListAPIView):
    """List all properties for the authenticated agent"""
    serializer_class = PropertyListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Property.objects.filter(agent=self.request.user)


def property_list_view(request):
    """Render the property listing page"""
    return render(request, 'properties/property_list.html')


def property_detail_view(request, property_id):
    """Render the property detail page"""
    return render(request, 'properties/property_detail.html', {'property_id': property_id})


def property_map_view(request):
    """Render the property map view"""
    return render(request, 'properties/property_map.html')
