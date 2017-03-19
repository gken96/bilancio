from django.shortcuts import render
from django.utils import timezone
from .models import buy_list
# Create your views here.
def post_list(request):
    posts = buy_list.objects.all()
    return render(request, 'budget/post_list.html', {'posts':posts})
