from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import faculty_login
from  student.models import students

# Create your views here.
def faculty (request):
    if request.session.get('fuser'):
        return redirect('home')
    else:    
        return render (request,'faculty.html')


def flogin (request):
    fuser=request.POST['fuser']
    fpass=request.POST['fpass']

    #return HttpResponse (fuser)

    res = faculty_login.objects.filter(fuser=fuser,fpass=fpass)

    if len(res)==1:
        request.session['fuser'] = res [0].fuser
        return redirect('home')
       

    else :
        return render (request,'faculty.html',{'error':'Username or Password is incorrect !!!'})


def home (request):
    if request.session.get('fuser'):
        return render (request,'home.html')

    else:
        return redirect('/Faculty/')    


def log_out(request):
    del request.session['fuser']
    return  redirect('/Faculty/')  


def account(request):
    if request.session.get('fuser'):
        return render (request,'account.html')

    else:
        return redirect('/Faculty/')   

def creat_account(request) :
    sname= request.POST['sname']       
    rollno= request.POST['rollno']       
    spass= request.POST['spass']     

    res = students.objects.filter(rollno=rollno)  
    
    if len (res)>0:
        return render(request,'account.html',{'msg':'Student with this roll no already exists!!!'})

    else:
        q = students(sname=sname,rollno=rollno,spass=spass)    
        q.save()

        return render(request,'account.html',{'msg':'Account created successfully!!!'})


def marks (request):
    if request.session.get('fuser'):
        res= students.objects.all()
        return render (request,'marks.html',{'res':res})

    else:
        return redirect('/Faculty/')

def updated_marks (request):
    marks = request.POST.getlist('marks')

    #return HttpResponse(marks)

    res = students.objects.all()

    ln = len(res)+1

    for i,j in zip(range(1,ln),marks):
        upd = students.objects.get(id=i)
        upd.marks = j
        upd.save()


    res = students.objects.all()

    return render (request,'updated_marks.html',{'res': res})  


def che_marks (request):
    res = students.objects.all()

    return render (request,'updated_marks.html',{'res': res})