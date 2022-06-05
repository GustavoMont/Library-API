"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from books.api.viewsets import BooksViewSets
from users.api.viewsets import UsersViewSets
from loans.api.viewsets import LoansViewSet

routes = routers.DefaultRouter()

routes.register(r'books', BooksViewSets, basename="Books")
routes.register(r'users', UsersViewSets, basename="Users")
routes.register(r'loans', LoansViewSet, basename='Loans')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routes.urls))
]
