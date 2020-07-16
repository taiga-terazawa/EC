from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from tool.models import Item, ItemStock
from .forms import CartForm, AmountForm
from .page.paginate import *
from .page.digit import *
from .models import Cart
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth import login, authenticate
# ログインパスを通す場合に必要
from django.contrib.auth.decorators import login_required
# ログアウトさせる為に必要
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView, )
from .forms import RegistrationForm, LoginForm
# キーワード検索
from django.db.models import Q
from django.contrib import messages

# フィールドを更新させる処理
from django.db.models import F
# Create your views here.


def item_list(request):
  items = Item.objects.filter(status=1)
  keyword = request.GET.get('keyword')
  category = request.GET.get('category')

  if keyword:
    items = items.filter(

        # ここでキーワードにtitleかcontentのカラムに部分一致したデータを取得
        Q(name__icontains=keyword) | Q(price__icontains=keyword)
    )
    messages.success(request, '「{}」の検索結果'.format(keyword))

  if category:
    items = items.filter(category=category)
  items = paginate_query(request, items, settings.PAGE_PER_ITEM)

  return render(request, 'shop/item_list.html', {'items': items})


@login_required
def cart_plus(request, pk):
  # ここでuser_idとitem_idで一致するものを取得
  item_cart = Cart.objects.filter(item_id=pk, user_id=request.user.id)

  # if notでもし上で取得ができなかったら追加処理をする
  if not item_cart:
    Cart.objects.create(
        amount=1,
        published_date=timezone.now(),
        item_id=pk,
        user_id=request.user.id
    )
    return redirect('cart_list')

  # 取得できていたらamountフィールドのみ+1して更新する
  else:
    item_cart.update(amount=F('amount') + 1)
    return redirect('cart_list')


@login_required
def cart_list(request):
  items = Cart.objects.filter(user_id=request.user.id)
  sum_price = 0
  for item in items:
    sum_price += item.item.price * item.amount

    form = AmountForm()
  return render(request, 'shop/cart_list.html', {'items': items, 'sum_price': sum_price, 'form': form})


@login_required
def finish_list(request):
  items = Cart.objects.filter(user_id=request.user.id)
  sum_price = 0
  for item in items:
    item_stocks = ItemStock.objects.filter(item_id=item.item.id)
    item_stocks.update(stock=F('stock') - item.amount)
    sum_price += item.item.price * item.amount
  Cart.objects.filter(user_id=request.user.id).delete()
  return render(request, 'shop/finish_list.html', {'items': items, 'sum_price': sum_price})


def amount_edit(request, pk):
  cart = get_object_or_404(Cart, pk=pk)
  if request.method == 'POST':
    form = CartForm(request.POST, instance=cart)
    if form.is_valid():
      post = form.save(commit=False)
      post.amount = request.POST.get('amount')
      post.published_date = timezone.now()
      post.save()
      return redirect('cart_list')


def cart_remove(request, pk):
  if request.method == 'POST':
    Cart.objects.filter(id=pk).delete()
    return redirect('cart_list')

# ログイン、ログアウト追加


class Login(LoginView):
  """ログインページ"""
  form_class = LoginForm
  template_name = 'registration/login.html'


class Logout(LoginRequiredMixin, LogoutView):
  """ログアウトページ"""
  template_name = 'registration/login.html'
# ここまで追加

# 新規登録


def registration_user(request):
  if request.method == 'POST':
    registration_form = RegistrationForm(request.POST)
    password = request.POST['password']
    password2 = request.POST['password2']

    if len(password) < 8:
      registration_form.add_error('password', "文字数は８文字未満です")
      return render(request, 'registration/registration.html', {'registration_form': registration_form})

    if not has_digit(password):
      registration_form.add_error('password', "アルファベット、数字が含まれていません")
      return render(request, 'registration/registration.html', {'registration_form': registration_form})

    if len(password2) < 8:
      registration_form.add_error('password', "文字数は８文字未満です")
      return render(request, 'registration/registration.html', {'registration_form': registration_form})

    if not has_digit(password2):
      registration_form.add_error('password', "アルファベット、数字が含まれていません")
      return render(request, 'registration/registration.html', {'registration_form': registration_form})

    if registration_form.has_error('password'):
      return render(request, 'registration.html', {'registration_form': registration_form})
    user = User.objects.create_user(
        username=request.POST['username'], password=password, email=request.POST['email'])
    return render(request, 'registration/login.html')
  else:
    registration_form = RegistrationForm()
  return render(request, 'registration/registration.html', {'registration_form': registration_form})
