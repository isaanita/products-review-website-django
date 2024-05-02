from django.shortcuts import render

from reviews.forms import FormProduct
from reviews.models import Product, Review

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def product_review(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_review.html', {'product': product})

def add_review(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        author = request.POST['author']
        content = request.POST['content']
        rating = request.POST['rating']
        review = Review(product=product, author=author, content=content, rating=rating)
        review.save()
        return redirect('product_detail', product_id=product_id)
    
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
