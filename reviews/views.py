from django.shortcuts import render

from reviews.forms import FormProduct
from reviews.models import Product, Review
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    # products = Product.objects.all()
    products = Product.objects.all()[:3]  # Ambil tiga produk pertama
    return render(request, 'index.html', {'products': products})

def product_reviews(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'product_reviews.html', {'product': product, 'reviews': reviews})

def add_review(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        author = request.POST['author']
        content = request.POST['content']
        rating = request.POST['rating']
        review = Review(product=product, author=author, content=content, rating=rating)
        review.save()
        return redirect('product_detail', product_id=product_id)
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

    
def product(request):
    products = Product.objects.all()

    konteks = {
        'products': products,
    }
    return render(request, 'index.html', konteks)

    
def add_product(request):
    if request.POST:
        form = FormProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormProduct()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'add_product.html', konteks)
    else:
        form = FormProduct()

        konteks = {
            'form': form,
        }

    return render(request, 'add_product.html', konteks)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})


from django.shortcuts import render, get_object_or_404
from .models import Product

def ImagePath(request, product_id):
    # Menggunakan get_object_or_404 untuk mendapatkan objek Product
    product = get_object_or_404(Product, id=product_id)

    # Mengambil URL cover dan mengganti tanda slash menjadi backslash
    if product.cover:
        product_cover_url = product.cover.url.replace("/", "\\")
    else:
        product_cover_url = None

    return render(request, 'index.html', {'product': product, 'product_cover_url': product_cover_url})
