from django.conf.urls import patterns, url
from deli import views

urlpatterns = patterns('',
    url(r'^restaurants/$',
        views.RestaurantList.as_view(),
        name='Restaurant-list'),
     url(r'^restaurants/(?P<pk>[0-9]+)/$',
        views.RestaurantDetail.as_view(),
        name='restaurant-detail'),
    url(r'^food/$',
        views.FoodItemList.as_view(),
        name='FoodItem-list'),
    url(r'^food/(?P<pk>[0-9]+)/$',
        views.FoodItemtDetail.as_view(),
        name='fooditem-detail'),
)