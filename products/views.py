from django.http import HttpResponse

def product_list(request):
    return HttpResponse('<h1>Product List</h1>')

def product_detail(request, product_id):
    return HttpResponse(f"<h1>Product Details: {product_id}</h1>")
