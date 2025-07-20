from django.shortcuts import render,redirect,get_object_or_404
from .models import order
from .models import dish
from .models import category
from .models import user
from .forms import AddcategoryForm
from .forms import AdddishForm
from .forms import AddorderForm 
from .forms import AdduserForm

def startpage(request):
    return render(request,"html/startpage.html")

def admin(request):
    orders=order.objects.all()
    return render(request,"html/admin.html",{"orders":orders})

#メニュー編集画面
def menumanage(request):
    dishes=dish.objects.all()
    if request.method=="POST":
        form=AdddishForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(menumanage)
    else:
        form=AdddishForm()
     
    return render(request,"html/menumanage.html",{"dishes":dishes,"form":form})

#カテゴリ編集画面
def categorymanage(request):
    categories=category.objects.all()
    if request.method=="POST":
        form=AddcategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(categorymanage)
    else:
        form=AddcategoryForm()
     
    return render(request,"html/categorymanage.html",{"categories":categories,"form":form})

#ユーザー編集画面
def usermanage(request):
    users=user.objects.all()
    if request.method=="POST":
        form=AdduserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(usermanage)
    else:
        form=AdduserForm()

    return render(request,"html/usermanage.html",{"users":users,"form":form})

#オーダー編集画面(追加)
def ordermanage(request):
    orders=order.objects.all()
    if request.method=="POST":
        form=AddorderForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(ordermanage)
    else:
        form=AddorderForm()

    return render(request,"html/ordermanage.html",{"orders":orders,"form":form})

#オーダー編集画面(編集)
def order_edit(request,pk):
    Order=get_object_or_404(order,pk=pk)
    if request.method=="POST":
        form=AddorderForm(request.POST,instance=Order)
        if form.is_valid():
            form.save(commit=True)
            return redirect(ordermanage)
    return redirect(ordermanage)

def order_delete(request,pk):
    Order=get_object_or_404(order,pk=pk)
    if request.method=="POST":
        Order.delete()
        return redirect(ordermanage)
    return redirect(ordermanage)

def managepage(request):
    return render(request,"html/admin.html")