from django.db import models

# Create your models here.
class Add_Student(models.Model):
    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    class1=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=boolChoice)
    email=models.EmailField(blank=True)
    phoneno=models.IntegerField()
    photo= models.ImageField(blank=True,upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return str(self.name)


class Compant_details(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    salary = models.IntegerField()
    bond = models.IntegerField()
    email = models.EmailField(max_length=200)
    careteria = models.CharField(max_length=200)
    phoneno = models.IntegerField()

    def __str__(self):
        return self.name

class Add_placement(models.Model):
    student_name=models.ForeignKey(Add_Student,on_delete=models.CASCADE)
    company_name=models.ForeignKey(Compant_details,on_delete=models.CASCADE)
    year=models.IntegerField()

    def __str__(self):
        return str(self.student_name)







