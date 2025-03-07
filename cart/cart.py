from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exists
        cart = self.session.get('session_key')

        #If the user is new, no session key, so create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        #Get product ids
        product_ids = self.cart.keys()
        #lookup those keys in products in database
        products = Product.objects.filter(id__in=product_ids)
        #get quantities
        quantities = self.cart
        #Start counting at 0
        total = 0
        for key, value in quantities.items():
            #Convert key string into int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_on_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use ids to lookup products in database
        products = Product.objects.filter(id__in=product_ids)
        #Return looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        #Get cart
        current_cart = self.cart
        #Update cart
        #Find item in cart dictionary with product id and update the qty
        current_cart[product_id] = product_qty

        self.session.modified = True
        updated_cart = self.cart
        return updated_cart
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True




