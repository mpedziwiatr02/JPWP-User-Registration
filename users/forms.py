from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label='Nazwa użytkownika')
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='Hasło')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
