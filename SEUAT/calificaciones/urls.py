from django.conf.urls import url
from .views import AdminView


urlpatterns = [
    url(r'^home/$', AdminView.as_view(), name='home'),
]
