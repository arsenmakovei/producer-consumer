import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from producer_consumer_app.forms import EmployeeCreateForm
from producer_consumer_app.models import Employee, Order
from producer_consumer_app.notification_service import send_telegram_message


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
            return Order.objects.select_related("employee")

        return Order.objects.filter(employee=user).select_related("employee")


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("producer_consumer_app:order-list")

    def form_valid(self, form):
        order = self.get_object()
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = super().form_valid(form)

        if isinstance(response, HttpResponseRedirect) and response.status_code == 302:
            message = (
                f"Задача №{order.pk}-{order.task_id} під назвою {order.name} "
                f"була опрацьована {order.employee.first_name} {order.employee.position} "
                f"у {current_datetime}"
            )
            send_telegram_message(message)

        return response
