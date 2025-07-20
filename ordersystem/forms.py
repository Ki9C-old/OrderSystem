from django import forms
from .models import category
from .models import user
from .models import dish
from .models import order


class AddcategoryForm(forms.ModelForm):
    class Meta:
        model=category
        fields=['category_name']
        labels={'category_name':'カテゴリ'}
class AdddishForm(forms.ModelForm):
    class Meta:
        model=dish
        fields=['title','image','price','category','taxcategory','agelimit','soldout','delete']
        labels={'title':'品名','image':'写真','price':'値段','category':'カテゴリ','taxcategory':'税区分','agelimit':'年齢制限','soldout':'売り切れ','delete':'削除'}
class AdduserForm(forms.ModelForm):
    class Meta:
        model=user
        fields=['username','authcategory']
        labels={'username':'ユーザー名','authcategory':'権限'}
class AddorderForm(forms.ModelForm):
    class Meta:
        model=order
        fields=['user','dish','status']
        labels={'user':'テーブル名','dish':'品名','status':'状態'}

