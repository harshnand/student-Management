from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add_student_detail/',views.Add_student_details,name='addstudentdetail'),
    path('student/',views.Student_details,name='studentdetails'),
    path('company/',views.Company_details,name='companydetails'),
    path('placement/',views.Add_Placement_details,name='addplacement'),
    path('placement_details/',views.Placement_Details,name="placementdetails"),
    path('company_details/',views.View_Company_Details,name="viewcompanydetails"),
    path('login/',views.login,name='login'),
    path('register/',views.register,name="register"),
    path('edit_student/<int:id>',views.Student_edit,name="editstudent"),
    path('edit_company/<int:id>',views.Compant_edit,name="editCompany"),
    path('update_student/<int:id>',views.Student_update,name="updatestudent"),
    path('delete_student/<int:id>',views.Student_delete,name="delatestudent"),
    path('thankyou/',views.thankyou,name='thankyou'),

]
