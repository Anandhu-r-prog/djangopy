from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import EventBooking, SignupData, UserMessage, UserSuggestion,BeachWeddingBooking


 
class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("password")
        cpw = cleaned_data.get("confirm_password")
        if pw != cpw:
            raise forms.ValidationError("Passwords do not match")
        
# class UserMessageForm(forms.Form):
#     full_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     phone = forms.CharField(max_length=15)
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

# from .models import UserMessage

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['name', 'email', 'message']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class BookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields =['name', 'email', 'event']

class UserSuggestionForm(forms.ModelForm):
    class Meta:
        model = UserSuggestion
        fields = ['full_name', 'phone_number', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your Full Name', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your Phone Number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your Email ID', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control', 'rows': 4}),
        }

class BeachWeddingForm(forms.ModelForm):
    class Meta:
        model = BeachWeddingBooking
        fields = '__all__'
