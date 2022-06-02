from email import message
from django.shortcuts import render, redirect
from app.models import Todo
from app.forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
    item = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            if Todo.objects.filter(item=f.item).exists():
                messages.error(request, "Todo Item Already Exist")
            else:
                f.save()
            return redirect('/')
            
    context = {
        "form": form,
        "item": item,
    }
    return render(request,'index.html', context)

def updateitem(request, pk):
    todo_item = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo_item)
    if request.method == 'POST':
        form = TodoForm(request.POST or None, instance=todo_item)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        "form": form,
    }
    return render(request,'update.html', context)

def deleteitem(request, pk):
    todo_item = Todo.objects.get(id=pk)
    todo_item.delete()
    return redirect('/')
