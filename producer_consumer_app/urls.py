from django.urls import path

from producer_consumer_app.views import (
    EmployeeCreateView,
    OrderListView,
    OrderDeleteView,
)

urlpatterns = [
    path("accounts/signup/", EmployeeCreateView.as_view(), name="signup"),
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
]

app_name = "producer_consumer_app"
