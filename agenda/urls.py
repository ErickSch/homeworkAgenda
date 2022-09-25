from django.urls import path

from . import views

urlpatterns = [
    path("", views.agenda, name="agenda"),
    path("edit_homework/<str:primary_key>/", views.edit_homework, name="edit_homework"),
    path("create_subject/", views.create_subject, name="create_subject"),
    

]