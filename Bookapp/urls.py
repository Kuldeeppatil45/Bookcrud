from django.urls import path
from Bookapp import views

urlpatterns = [
    path('home',views.homepage),
    path('register',views.addbook),
    path('delete/<bookid>',views.deleteBook),
    path('update/<bookid>',views.updateBook),
]
