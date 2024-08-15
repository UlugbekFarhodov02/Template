from django.urls import path
from .views import index_view, AboutListView,ContactFormView,FaqListView, ProductListView,ProductsListView,Sign_inListView,Sign_upListView,StoryListView


urlpatterns = [
    path('',index_view,name='index-page'),
    path('story/',StoryListView.as_view(),name='story-page'),
    path('about/',AboutListView.as_view(),name='about-page'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('faq/', FaqListView.as_view(), name='faq-page'),
    path('product/', ProductListView.as_view(), name='product-page'),
    path('products/', ProductsListView.as_view(), name='products-page'),
    path('sign-in/', Sign_inListView.as_view(), name='sign_in-page'),
    path('sign-up/', Sign_upListView.as_view(), name='sign_up-page')
]
