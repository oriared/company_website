from django.urls import path

from .views import CooperationCreateView

app_name = 'cooperation'

urlpatterns = [
    path('<str:type>', CooperationCreateView.as_view(), name='cooperation'),
]
