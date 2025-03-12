from django.http import HttpResponse
from django.shortcuts import redirect, render

from todos.forms import TodoForm
from todos.models import Todo

# Create your views here.


# dev_1
def home(request):
    # return HttpResponse("<h1>안녕하세요</h1>")
    return render(request, "home.html")


# dev_3


def todo_list(request):
    # select * from todos where complete=0
    todos = Todo.objects.filter(complete=False)
    print(todos)
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_post(request):

    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")

    else:
        form = TodoForm()

    return render(request, "todo/todo_post.html", {"form": form})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)  # filter는 1개이상, get은 단일객체
    return render(request, "todo/todo_detail.html", {"todo": todo})


def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")

    else:
        form = TodoForm(instance=todo)  # 레코드, 튜플
    return render(request, "todo/todo_post.html", {"form": form})


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect("todo_list")


def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, "todo/done_list.html", {"dones": dones})
