from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # cart = Cart.objects.filter(cart_id=_cart_id)
            # cart_items = CartItem.objects.all()
            # cart = Cart.objects.get(cart_id=_cart_id(request))
            # cart_items = CartItem.objects.filter(cart=cart)
            # cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
            else:
                # cart_items = CartItem.objects.filter(cart=cart)
                # cart = Cart.objects.filter(cart_id=_cart_id(request))
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            # cart = Cart.objects.filter(cart_id=_cart_id(request))
            # cart_items = CartItem.objects.all()
            # print(cart_items)
            for cart_item in cart_items:
                cart_count += cart_item.quantity
            # print(cart_count)
        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count)
