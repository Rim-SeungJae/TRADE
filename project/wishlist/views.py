from django.shortcuts import render
from django.views.generic import ListView,DetailView
from wishlist.models import Wishlist

from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.

class WishlistLV(ListView):
    model=Wishlist

class WishlistDV(DetailView):
    model=Wishlist
    
class WishlistCreateView(LoginRequiredMixin,CreateView):
    model=Wishlist
    fields=['title','url']
    success_url=reverse_lazy('wishlist:change')

    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class WishlistChangeLV(LoginRequiredMixin,ListView):
    template_name='wishlist/wishlist_change_list.html'

    def get_queryset(self):
        return Wishlist.objects.filter(owner=self.request.user)

class WishlistUpdateView(OwnerOnlyMixin,UpdateView):
    model=Wishlist
    fields=['title','url']
    success_url=reverse_lazy('wishlist:change')

class WishlistDeleteView(OwnerOnlyMixin,DeleteView):
    model=Wishlist
    success_url=reverse_lazy('wishlist:change')
                
