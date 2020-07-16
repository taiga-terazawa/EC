from .forms import ItemForm, ChoiceForm, ItemStockForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, ItemStock
from django.contrib.auth.models import User


# Create your views here.

def tool_list(request):

  items = Item.objects.all()
  form = ItemForm()
  stock_form = ItemStockForm()
  return render(request, 'tool/tool_list.html', {'items': items, 'form': form, 'stock_form': stock_form})

# アイテム追加


def tool_create(request):
  if request.method == "POST":
    form = ItemForm(request.POST)
  # user_form = UserForm(request.POST)
  # フォームの値が正しいかチェック
    if form.is_valid():
      post = form.save(commit=False)
      post.image = request.FILES['image']
      post.published_date = timezone.now()
      post.status = request.POST.get('status')
      post.category = request.POST.get('category')
      post.save()

      stock = ItemStockForm()
      stock_post = stock.save(commit=False)
      stock_post.item_id = post.id
      stock_post.stock = request.POST.get('stock')
      stock_post.save()

      return redirect('tool_list')
  else:
    form = ItemForm()
    choice = ChoiceForm()
    stock_form = ItemStockForm()

  # if post.save():

    return render(request, 'tool/tool_create.html', {'form': form, 'choice': choice, 'stock_form': stock_form})

# 数量変更


def stock_edit(request, pk):
    # ここで特定のフィールドカラムのテーブル情報を取得している
  item_stock = get_object_or_404(ItemStock, item_id=pk)
  if request.method == 'POST':
    form = ItemStockForm(request.POST, instance=item_stock)
    if form.is_valid():

      post = form.save(commit=False)

      post.item_id = pk
      post.stock = request.POST.get('stock')
      post.published_date = timezone.now()
      post.save()

      return redirect('tool_list')

# status変更


def status_edit(request, pk):
  # item = get_object_or_404(Item, pk=pk)
  if request.method == 'POST':
    item_status = Item.objects.filter(pk=pk)
    for item in item_status:
      item.status = request.POST.get('status')
      item.save()
      return redirect('tool_list')


# delete


def item_remove(request, pk):
  if request.method == 'POST':
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('tool_list')


def user_list(request):
  users = User.objects.all()
  return render(request, 'tool/user_list.html', {'users': users})
