from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.', widget= forms.TextInput (attrs={'placeholder':'Email', 'class':'form-control'}))
    username = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', widget= forms.TextInput (attrs={'placeholder':'Username', 'class':'form-control'}))
    first_name= forms.CharField(max_length=100, widget= forms.TextInput (attrs={'placeholder':'Enter your first name', 'class':'form-control'}))
    last_name= forms.CharField(max_length=100, widget= forms.TextInput (attrs={'placeholder':'Enter your last name', 'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control py-2'}))
    password2 = forms.CharField(label='Password confirmation', widget= forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form-control py-2'}))


    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AccountAuthenticationForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.TextInput (attrs={'placeholder':'Email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput (attrs={'placeholder':'Password'}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')
    
    def __init__(self, *args, **kwargs):
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', )

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)
            