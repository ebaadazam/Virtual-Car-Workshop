from django.db import models

# Create your models here.
# manually
class Contact(models.Model):
    # name = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)
    # number = models.CharField(max_length=10)
    # desc = models.TextField()
    # city = models.CharField(max_length=50)
    # date = models.DateField()
    
    SERVICE_CHOICES = [
        ('car_modification', 'Car Modification'),
        ('car_repairing', 'Car Repairing'),
        ('car_detailing', 'Car Detailing'),
        ('car_washing', 'Car Washing'),
    ]
    
    name = models.CharField(("name"), max_length=50)
    email = models.CharField(("email"), max_length=50)
    number = models.CharField(("number"), max_length=10)
    service = models.CharField(("service"), max_length=255, choices=SERVICE_CHOICES, default='car modification')
    city = models.CharField(("city"), max_length=50)
    state = models.CharField(("state"), max_length=50)
    date = models.DateField(("date"), auto_now=False, auto_now_add=False)
    
     # Now we want the name of the person who submit the form not the contact_obj in database
    def __str__(self):
        return self.name