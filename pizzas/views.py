from django.shortcuts import render, redirect
from .models import *
from .forms import *
from email.mime import image
# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()


    context = {'all_pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('topping_name')
    comments = pizza.comment_set.order_by('-date_added')
    image = Pizza.image

    context = {'pizza':pizza, 'comments':comments, 'toppings':toppings, 'image':image}
    return render(request, 'pizzas/pizza.html', context)

    

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
        
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html',context)





