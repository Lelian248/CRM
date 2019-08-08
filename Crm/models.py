from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    seconed_name = models.CharField(max_length=30)
    number = models.IntegerField()
    employee = models.ForeignKey('Empolyee', on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s" % (self.first_name ,self.seconed_name)


    class Meta:
        ordering=('name')


class Service(models.Model):
    headline = models.CharField(max_length=50)
    pub_date =models.DateField()
    customer = models.ManyToManyField(Customer)

    def __str__(self):
        self.headline

    class Meta:
        ordering=('headline')

class Empolyee(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField()
    service = models.ManyToManyField(Service)


    def __str__(self):
        self.name







