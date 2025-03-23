from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import Book
from .serializers import AdminRegistrationSerializer, AdminLoginSerializer, BookSerializer
from django.shortcuts import render

# Admin Registration View
class AdminRegistrationView(generics.CreateAPIView):
    serializer_class = AdminRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,
            'name': user.name
        }, status=status.HTTP_201_CREATED)

# Admin Login View
class AdminLoginView(APIView):
    serializer_class = AdminLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,
            'name': user.name
        })

# Book List Create View (for Admin)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Book Detail View (for Admin) - Retrieve, Update, Delete
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Student Book List View (No authentication required)
class StudentBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def student_frontend_view(request):
    return render(request, 'index.html')