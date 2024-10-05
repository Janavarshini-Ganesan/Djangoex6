from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel
from django.urls import reverse
from django.http import HttpResponse

# Home view
def home(request):
    return render(request, 'home.html')

# Create record view
def create1(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        description = request.POST['description']
        
        # Create the new product record
        MyModel.objects.create(product_name=product_name, price=price, quantity=quantity, description=description)
        
        # Redirect to success page after creation
        return redirect('success_create')  # Use a different name for success after creation
    
    return render(request, 'create.html')

# Read (List) records view
def read(request):
    records = MyModel.objects.all()  # Assuming you're retrieving all records
    return render(request, 'read.html', {'records': records})

# Update record view
def update(request, pk):
    product = get_object_or_404(MyModel, pk=pk)  # Fetch the product by its primary key
    if request.method == 'POST':
        product.product_name = request.POST['product_name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.description = request.POST['description']
        product.save()
        return redirect('readtab')  # Redirect to read page after updating
    return render(request, 'update.html', {'product': product})

# Delete individual record view (by primary key)
def delete(request, pk):
    product = get_object_or_404(MyModel, pk=pk)
    product.delete()
    return redirect('readtab')

# Success view after creation
def success_create(request):
    success_message = request.GET.get('message', 'Record created successfully!')
    return render(request, 'success.html', {'success_message': success_message})

# Delete confirmation page (before confirming deletion)
def delete_confirmation(request):
    return render(request, 'delete.html')

# Final delete confirmation step
def delete_confirm(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        return render(request, 'confirm_delete.html', {'product_name': product_name})

# Deleting the product by name
def delete_product(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        
        # Use filter() to find products with the given name
        products = MyModel.objects.filter(product_name=product_name)
        
        if products.exists():
            products.delete()  # Delete all matching products
            return render(request, 'delete_success.html', {'success_message': 'Record deleted successfully!'})  # Success message page
        else:
            # If no products are found, return to delete page with an error message
            return render(request, 'delete.html', {'error_message': 'No product found with that name'})

# Success view after deletion
def success_delete(request):
    return render(request, 'delete_success.html')
