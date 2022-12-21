from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.


# ListView
class TaskListView(ListView):
    # defining generic view- ListViews we use class instead of def and import ListView as above
    model = Task  # 1. we need to specify model ie;table
    template_name = 'home.html'  # 2. specifying where to display the list
    context_object_name = 'task1'  # 3. variable we used in home.html to list
    # add path in url.py app folder


# DetailView
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'


# UpdateView
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')

    def get_success_url(self):# fn defined to retun page to specified url
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


# DeleteView
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task1'
    success_url = reverse_lazy('cbvhome')  # redircting to home page after deletion


def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'task1': task1})


# def details(request):
#     task = Task.objects.all()
#     return render(request,'detail.html',{'task':task})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def cbvpdate(request, task_id):
    task = Task.objects.get(id=task_id)
    fTask = TodoForm(request.POST or None, instance=task)
    if fTask.is_valid():
        fTask.save()
        return redirect('/')
    return render(request, 'home.html', {'fTask': fTask, 'task': task})


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    fTask = TodoForm(request.POST or None, instance=task)
    if fTask.is_valid():
        fTask.save()
        return redirect('/')
    return render(request, 'update.html', {'fTask': fTask, 'task': task})
