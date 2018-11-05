from django import forms
from django.contrib.auth.models import User
from index.models import Member
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("name", "contact", "description", "location", "avatarImage")
        labels = {
            'avatarImage': _('Avatar Image'),
            'description': _('Self-description')
        }


    def clean(self):
        name = self.cleaned_data.get("name")
        contact = self.cleaned_data.get("contact")
        description = self.cleaned_data.get("description")
        avatarImage = self.cleaned_data.get("avatarImage")
        location = self.cleaned_data.get("location")

        errors = []
        if not name and not contact and not description and not avatarImage and not location:
            errors.append("Nothing is updated.")
        
        if (len(Member.objects.filter(name=name)) > 0):
            errors.append("This name is already used. Please input another one.")

        if errors:
            raise ValidationError(errors)

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("name", "description")
        labels = {
            'description': _('Self-description')
        }
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 3}),
        }

    def clean(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")

        errors = []
        if not name or not description:
            errors.append("All fields are required.")

        if (len(Member.objects.filter(name=name)) > 0):
            errors.append("This name is already used. Please input another one.")
            
        if errors:
            raise ValidationError(errors)