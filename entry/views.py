from django.shortcuts import render
from .models import diary_page
from .models import todo
from .forms import diary_page_form
from django.shortcuts import redirect

def page_list(request):
    pages = diary_page.objects.filter().order_by('date')
    todo_list = todo.objects.filter().order_by('date_added')
    if request.method == "POST":
        print(request.POST)
        done = request.POST.getlist('completed')
        for d in done:
            todo.objects.filter(pk=d).delete()
        if 'add_todo' in request.POST:
            new_todo = todo()
            new_todo.point = request.POST.get('add_todo')
            new_todo.add()
        if 'delete_page' in request.POST:
            pk = request.POST.get('delete_page')
            diary_page.objects.filter(pk=pk).delete()
        return redirect('page_list')
    return render(request, 'entry/page_list.html', {'pages':pages, 'todo_list':todo_list})

def add_page(request):
    if request.method == 'POST':
        form = diary_page_form(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()
            return redirect('page_list')
    else:
        form = diary_page_form()
    return render(request, 'entry/add_to_diary.html', {'form':form})


