


from django.shortcuts import render
from .models import Contact,About,Faq,Story,Index,Product,Products,Sign_in,Sign_up
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .bot import send_message
from django.views.generic.list import ListView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class =ContactForm
    success_url = "/"
 
    def form_valid(self,form):
      full_name = form.cleaned_data.get('full_name')
      email_addres= form.cleaned_data.get('email_addres')
      content = form.cleaned_data.get('content')
      text = f"Full name: {full_name}\nEmail: {email_addres}\ntext: {content}"
      send_message(text)
      form.save()
      return super().form_valid(form)






class AboutListView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'


class StoryListView(ListView):
    model = Story
    template_name = 'story.html'
    context_object_name = 'story'







class FaqListView(ListView):
    model = Faq
    context_object_name = 'faq'
    template_name = "faq.html"



def index_view(requests):
    index = Index.objects.all()
    context = {
        "index" : index,
    }
    return render(requests, 'index.html',context)





class ProductListView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = "product.html"

    

class ProductsListView(ListView):
    model = Products
    template_name = "products-single.html"
    context_object_name = "category"

class ProductListView(ListView):
    model = Products
    template_name = "product.html"
    context_object_name = "category"

    
class Sign_inListView(ListView):
    model = Sign_in
    template_name = "sign_upsingle.html"
    context_object_name = "sign"

class Sign_upListView(ListView):
    model = Sign_up
    template_name = "sign_upsingle.html"
    context_object_name = "sign_up"

    