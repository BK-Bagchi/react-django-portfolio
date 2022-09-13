from django.urls import path
from . import views

urlpatterns = [
    path('skilldetail/',  views.getSkillDetail),
    path('additionalskills/',  views.getAdditionalSkills),
    path('experience/', views.getExperience),
    path('workdetails/', views.getWorkDetails),
    # path('add/', views.addItem)
]
