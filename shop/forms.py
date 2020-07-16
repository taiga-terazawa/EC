from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cart


class CartForm(forms.ModelForm):
  class Meta:
    model = Cart
    fields = ('amount',)


class AmountForm(forms.Form):
  amount = forms.IntegerField(label='', required=True)
# 新規ユーザー登録


class RegistrationForm(forms.Form):
  username = forms.CharField(label='ユーザー名')
  password = forms.CharField(widget=forms.PasswordInput(), label="パスワード")
  password2 = forms.CharField(widget=forms.PasswordInput(), label="パスワード再確認")
  email = forms.EmailField(label="メールアドレス")


class LoginForm(AuthenticationForm):
  """ログオンフォーム"""

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'
      field.widget.attrs['placeholder'] = field.label
