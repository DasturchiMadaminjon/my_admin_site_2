from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Faculty
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('faculties/create/', views.faculty_create, name='faculty_create'),
    path('faculties/<int:pk>/update/', views.faculty_update, name='faculty_update'),
    path('faculties/<int:pk>/delete/', views.faculty_delete, name='faculty_delete'),

    # Kafedra
    path('kafedras/', views.kafedra_list, name='kafedra_list'),
    path('kafedras/create/', views.kafedra_create, name='kafedra_create'),
    path('kafedras/<int:pk>/update/', views.kafedra_update, name='kafedra_update'),
    path('kafedras/<int:pk>/delete/', views.kafedra_delete, name='kafedra_delete'),

    # Subject
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/update/', views.subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    
    # Group
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:pk>/update/', views.group_update, name='group_update'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),
    
    # Teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/update/', views.teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    
    # Student
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]