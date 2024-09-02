from django.shortcuts import render
from .models import Student

def student_list(request):
    query = request.GET.get('q')
    show_all = request.GET.get('show_all')

    if query:
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    elif show_all:
        students = Student.objects.all()
    else:
        students = []  # Empty list if no search or show all is requested

    return render(request, 'students/student_list.html', {'students': students})
