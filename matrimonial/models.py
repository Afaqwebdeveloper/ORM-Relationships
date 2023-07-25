from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Religion(models.Model):
    name =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Religion"
    def __str__(self): 
        return self.name
    
    
class Sect(models.Model):
    name =models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Sect"
    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='sects')  
    def __str__(self): 
        return self.name 


class Caste(models.Model):
    name =models.CharField(max_length=100)    
    class Meta:
        verbose_name_plural="Caste"
    def __str__(self): 
        return self.name    
        

class hobby(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="hobbies"
    def __str__(self): 
        return self.name    
         
    
class Father(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural="Father"
    occupation=models.CharField(max_length=100,null=True)   
    def __str__(self): 
        return self.name     


class Profile(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(null=True, blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation=models.CharField(max_length=100,null=True)
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    email=models.EmailField(max_length=254, unique=True)

    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='profiles',null=True)
    Sect=models.ForeignKey(Sect, on_delete=models.CASCADE, related_name='profiles',null=True)
    caste=models.ForeignKey(Caste, on_delete=models.CASCADE, related_name='profiles',null=True)
    hobbies= models.ManyToManyField(hobby,related_name='profiles',null=True)
    father=models.OneToOneField(Father,on_delete=models.CASCADE,related_name='dependent',null=True)
    
    def save(self, *args, **kwargs):
        print(f"Data Updated for{self.name}")
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.name 
        
