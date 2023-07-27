from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from .models import Item,cartItem
from django.views import View
import time
from django.conf import settings

class home(View):
    def post(self,request):
        product=request.POST.get('item')
        print(product)
    def get(self,request):
         items=Item.objects.all()
         return render(request,'home.html',{'items':items})
 

def register(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get("conpass")
        if pass1 != pass2 :
            return render(request, 'register.html',{'erro_message':'password does not match.please enter password again.'})
        else:
            if User.objects.filter(username=name).exists():
                return render(request, 'register.html', {'error_message': 'Username already exists. Please choose a different username.'})
            else:
                
                my_user = User.objects.create_user(name, uname, pass1)
                my_user.save()
                return redirect("home")

    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html")

    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect(user_login)
    
def add_to_cart(request):
    if request.method=='POST':
        item_id=request.POST.get('item')
        item=Item.objects.get(pk=item_id)
        cart_item,created=cartItem.objects.get_or_create(item=item,user=request.user)
        cart_item.quantity+=1
        cart_item.save()
        return render(request,'cart.html')
    return render(request,'cart.html') 

import razorpay
from django.conf import settings
from django.shortcuts import render
from .models import PaymentDetail
def payment_product(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        order_id = request.POST.get('order_id')
        amount_in_paisa = int(float(amount) * 100)
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_SECRET_KEY))
        razorpay_order = client.order.create(dict(amount=amount_in_paisa, currency='INR'))
        razorpay_order_id = razorpay_order['id']
        return render(request, 'payment.html', {'amount': amount_in_paisa, 'order_id': int(order_id), 'razorpay_order_id': razorpay_order_id})
    else:
        return render(request, 'payment.html')
def payment_success(request):
    if request.method=='POST':
         
        #  payment_id=request.POST.get('razorpay_payment_id')
        #  order_id=request.POST.get('razorpay_order_id')
        #  signature=request.POST.get('razorpay_signature')
        #  item=Item.objects.get(pk=order_id)
        #  payment_detail = PaymentDetail.objects.create(
        #     name=request.user.username,  
        #     email=request.user.email,
        #     product_name=item.name,
        #     price=item.price,
        #     payment_id=payment_id,
        # )
         
         return render(request,'payment_success.html')
    else:
        return render(request, 'payment.html')
    