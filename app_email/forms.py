from django import forms
from app_email.models import Email
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Отправить', css_class="btn-success"))
