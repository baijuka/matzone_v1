from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, ProductVariation
from django.db.models.functions import Lower
from django.forms import formset_factory
from .forms import ProductForm, ProductVariationForm


def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    variation_formset = formset_factory(ProductVariationForm, extra=5)
    
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to access this page.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        formset = variation_formset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            product = form.save()
            print('FORM',product.id)
            for item in formset:
                instance = item.save(commit=False)
                instance.product_id = product.pk
                print (instance.pk)
                instance.save()
          
            # size = request.POST['size']
            # price = request.POST['price']
            # stock = request.POST['stock']
            # variation = ProductVariation(size=size, price=price, stock=stock, product=product)
            #variation.save()
            #formset.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        formset = variation_formset()
        #variation_form = ProductVariationForm()
        ## form = ProductVariationForm()
        ##form = inlineformset_factory(parent_model=Category, model=Product, fk_name='category', extra=1, fields=('category','name', 'sku', 'description',))
        
    template = 'products/add_product.html'
    context = {
        'form': form,
        'formset': formset
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to access this page.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to access this page.")
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))