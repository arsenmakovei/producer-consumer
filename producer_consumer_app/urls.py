from django.urls import path

from producer_consumer_app.views import (
    EmployeeCreateView,
    OrderListView,
    OrderDeleteView,
    OrderDetailView,
    EmployeeDetailView,
)

urlpatterns = [
    path("accounts/signup/", EmployeeCreateView.as_view(), name="signup"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
]

app_name = "producer_consumer_app"
