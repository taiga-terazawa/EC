"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

# login機能よびだし
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm


urlpatterns = [
    path('admin/', admin.site.urls),
    # ここに表示させたいテンプレート書く
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('shop.urls')),
    path('tool/', include('tool.urls'))
]

if settings.DEBUG:
  import debug_toolbar
  # import debug_toolbar
  urlpatterns.append(path("", include(debug_toolbar.urls)))

  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#   urlpatterns += static(settings.IMAGE_URL,
#                         document_root=settings.IMAGE_ROOT)
