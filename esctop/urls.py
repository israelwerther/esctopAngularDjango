from esctop.views import ClienteEsctopListView
from django.urls import path

app_name = 'esctop'
urlpatterns = [
    path('list/', ClienteEsctopListView.as_view(), name="list"),
]
