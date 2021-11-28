"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from list import views
from django.urls import path,re_path

app_name='list'

urlpatterns = [
    path('',views.PostLV.as_view(),name='index'),

    path('post/',views.PostLV.as_view(),name='post_list'),

    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(),name='post_detail'),

    path('search/',views.SearchFormView.as_view(),name='search'),

    path('add/',views.PostCreateView.as_view(),name="add",),

    path('change/',views.PostChangeLV.as_view(), name="change",),

    path('<int:pk>/update/',views.PostUpdateView.as_view(),name="update",),

    path('<int:pk>/delete/',views.PostDeleteView.as_view(),name="delete",),
]
