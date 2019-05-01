from django.conf.urls import include, url
from django.contrib import admin
from home import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
