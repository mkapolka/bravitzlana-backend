"""bravitzlana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bravitzlana import views

UUID_REGEX = '[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}'

urlpatterns = [
    url(r'^/?$', views.main),
    url(r'^admin/', admin.site.urls),
    url(r'^(?i)new(?:/(%s))?/?' % UUID_REGEX, views.new, name='new'),
    url(r'^(?i)play/(%s)/?' % UUID_REGEX, views.play, name='play'),
    # url(r'^save/<game_id>/', None),
    url(r'(?i)^data/(%s).json$' % UUID_REGEX, views.save_data),
    url(r'^upload/?', views.upload),
    url(r'^games/?', views.games),
]
