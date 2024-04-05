from django.urls import path
from .views import AnnualData

urlpatterns = [path("data/", AnnualData.as_view())]
