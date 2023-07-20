from django import forms
from django.contrib.auth.forms import (AuthenticationForm as AuthenticationFormGeneric,
                                       UserCreationForm as UserCreationFormGeneric,
                                       )

class AuthenticationForm(AuthenticationFormGeneric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
            # if isinstance(field, forms.CharField):
            #     print(field.label, type(field.lable))
            #


class UserCreationForm(UserCreationFormGeneric):
    class Meta(UserCreationFormGeneric.Meta):
        fields = "username", "email",
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field)
            field: forms.Field
            widget: forms.Widget = field.widget
            widget.attrs["class"] = "form-control"
