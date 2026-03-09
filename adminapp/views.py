from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Group, Teacher, Student, Faculty, Kafedra
from .forms import SubjectForm, GroupForm, TeacherForm, StudentForm, FacultyForm, KafedraForm

def dashboard(request):
    ctx = {
        'subjects_count': Subject.objects.count(),
        'groups_count': Group.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'students_count': Student.objects.count(),
        'faculties_count': Faculty.objects.count(),
        'kafedras_count': Kafedra.objects.count(),
    }
    return render(request, 'dashboard.html', ctx)

# Generic CRUD helper
def crud_view(request, model_class, form_class, redirect_url, obj_id=None):
    obj = get_object_or_404(model_class, id=obj_id) if obj_id else None
    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=obj)
    
    return render(request, 'generic_form.html', {'form': form, 'obj': obj})

# Faculty
def faculty_list(request):
    objects = Faculty.objects.all()
    return render(request, 'faculty/list.html', {'objects': objects})

def faculty_create(request):
    return crud_view(request, Faculty, FacultyForm, 'faculty_list')

def faculty_update(request, pk):
    return crud_view(request, Faculty, FacultyForm, 'faculty_list', obj_id=pk)

def faculty_delete(request, pk):
    obj = get_object_or_404(Faculty, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('faculty_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Kafedra
def kafedra_list(request):
    objects = Kafedra.objects.all()
    return render(request, 'kafedra/list.html', {'objects': objects})

def kafedra_create(request):
    return crud_view(request, Kafedra, KafedraForm, 'kafedra_list')

def kafedra_update(request, pk):
    return crud_view(request, Kafedra, KafedraForm, 'kafedra_list', obj_id=pk)

def kafedra_delete(request, pk):
    obj = get_object_or_404(Kafedra, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('kafedra_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Subjects
def subject_list(request):
    objects = Subject.objects.all()
    return render(request, 'subject/list.html', {'objects': objects})

def subject_create(request):
    return crud_view(request, Subject, SubjectForm, 'subject_list')

def subject_update(request, pk):
    return crud_view(request, Subject, SubjectForm, 'subject_list', obj_id=pk)

def subject_delete(request, pk):
    obj = get_object_or_404(Subject, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('subject_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Groups
def group_list(request):
    objects = Group.objects.all()
    return render(request, 'group/list.html', {'objects': objects})

def group_create(request):
    return crud_view(request, Group, GroupForm, 'group_list')

def group_update(request, pk):
    return crud_view(request, Group, GroupForm, 'group_list', obj_id=pk)

def group_delete(request, pk):
    obj = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('group_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Teachers
def teacher_list(request):
    objects = Teacher.objects.all()
    return render(request, 'teacher/list.html', {'objects': objects})

def teacher_create(request):
    return crud_view(request, Teacher, TeacherForm, 'teacher_list')

def teacher_update(request, pk):
    return crud_view(request, Teacher, TeacherForm, 'teacher_list', obj_id=pk)

def teacher_delete(request, pk):
    obj = get_object_or_404(Teacher, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('teacher_list')
    return render(request, 'delete_confirm.html', {'obj': obj})

# Students
def student_list(request):
    objects = Student.objects.all()
    return render(request, 'student/list.html', {'objects': objects})

def student_create(request):
    return crud_view(request, Student, StudentForm, 'student_list')

def student_update(request, pk):
    return crud_view(request, Student, StudentForm, 'student_list', obj_id=pk)

def student_delete(request, pk):
    obj = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('student_list')
    return render(request, 'delete_confirm.html', {'obj': obj})
