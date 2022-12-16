from django.http import HttpResponse
from django.shortcuts import render
from mycart.models import Cart
from myapp.models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

# from .models import Cart, CartItem

# Create your views here.


# def cart_details(request):
#     # return HttpResponse("This is a new one")
#     return render(request, 'cart_details.html')

# def cart_add(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("home")
 

##-------------- Cart Views --------------------------------------
# class DetailCart(DetailView):
#     model = Cart
#     template_name='cart/detail_cart.html'

# class ListCart(ListView):
#     model = Cart
#     context_object_name = 'carts'
#     template_name='cart/list_carts.html'

# class CreateCart(CreateView):
#     model = Cart
#     template_name = 'cart/create_cart.html'

# class Updatecart(UpdateView):
#     model = Cart
#     template_name = 'cart/update_cart.html'

# class DeleteCart(DeleteView):
#     model = Cart
#     template_name = 'cart/delete_cart.html'

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return render(request,'product.html')




# def cart(request):
#     c = Cart.objects.all()
#     context = {'cart':c}
#     return render(request, 'cart.html',context=context)

def cart(request):
    p = Product.objects.all()
    context = {'product':p}
    return render(request, 'cart.html',context=context)

    # return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')