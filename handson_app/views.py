from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm

# Create your views here.

def home(request):
    items = Item.objects.all()
    return render(request, 'handson_app/home.html', {'items': items})

class ItemListView(ListView):
    model = Item
    template_name = 'handson_app/item_list.html'
    context_object_name = 'items'

# 新規作成（Create）
class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'handson_app/item_form.html'
    success_url = reverse_lazy('handson_app:item_list')

# 更新（Update）
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'handson_app/item_form.html'
    success_url = reverse_lazy('handson_app:item_list')

# 削除（Delete）
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'handson_app/item_confirm_delete.html'
    success_url = reverse_lazy('handson_app:item_list')