from django.db import models

class Order(models.Model):

    title = models.CharField(max_length=32)
    order_num = models.CharField(max_length=32)
    status_choices = (
        (1,'未支付'),
        (2,'已支付'),
    )
    status = models.IntegerField(choices=status_choices,default=1)
