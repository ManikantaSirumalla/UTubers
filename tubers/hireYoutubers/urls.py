from django.urls import path


from . import views

urlpatterns = [
    path('hireYoutubers', views.hireYoutubers, name="hireYoutubers"),
]
