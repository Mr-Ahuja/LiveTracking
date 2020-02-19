from django.conf.urls import url
from . import views
from .views import LogsView

urlpatterns = [
    url('logs',LogsView.as_view()),
    url(r'^user/(?P<id>\w{0,50})',views.activateTrackers),
]