from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime

from main.forms import ProductForm
from main.models import Product
from django.utils.html import strip_tags


# ===========================
# MAIN PAGE
# ===========================
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        'npm': '2406436045',
        'name': request.user.username,
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


# ===========================
# CRUD PRODUCT
# ===========================
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "edit_product.html", context)


@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {'product': product})


# ===========================
# JSON & XML SERIALIZATION
# ===========================
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'image': product.image.url if product.image else None,
            'date_added': product.date_added.isoformat() if product.date_added else None,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        if not product_item.exists():
            return HttpResponse(status=404)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'image': product.image.url if product.image else None,
            'date_added': product.date_added.isoformat() if product.date_added else None,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Produk tidak ditemukan'}, status=404)


# ===========================
# AUTHENTICATION
# ===========================
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


# ===========================
# AJAX HANDLER
# ===========================
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    category = strip_tags(request.POST.get("category"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user if request.user.is_authenticated else None
    new_product = Product(
        name=name,
        description=description,
        price=int(price) if price else 0,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )

    new_product.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == "DELETE":
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return JsonResponse({"message": "Product deleted successfully"}, status=200)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
@require_POST
def update_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))

    product.name = name
    product.price = price
    product.description = description
    product.save()
    return JsonResponse({"success": True})
