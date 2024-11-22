from . import views
from django.urls import path


app_name = 'food'
# food/
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # /food/
    path('item/', views.index, name="item"),
    # /food/1
    path('<int:pk>/', views.FoodDetail.as_view(), name="detail"),
    # add items
    path('add/', views.CreateItem.as_view(), name="create_item"),
    # edit
    path('update/<int:item_id>/', views.update_item, name="update_item"),
    # delete
    path('delete/<int:item_id>', views.delete_item, name="delete_item"),
]