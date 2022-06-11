from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form



class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2',]
        labels = {
            'first_name':'الاسم الاول',
            'last_name':'الاسم الاخير',
            'username':'اسم المستخدم',
            'email':'البريد الالكتروني',
            'password1':'كلمة المرور',
            'password2':'تأكيد كلمة المرور',
        }

# class customUserCreationForm(UserCreationForm):
#     username = forms.CharField(label='اسم المستخدم',min_length=6,max_length=50,widget=forms.TextInput(attrs={'class':'form-control text-center'}))
#     email = forms.EmailField(label="البريد الالكتروني", widget=forms.TextInput(attrs={'class':'form-control text-center'}))
#     password1 = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput(attrs={"class":"form-control text-center"}))
#     password2 = forms.CharField(label="تأكيد كلمة المرور", widget=forms.PasswordInput(attrs={'class':'form-control text-center'}))

#     def username_clean(self):
#         username = self.cleaned_data['username'].lower()
#         new = User.objects.filter(username = username)
#         if new.count():
#             raise ValidationError("اسم المستخدم هذا موجود مسبقاً")
#         return username

#     def email_clean(self):
#         email = self.cleaned_data['email'].lower()
#         new = User.objects.filter(email = email)
#         if new.count():
#             raise ValidationError("هذا البريد تم استخدامه مسبقاً")
#         return email

#     def clean_password(self):
#         password1 = self.cleaned_data['password1']
#         password2 = self.cleaned_data['password2']
        
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("كلمة المرور ليست متطابقة")
#         return password2

#     def save(self, commit = True):
#         user = User.objects.create_user(
#             self.cleaned_data["username"],
#             self.cleaned_data["password"],
#             self.cleaned_data["email"],
#         )
#         return user

class LoginForm(forms.Form):
    usesrname = forms.CharField(max_length=50, label='اسم المستخدم', widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    password = forms.CharField(max_length=50, label="كلمة المرور", widget=forms.PasswordInput(attrs={'class':'form-control text-center'}))
    