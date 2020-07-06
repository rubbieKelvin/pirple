from django.urls import path

from .views import SignUpView, UserRecordView

app_name = "classroom"

urlpatterns = [
    path("accounts/signup/", SignUpView.as_view(), name="accounts-signup"),
    path("accounts/", UserRecordView.as_view(), "users")
]