from django.db import models

def upload_to(instance, filename):
    return 'user_profile_image/{}/{}'.format(instance.item_id, filename)


class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=20)
    item_price = models.FloatField(max_length=20,blank=False,null=False)
    item_image = models.ImageField(upload_to=upload_to,blank=True,null=True)
    item_description = models.CharField(max_length=100,default='Basic Needs')
    item_quantity = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return "%s " % self.item_name