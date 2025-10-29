from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faculty/', views.faculty_home),
    path('faculty/upload/', views.faculty_upload),
    path('faculty/search/', views.faculty_search),
    path('course/', views.course_home),
    path('course/search/', views.course_search),
    path('course/apply/', views.course_apply),
    path('course/delete/', views.course_delete),
    path('course/admin/', views.course_admin),
    path('course/admin/download/', views.course_admin_download),
]
