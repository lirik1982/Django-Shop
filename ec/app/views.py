from django.shortcuts import render
from django.views import View
from .models import Product
from django.db.models import Count
from .forms import CustumerRegistrationForm
from django.contrib import messages


def home(request):
    return render(request, 'app/home.html')


def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')


class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html",  locals())


class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",  locals())


class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())


class CustumerRegistrationView(View):
    def get(self, request):
        form = CustumerRegistrationForm()
        return render(request, "app/custumerregistration.html", locals())

    def post(self, request):
        form = CustumerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully")
        else:
            messages.warning(request, "Invalid input data")
        return render(request, "app/custumerregistration.html", locals())


class ProfileView(View):
    def get(self, request):
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        return render(request, 'app/profile.html', locals())


