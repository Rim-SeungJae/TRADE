from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView,MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from list.models import Post
from django.conf import settings
from django.views.generic import FormView
from list.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.

# PostLV view is for showing list of posted data
class PostLV(ListView):
    model=Post
    template_name='list/post_all.html'
    context_object_name='posts'
    paginate_by=5

# PostDV view is for showing detailed information of data
class PostDV(DetailView):
    model=Post

    # get detailed information of data and return
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['disqus_short']=f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id']=f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url']=f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title']=f"{self.object.slug}"
        return context

class PostAV(ArchiveIndexView):
    model=Post
    date_field='modify_dt'

# SearchFormView view is for showing search result
class SearchFormView(FormView):
    form_class=PostSearchForm
    template_name='list/post_search.html'

    # select only valid result of search, and return
    def form_valid(self,form):
        searchWord=form.cleaned_data['search_word']
        post_list=Post.objects.filter(Q(title__icontains=searchWord)|Q(description__icontains=searchWord)|Q(content__icontains=searchWord)).distinct()

        context={}
        context['form']=form
        context['search_term']=searchWord
        context['object_list']=post_list

        return render(self.request,self.template_name,context)

# PostCreateView is for showing how to post new data
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','description','content']
    success_url=reverse_lazy('list:index')

    def form_valid(self,form):
        form.instance.seller=self.request.user
        return super().form_valid(form)

# PostChangeLV is for showing how to change posted data
class PostChangeLV(LoginRequiredMixin,ListView):
    template_name='list/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(seller=self.request.user)

# PostUpdateView is for updating posted data
class PostUpdateView(OwnerOnlyMixin,UpdateView):
    model=Post
    fields=['title','description','content']
    success_url=reverse_lazy('list:index')

# PostDeleteView is for deleting posted data
class PostDeleteView(OwnerOnlyMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('list:change')
