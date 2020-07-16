from django import forms
from .models import Item, ItemStock

# 定数化
STATUS_CHOICES = [
    (0, '非公開'),
    (1, '公開'),
]

CATEGORY_CHOICES = [
    ('食品', '食品'),
    ('ファッション', 'ファッション'),
    ('家具', '家具'),
    ('テクノロジー', 'テクノロジー'),
    ('贈り物', '贈り物'),
    ('その他', 'その他'),
]


class ItemForm(forms.ModelForm):

  class Meta:

    # Taskモデルを継承している
    model = Item
    # モデルのフィールドで使用するカラムを指定する
    # (このモデルは残りのカラムは自動生成するものだから書かない)
    fields = ('name', 'price', 'image')


class ChoiceForm(forms.Form):
  # class Meta:

  status = forms.MultipleChoiceField(
      label='ステータス',
      required=False,
      widget=forms.Select,
      choices=STATUS_CHOICES,
  )
  category = forms.MultipleChoiceField(
      label='カテゴリー',
      required=False,
      widget=forms.Select,
      choices=CATEGORY_CHOICES,
  )


class ItemStockForm(forms.ModelForm):
  class Meta:
    model = ItemStock
    # モデルのフィールドで使用するカラムを指定する
    # (このモデルは残りのカラムは自動生成するものだから書かない)
    fields = ('stock',)
