from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name= models.CharField(max_length=100)
    dep_desc= models.TextField()
    
    def __str__(self):
         return self.dep_name


class Doctors(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')

    def __str__(self):
         return 'Dr' + self.doc_name + '- (' + self.doc_spec+')'
    
    
class Booking(models.Model):
     p_name=models.CharField(max_length=255)
     p_phone=models.CharField(max_length=10)
     p_email=models.EmailField()
     doc_name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
     booking_date=models.DateField()
     booked_on=models.DateField(auto_now=True)


class Doctor(models.Model):
     name=models.CharField(max_length=50)
     mobile= models.IntegerField()
     special=models.CharField(max_length=50)

     def __str__(self):
         return self.name
     
class Patient(models.Model):
     name=models.CharField(max_length=100)
     gender=models.CharField(max_length=10)
     mobile=models.IntegerField(null=True)
     address=models.CharField(max_length=200)

     def __str__(self):
         return self.name


class Appointment(models.Model):

     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
     patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
     date1=models.DateField()
     time1=models.TimeField()

     def __str__(self):
        return f"Appointment with {self.doctor} for {self.patient} on {self.date1} at {self.time1}"




     
    