
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, contact, welcome, about, signup, contact_success
from product.views import flan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('flan/<slug:slug>/', flan, name='flan'),
    path('contact/', contact, name='contact'),
    path('success/', contact_success, name='contact_success'),
    path('welcome/', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
