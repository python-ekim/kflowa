from django.urls import path
from . import views

app_name = "accounts"  # optional but recommended for namespacing

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    # add more…
]
