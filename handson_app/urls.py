from django.urls import path
from . import views

app_name = 'handson_app'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),  # リスト表示をデフォルトビューに
    path('create/', views.ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
]