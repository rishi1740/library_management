from django.http import HttpResponse
from django.urls import path
from .views import (
    AdminRegistrationView, 
    AdminLoginView,
    BookListCreateView,
    BookDetailView,
    StudentBookListView,
    student_frontend_view,
)

urlpatterns = [
    # Admin Authentication
    path('admin/register/', AdminRegistrationView.as_view(), name='admin-register'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    
    # Admin Book Operations
    path('admin/books/', BookListCreateView.as_view(), name='admin-book-list'),
    path('admin/books/<int:pk>/', BookDetailView.as_view(), name='admin-book-detail'),
    
    # Student View
    path('books/', StudentBookListView.as_view(), name='student-book-list'),
    path('', student_frontend_view, name='student-frontend'),
]

#testing 
""" def test_view(request):
    return HttpResponse("Hello, Django!")

urlpatterns += [
    path('test/', test_view, name='test'),
] """