from django.db import models
from PIL import Image
from django.utils import timezone
#おすすめメニュー　まだ考え中
#画像だけ表示させておいて、タッチしたらおすすめメニュー一覧を表示する感じにしようかな

#メニュー一覧　タイトル/インデックス/画像/値段/カテゴリー（肉料理とか魚料理とか）)

class dish(models.Model):
    dish_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=80)
    image=models.ImageField(blank=True,null=True,upload_to="templates")
    price=models.IntegerField()
    category=models.ForeignKey("category",on_delete=models.PROTECT)
    taxcategory=models.ForeignKey("taxcategory",on_delete=models.PROTECT)
    agelimit=models.BooleanField(default=False)
    soldout=models.BooleanField(default=False)
    delete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    #画像の解像度を200,180に固定
    def save(self,*args,**kwargs):
        super().save(*args,*kwargs)
        if self.image:
            img=Image.open(self.image.path)

            fixed_width=200
            fixed_height=180
            img=img.resize((fixed_width,fixed_height),Image.LANCZOS)
            img.save(self.image.path)
    
    def __str__(self):
        return self.title

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=80)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
    
class taxcategory(models.Model):
    taxcategory_id=models.AutoField(primary_key=True)
    taxcategory_name=models.CharField(max_length=80)
    taxrate=models.FloatField()

    def __str__(self):
        return self.taxcategory_name
    
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=80)
    authcategory=models.ForeignKey("authcategory",on_delete=models.PROTECT)

    def __str__(self):
        return self.username
    
class authcategory(models.Model):
    authcategory_id=models.AutoField(primary_key=True)
    authcategory_name=models.CharField(max_length=80)

    def __str__(self):
        return self.authcategory_name
    
class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    user=models.ForeignKey("user",on_delete=models.PROTECT)
    dish=models.ForeignKey("dish",on_delete=models.PROTECT)
    status=models.ForeignKey("status",on_delete=models.PROTECT)
    ordered_at=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        #status_idが２になったら、orderd_atを現在日時に設定
        if self.status_id ==2:
            self.ordered_at=timezone.now()
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.dish}({self.user})[{self.status}]"
    
class status(models.Model):
    status_id=models.AutoField(primary_key=True)
    status_name=models.CharField(max_length=80)
    def __str__(self):
        return self.status_name
