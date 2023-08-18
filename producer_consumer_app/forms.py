from django.contrib.auth.forms import UserCreationForm

from producer_consumer_app.models import Employee


class EmployeeCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "probation",
            "position",
        )
