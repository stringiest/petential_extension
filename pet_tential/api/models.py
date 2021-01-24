from django.db import models

# Create your models here.
class Food(models.Model):
    meal_type = models.CharField(max_length=20, null=True, default="")
    date = models.DateField()
    fed_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=100, null=True, default="")
    treats = models.IntegerField(null=False, default=0)

# The __str__ method just tells Django what to print when it needs to print out an instance of the any model.
    def _str_(self):
        return self.meal_type