from django.db.models.fields import URLField

from django.utils.text import slugify
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class newbiz(models.Model):
    title =models.CharField (max_length=200,verbose_name=_("عنوان الموقع "))
    icon = models.ImageField(verbose_name=_("ايقوتة الموقع "),upload_to="img/")
    logo = models.ImageField(verbose_name=_("اللوجو"),upload_to="img/")
    imagew=models.ImageField(verbose_name=_("صورة الصفحه"),upload_to="img/")
    alt=models.CharField(max_length=500,verbose_name=_("وصف الصوره  "))
    wordaboveimage1=models.CharField(max_length=200,verbose_name=_("كلام فوق الصوره "))
    wordaboveimage2=models.CharField(max_length=200,verbose_name=_("كلام فوق الصوره "))
    wordaboveimage3=models.CharField(max_length=200,verbose_name=_("كلام فوق الصوره "))
    actionone=models.CharField(max_length=200,verbose_name=_("الزر الاول  "))
    actiontwo=models.CharField(max_length=200,verbose_name=_("الزر الثاني "))
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
def __str__(self):
    return str(self.title)
def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(newbiz,self).save(*args, **kwargs)  # save
    











class Aboutus(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("العنوان "))
    description=models.TextField(max_length=2000,verbose_name=_("الوصف"))
    descriptiontwo=models.TextField(max_length=2000,verbose_name=_("الوصف"))
    titletwo=models.CharField(max_length=200,verbose_name=_("العنوان في عنا"))
    descriptiontthre=models.TextField(max_length=2000,verbose_name=_("الوصف في عنا"))
    imageone=models.ImageField(verbose_name=_("صوره في عنا"),upload_to="img/")
    titleimageone=models.CharField(max_length=200,verbose_name=_("العنوان بجانب الصوره"))
    description=models.TextField(max_length=3000,verbose_name=_("الوصف بجانب الصوره"))
    imagetwo=models.ImageField(verbose_name=_("صوره في عنا"),upload_to="img/")
    titleimagetwo=models.CharField(max_length=200,verbose_name=_("العنوان بجانب الصوره"))
    descriptiontwo=models.TextField(max_length=3000,verbose_name=_("الوصف بجانب الصوره"))
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
def __str__(self):
    return str(self.title)



def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(Aboutus,self).save(*args, **kwargs)  # save



class Service(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("خدمتنا"))
    descriptionservice=models.TextField(max_length=3000,verbose_name=_(",وصف الخدمات"))
    titleservice=models.TextField(max_length=200,verbose_name=_("عنوان الخدمه الاولي"))
    descriptionso=models.TextField(max_length=3000,verbose_name=_("وصف الخدمه الاولي"))
    titleservice2=models.TextField(max_length=200,verbose_name=_("2عنوان الخدمه "))
    description2=models.TextField(max_length=3000,verbose_name=_("وصف الخدمه2"))
    titleservice3=models.TextField(max_length=200,verbose_name=_("عنوان الخدمه3"))
    description3=models.TextField(max_length=3000,verbose_name=_("وصف الخدمه3"))
    titleservice4=models.TextField(max_length=200,verbose_name=_("عنوان الخدمه4"))
    description4=models.TextField(max_length=3000,verbose_name=_("وصف الخدمه4"))
    titleservice5=models.TextField(max_length=200,verbose_name=_("عنوان الخدمه5"))
    description5=models.TextField(max_length=3000,verbose_name=_("وصف الخدمه5"))
    titleservice6=models.TextField(max_length=200,verbose_name=_("عنوان الخدمه6"))
    description6=models.TextField(max_length=3000,verbose_name=_("وصف الخدمه6"))
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    phonenumber = PhoneNumberField(blank=True)
    
def __str__(self):
    return str(self.title)


def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(Service,self).save(*args, **kwargs)  # save


class whychooseus(models.Model):
    title=models.CharField(max_length=200,verbose_name=_("العنوان"))
    description=models.TextField(max_length=3000,verbose_name=_("الوصف"))
    choo=models.ForeignKey("Choose",related_name="whychooseus_Choose",on_delete=models.CASCADE,verbose_name=_("لماذا يختارنا"))
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
def __str__(self):
    return str(self.title)



def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(whychooseus,self).save(*args, **kwargs)  # save

class Choose(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/")
    description=models.TextField(max_length=3000)
    
def __str__(self):
    return str(self.title)

    


class OurPortfolio(models.Model):
    title=models.CharField(max_length=300,verbose_name=_("العنوان"))
    
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    
def __str__(self):
    return str(self.title)

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(OurPortfolio,self).save(*args, **kwargs)  # save


class imagelist(models.Model):
    name = models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/")

    
def __str__(self):
    return str(self.name)





class Team(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to="img/")
    fac_link=models.URLField(max_length=300, verbose_name=_("facbook"),null=True)
    twi_link=models.URLField(max_length=300, verbose_name=_("twitter"),null=True)
    gma_link=models.URLField(max_length=300, verbose_name=_("gmail"),null=True)
    ins_link=models.URLField(max_length=300, verbose_name=_("instgram"),null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )

    
def __str__(self):
    return str(self.title)

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(Team,self).save(*args, **kwargs)  # save   


class ourclients(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to="img/")
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )


    
def __str__(self):
    return str(self.title)

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(ourclients,self).save(*args, **kwargs)  # save






class contactus(models.Model):
    title=models.CharField(max_length=200)
    map=models.URLField(max_length=300)
    address=models.CharField(max_length=200)
    linkcontact=models.URLField(max_length=300)
    phone=PhoneNumberField( verbose_name=_("phone"),null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )


    
def __str__(self):
    return str(self.title)





def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(contactus,self).save(*args, **kwargs)  # save
















class footer(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    titletwo=models.CharField(max_length=200)
    titlethre=models.CharField(max_length=200)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )

    
def __str__(self):
    return str(self.title)


    

    
def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(footer,self).save(*args, **kwargs)  # save




class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    
    

def __str__(self):
    return str(self.email)


    

    
  # save