# fnl/urls.py
from django.urls import path
from .views import DeleteDisView, BlogDetailView, UpdateDisView, homePageView, aboutPageView, Cal1PageView, BlogListView, AddDisView, delPageView, ShowDataPageView


urlpatterns = [
    path('', homePageView, name='home'),
    path('home/', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('cal_1/', Cal1PageView.as_view(), name='cal_1'),
    path('manage/', BlogListView.as_view(), name='manage'),
    path('manage_detail/<int:pk>/', BlogDetailView.as_view(), name='manage_detail'),
    path('add_dis/',AddDisView.as_view(), name='add_dis'),
    path('edit_dis/<int:pk>/', UpdateDisView.as_view(), name='edit_dis'),
    path('delete_dis/<int:pk>/', DeleteDisView.as_view(), name='delete_dis'),
    path('removesuc', delPageView, name='removesuc'),
    path('alldata/', ShowDataPageView.as_view(), name='alldata'),


]