from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def newindex(request):
    return render(request,'index1.html')

def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        place=request.POST['place']
        designation=request.POST['designation']
        image=request.FILES['image']
        age=request.POST['age']
        data=Employee.objects.create(name=name,
                                     age=age,
                                     email=email,
                                     place=place,
                                     designation=designation,
                                     img=image
                                     )
        data.save()
        return redirect(details)
    else:
        return render(request,'form.html')
    
def details(request):
    a=Employee.objects.all()
    return render(request,'view.html',{'data':a})


def Delete(request,id):
    b=Employee.objects.get(id=id)
    b.delete()
    return redirect(details)

def edit(request,id):
    c=Employee.objects.get(id=id)
    if request.method=='POST':
       c.name=request.POST['name']
       c.email=request.POST['email']
       c.age=request.POST['age']
       c.designation=request.POST['designation']
       c.place=request.POST['place']
       c.date=request.POST['date']
     
       if 'image' in request.FILES:
           c.img=request.FILES['image']
           print(c.img)
       c.save()    
       return redirect(details)
    else:
        return render(request,'edit.html',{'Employee':c})
    
def search(request):
    if request.method=='POST':
        d=request.POST.get('name','')
        e=Employee.objects.filter(name__icontains=d)
        return render(request,'view.html',{'data'})
    

def index(request):
    if request.method == 'POST':
        # Retrieve form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        age = request.POST.get('age')
        image = request.FILES.get('image')  

        employee = Employee(
            name=name,
            email=email,
            place=place,
            date_of_birth=dob,
            designation=designation,
            age=age,
            image=image
        )
        employee.save()  # Save the new employee record to the database

        return redirect('employee-details')

    return render(request, 'index.html')



