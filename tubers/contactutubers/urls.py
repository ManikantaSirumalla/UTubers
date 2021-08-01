from django.urls import path


from . import views

urlpatterns = [
        path('contactutubers', views.contactutubers, name="contactutubers"),

]
