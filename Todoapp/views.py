from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Task
from .forms import TaskForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all()
        ctx = {'Task_list': tasks}
        return render(request, 'Todoapp/Task_list.html', ctx)

class OpenView(View):
    def get(self, request):
        return render(request, 'Todoapp/logout_view.html')

class TodoCreateView(View):
    def get(self, request):
        form = TaskForm()
        ctx = {"form": form}
        return render(request, "Todoapp/Task_form.html", ctx)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Todoapp/Task_success.html")
        else:
            ctx = {'form': form}
            return render(request, "Todoapp/Task_form.html", ctx)

class TodoDeleteView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('Todoapp:all')

class MarkCompletedView(View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.complete = True
        task.save()
        return redirect('Todoapp:all')


