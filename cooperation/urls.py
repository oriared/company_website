from django.urls import path

from .views import CooperationCreateView

app_name = 'cooperation'

urlpatterns = [
    path('distribution', CooperationCreateView.as_view(),
         {'type': 'distribution'}, name='distribution'),
    path('private_label', CooperationCreateView.as_view(),
         {'type': 'private_label'}, name='private_label'),
]
