"""
URL configuration for BookMaintenanceSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
import accounts.views as aviews
import books.views as bviews
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", aviews.sign_in, name='login'),
    path("log_out/", aviews.log_out, name='log_out'),
    path("register/", aviews.register, name='register'),
    path("", bviews.book, name='Book'),
    path("book/", bviews.book, name='Book'),
    path("book/create/", bviews.book_create, name='BookCreate'),
    path("book/edit/<int:book_id>/", bviews.book_edit, name='BookEdit'),
    path("book/details/<int:book_id>/", bviews.book_details, name='BookDetails'),
    path("book/lendrec/<int:book_id>/", bviews.book_lendrec, name='BookLendRec'),
    path("book/delete/<int:book_id>", bviews.book_delete, name='Delete'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
