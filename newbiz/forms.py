

from django.db.models.fields import DateField, Field
from.models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


class  CustomerForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"text",
            "placeholder":"Your Name",
            "validators": "validators",
            "style":"max-width:20em",
            
            
            

            }),label="Your Name",required=True,
        
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"email",
            "placeholder":"Your email",
            "validators": "validators",
            "style":"max-width:20em",}),label="email")
    subject = forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "type":"text",
            "placeholder":"subject",
            "validators": "validators",
            "style":"max-width:20em",}),label="subject")
    message = forms.CharField(widget=forms.Textarea
    (attrs={"class":"form-control",

    }),label="massage")
    
    class Meta: 
        model=  Customer
        fields={"name","email","subject","message"}
       
      


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper= FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div("name",css_class="form-group col-lg-6"),
                Div("email",css_class="form-group col-lg-6"),
                css_class='form-row'
 
            ),
            Div(
                Div("subject",css_class="form-group col-lg-6"),
               css_class='form-row' ),
            Div("message",rows="3", css_class='input-xlarge'),
            
            Div(
            Submit('submit', 'submit',css_class='btn btn-outline-success')),
                

          
        )

    
    