from django.shortcuts import render,redirect,get_object_or_404

from .forms import CompanyDetailsForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Add_Student,Compant_details,Add_placement
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'student/home.html')

def Add_student_details(request):

    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        class1 = request.POST['class1']
        semester = request.POST['semester']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        photo = request.POST['photo']

        ss=Add_Student(name=name,address=address,class1=class1,semester=semester,age=age,gender=gender,email=email,phoneno=phoneno,photo=photo)
        ss.save()
        print("data saved")








        # for item in request.POST:
        #     key = item
        #     value = request.POST[key]
        #



    return render(request,'student/add_student_details.html')

def Student_details(request):
    st_details=Add_Student.objects.all()
    return render(request,'student/student_details.html',{
        "student":st_details,
    })

def Company_details(request):
    form=CompanyDetailsForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,'data added successfully')
        return redirect('companydetails')

    else:
        form=CompanyDetailsForm()
        messages.error(request,'not saved')


    return render(request,'student/company_details.html',{
        "form":form
    })
def Compant_edit(request,id):
    stu_edit = Compant_details.objects.get(id=id)
    form=CompanyDetailsForm(instance=stu_edit)

    if request.method == 'POST':
        form = CompanyDetailsForm(request.POST, instance=stu_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'data added successfully')
            return redirect('companydetails')

        else:
            form = CompanyDetailsForm()
            messages.error(request, 'not saved')

    return render(request,'student/edit_Company.html',{
        'student':stu_edit,
        "form":form
    })

def Add_Placement_details(request):

    placement=Add_Student.objects.all()

    placement1 = Compant_details.objects.all()



    if request.method =='POST':

        stu=request.POST['stu']
        comp=request.POST['comp']
        year=request.POST['year']

        student=Add_placement(student_name=stu,company_name=comp,year=year)
        student.save()
        return redirect('addplacement')
        messages.success(request,"saved successfully")



    return render(request,'student/Add_placement_Details.html',{
        'placement':placement,
        'placement1': placement1,


    })




def Placement_Details(request):
    return render(request,'student/view_Placement.html')

def login(request):
    return render(request,'student/login.html')

def register(request):
    return render(request,'student/register.html')

def thankyou(request):
    return render(request,'student/thankyou.html')


def Student_edit(request,id):
    stu_edit=Add_Student.objects.get(id=id)
    return render(request,'student/edit_student.html',{
        'student':stu_edit
    })
def Student_delete(request,id):
    stu_edit=Add_Student.objects.get(id=id)
    stu_edit.delete()
    return render(request,'student/home.html')

def Student_update(request,id):
    if request.method =='POST':
        st = Add_Student.objects.get(id=id)
        st.name = request.POST['name']
        st.address = request.POST['address']
        st.class1 = request.POST['class1']
        st.semester = request.POST['semester']
        st.age = request.POST['age']
        st.gender = request.POST['gender']
        st.email = request.POST['email']
        st.phoneno = request.POST['phoneno']
        st.photo = request.POST['photo']
        st.save()
        print("data saved")



    return render(request,'student/student_details.html')

def View_Company_Details(request):
    company=Compant_details.objects.all()
    return render(request,'student/view_company_Details.html',{
        "company":company
    })