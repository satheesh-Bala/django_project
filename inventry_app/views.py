from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

current_sku = None


def add_product(request):
    if request.method == 'POST':
        sku = current_sku
        name = request.POST['name']
        other_category = request.POST.get('otherCategory', None)
        price = request.POST['price']
        quantity = request.POST['quantity']
        location = request.POST['location']
        brand = request.POST['brand']
        manufacturer = request.POST['manufacturer']
        vendor = request.POST['vendor']
        description = request.POST['description']
        images = request.FILES.getlist('images[]')

        if other_category:
            category_obj, _ = Category.objects.get_or_create(
                name=other_category)

        else:
            category_name = request.POST['category']
            category_obj = Category.objects.get(name=category_name)

            print(category_obj)

        prod = Product1.objects.create(
            sku=sku,
            name=name,
            category=category_obj,
            price=price,
            quantity=quantity,
            location=location,
            brand=brand,
            manufacturer=manufacturer,
            vendor=vendor,
            description=description
        )
        prod.save()

        # Process the uploaded images
        i = 0
        for im in images:
            img = Image1.objects.create(product=prod, image=im)
            img.save()
            i = i+1
        return render(request, 'added.html', {'result': i})
    else:
        return render(request, 'failed.html')


def add_item(request):
    global current_sku
    categories = Category.objects.all()
    try:
        latest_product = Product1.objects.latest('id')
        latest_pk = latest_product.id
        current_sku = f"sku{latest_pk + 1}"
    except Product1.DoesNotExist:
        current_sku = "sku1"
    context = {'categories': categories, 'sku': current_sku}
    return render(request, 'add_item.html', context)


def home(request):
    listedSite = ecommerceSites.objects.all()
    return render(request, 'listed_online.html', {'listedSite': listedSite})


class ProductSearchView(View):
    def get(self, request):
        sku = request.GET.get('sku')
        products = Product1.objects.filter(
            sku__icontains=sku).values('sku', 'name')
        print(products)
        return JsonResponse(list(products), safe=False)
