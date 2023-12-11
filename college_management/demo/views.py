from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from demo.models import  Category,Product

def create_product(request):
    if request.POST:
        category_name = request.POST.get('category')
        product_names = request.POST.getlist('product_name') 
        category, created = Category.objects.get_or_create(name=category_name)
        for product_name in product_names:
            if product_name.strip():
                product, created = Product.objects.get_or_create(name=product_name, category=category)

        return render(request,"formss.html")

    
    return render(request,"formss.html")
def show(request):
    if request.method == 'POST':
        category_id = request.POST.get("selct")
        category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    
    categories = Category.objects.all()
    return render(request, "show.html", {"data": categories, "all": ""})
