from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Staff(models.Model):
    name = models.CharField(max_length=40)
    positon = models.CharField(max_length=40)

    def save_staff(self):
        self.save()

    def delete_staff(self):
        self.delete()
   
class Waiter(models.Model):
    name = models.CharField(max_length=40)

    def save_waiter(self):
        self.save()

    def delete_waiter(self):
        self.delete()

class Items(models.Model):
    name = models.CharField(max_length=40)
    selling_price = models.DecimalField(decimal_places=2, max_digits=20)
    buying_price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.ForeignKey(Categories)
    quantity = models.PositiveIntegerField(default=0)

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()

class Orders(models.Model):
    waiter = models.ForeignKey(Waiter)
    items = models.ForeignKey(Items,default=0)
    table_no = models.PositiveIntegerField()
    total_cost = models.DecimalField(decimal_places=2, max_digits=20)


    def save_order(self):
        self.save()

    def delete_order(self):
        self.delete()