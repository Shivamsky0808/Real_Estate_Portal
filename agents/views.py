from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Agent, AgentReview
from .serializers import AgentSerializer, AgentListSerializer, AgentReviewSerializer


class AgentListView(generics.ListAPIView):
    """List all agents with filtering and search"""
    queryset = Agent.objects.filter(is_verified=True)
    serializer_class = AgentListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['agency_name', 'years_experience', 'specialization']
    search_fields = ['user__first_name', 'user__last_name', 'agency_name', 'specialization']
    ordering_fields = ['rating', 'years_experience', 'user__first_name']
    ordering = ['-rating']


class AgentDetailView(generics.RetrieveAPIView):
    """Retrieve a specific agent with all details"""
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [AllowAny]


class AgentReviewCreateView(generics.CreateAPIView):
    """Create a new agent review"""
    queryset = AgentReview.objects.all()
    serializer_class = AgentReviewSerializer
    permission_classes = [AllowAny]


def agent_list_view(request):
    """Render the agent listing page"""
    return render(request, 'agents/agent_list.html')


def agent_detail_view(request, agent_id):
    """Render the agent detail page"""
    return render(request, 'agents/agent_detail.html', {'agent_id': agent_id})


def agent_dashboard_view(request):
    """Render the agent dashboard page"""
    return render(request, 'agents/agent_dashboard.html')
