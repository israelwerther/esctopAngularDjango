from credcoop.views import ClienteCreedcoopListView
from django.urls import path

app_name = 'credcoop'
urlpatterns = [
    path('list/', ClienteCreedcoopListView.as_view(), name="list"),
]
