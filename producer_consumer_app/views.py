from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from producer_consumer_app.forms import EmployeeCreateForm
from producer_consumer_app.models import Employee, Order


class EmployeeCreateView(generic.CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Order.objects.all()

        return Order.objects.filter(employee=user)


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("producer_consumer_app:order-list")
