from django.db import models

status=(
    ('approve','APPROVED'),
    ('pending','PENDING')
)
class inventory(models.Model):
    ProductId=models.IntegerField()
    ProductName=models.CharField(max_length=100)
    Vendor=models.CharField(max_length=100)
    MRP=models.FloatField()
    BatchNum=models.IntegerField()
    BatchDate=models.DateField()
    Quantity=models.CharField(max_length=100)
    status=models.CharField(max_length=200, choices=status, default='pending')
    def __str__(self):
        return self.ProductName
