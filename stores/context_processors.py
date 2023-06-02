from . models import CarCategory,CartItem

def categorys(request):
    cats =CarCategory.objects.filter()

    return{
        'catloops':cats
    }

def allcart(request):
    
    if request.session.get('cart_id',None):
        cart = CartItem.objects.filter()
        total = cart.count()
    elif request.user:
        cart = CartItem.objects.filter()
        total = cart.count()
    return {
        'carts':total
    }
        