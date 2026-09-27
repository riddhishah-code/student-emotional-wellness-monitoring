from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("questionnaire/", views.questionnaire, name="questionnaire"),
    path("result/<int:record_id>/", views.result, name="result"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
