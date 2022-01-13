from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, ProductVariation, Review
from django.db.models.functions import Lower
from django.forms import formset_factory, inlineformset_factory
from .forms import ProductForm, ProductVariationForm, ReviewForm
from django.core.paginator import Paginator


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
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    review = Review.objects.all()

    context = {
        'products': product_list,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'review': review,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product_id=product.id, status=True)
    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    variation_formset = formset_factory(ProductVariationForm, extra=1)
    
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to access this page.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        formset = variation_formset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            product = form.save()

            for item in formset:
                instance = item.save(commit=False)
                instance.product_id = product.pk
                instance.save()

            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        formset = variation_formset()
                
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
        
    product = get_object_or_404(Product, id=product_id)
    variationFormset = inlineformset_factory(Product, ProductVariation, fields="__all__", extra=1)
    formset = variationFormset(instance=product)
 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None, instance=product)       
        formset = variationFormset(request.POST, instance=product)
        if form.is_valid():
            form.save()

        if formset.is_valid():
            formset.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        instance = get_object_or_404(Product, id=product_id)   
        form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
        formset = variationFormset(instance=product)

        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'formset': formset,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to access this page.")
        return redirect(reverse('home'))

    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
    else:
        product = get_object_or_404(Product, pk=product_id)
        template = 'products/delete_product.html'
        context = {
            'product': product,
        }
    return render(request, template, context)

    
#Credit : https://www.youtube.com/watch?v=eIN1nZCt7Ww

@login_required
def add_review(request, product_id):
    url = request.META.get('HTTP_REFERER')

    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                reviews = Review.objects.get(user_profile__id=request.user.id, product__id=product_id)
                form = ReviewForm(request.POST, instance=reviews)
                form.save()
                messages.success(request, 'Thank you! Your review has been updated.')
                return redirect(reverse('products'))
            except Review.DoesNotExist:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    data = Review()
                    data.subject = form.cleaned_data['subject']
                    data.rating = form.cleaned_data['rating']
                    data.review = form.cleaned_data['review']
                    data.product_id = product_id
                    data.user_profile_id = request.user.id
                    data.save()
                    messages.success(request, 'Thank you! Your review has been submitted.')
                    return redirect(reverse('products'))
        else:
            template = 'products/add_review.html'
            product = get_object_or_404(Product, id=product_id)
            context = {
                'product': product,
            }
        
        return render(request, template, context)
    else:
        messages.error(request, 'Sorry, only logged in users can \
            leave a review.')
        return redirect(reverse('login'))


@login_required
def edit_review(request, review_id):

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only logged in users can \
            edit a review.')
        return redirect(reverse('login'))

    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)       
            if form.is_valid():
                form.save()
        else:
            form = ReviewForm(instance=review)
            messages.info(request, f'You are editing {review.product}')

        template = 'products/edit_review.html'
        context = {
            'form': form,
            'review': review,
        }

        return render(request, template, context)