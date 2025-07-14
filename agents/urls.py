from django.urls import path
from . import views

app_name = 'agents'

urlpatterns = [
    # API endpoints
    path('api/agents/', views.AgentListView.as_view(), name='agent-list-api'),
    path('api/agents/<int:pk>/', views.AgentDetailView.as_view(), name='agent-detail-api'),
    path('api/agents/reviews/', views.AgentReviewCreateView.as_view(), name='agent-review-create-api'),
    
    # Web views
    path('', views.agent_list_view, name='agent-list'),
    path('agent/<int:agent_id>/', views.agent_detail_view, name='agent-detail'),
    path('dashboard/', views.agent_dashboard_view, name='agent-dashboard'),
]
