from django.shortcuts import render,redirect
from todo_list.forms import TodoForm
from . models import Todo

# Create your views here.

def home(request):
    # creating object for TodoForm, defined in forms.py
    form = TodoForm()
    # print(form)
    # to get all data from database we create a variable todos and store
    todos= Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    # passing  object form inside render as a dictionary
    return render(request ,'home.html',{'form':form ,'todos':todos})


def update(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            return redirect('home')

    return render(request, 'update.html', {'form':form})



def delete(request,todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
        return redirect('home')