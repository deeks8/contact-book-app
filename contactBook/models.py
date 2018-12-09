from django.db import models

class Contact(models.Model):
    ContactId = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    EmailId = models.CharField(max_length=100, null=False, blank=False,unique=True)
    PhoneNumber = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return str(self.Name)
