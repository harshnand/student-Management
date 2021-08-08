from django import forms
from .models import Compant_details
from .models import Add_placement
class CompanyDetailsForm(forms.ModelForm):
    class Meta:
        model = Compant_details
        # fields=['name','address','salary','bond','email','careteria','phoneno']
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyDetailsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter  Name'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter address'
        self.fields['salary'].widget.attrs['placeholder'] = 'Enter Salary'
        self.fields['bond'].widget.attrs['placeholder'] = 'Enter Bond'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['careteria'].widget.attrs['placeholder'] = 'Enter careteria'
        self.fields['phoneno'].widget.attrs['placeholder'] = 'Enter phoneno'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AddplacementForm(forms.ModelForm):
    class Meta:
        model = Add_placement
        # fields=['name','address','salary','bond','email','careteria','phoneno']
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(AddplacementForm, self).__init__(*args, **kwargs)
        self.fields['student_name'].widget.attrs['placeholder'] = 'select student'
        self.fields['company_name'].widget.attrs['placeholder'] = 'select company'
        self.fields['year'].widget.attrs['placeholder'] = 'Enter Selection year'
        # # self.fields['bond'].widget.attrs['placeholder'] = 'Enter Bond'
        # self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        # # self.fields['careteria'].widget.attrs['placeholder'] = 'Enter careteria'
        # self.fields['phoneno'].widget.attrs['placeholder'] = 'Enter phoneno'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



