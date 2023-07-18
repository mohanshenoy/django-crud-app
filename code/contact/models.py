from django.db import models

class Contact(models.Model):  
    firstname = models.CharField(max_length=100)  
    lastname = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)  
    mobile = models.IntegerField()  
    age = models.IntegerField()  
    class Meta:  
        db_table = "contact"  	
