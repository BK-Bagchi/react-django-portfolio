from django.urls import path
from . import views

urlpatterns = [
    path('skilldetail/',  views.getSkillDetail),
    path('additionalskills/',  views.getAdditionalSkills),
    # path('add/', views.addItem)
]
