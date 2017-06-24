"""ch05www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from mysite import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^about/([0|1|2|3])/$', views.about),
    url(r'^list/(?P<list_date>\d{4}/\d{1,2}/\d{1,2})$', views.listing),
    url(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,3})$', views.post),
    url(r'^admin/', admin.site.urls),
]