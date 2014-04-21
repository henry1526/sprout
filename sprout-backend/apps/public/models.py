from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

###
### The below @receiever is a Python decorator. Decorators can alter the way
### that methods work. This one in particular listens for anytime a User object is
### saved, and if it is just being created, it creates a new security token associated
### with that user. These tokens are used for the REST Framework, and allow us to 
### track who is logged in and allow different permissions per user
###
###

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


###
### Below is an example of a model. Uncomment to see it in action.
### When you create a new model, you must create a new schema migration
### [ python manage.py schemamigration __YOUR-APP-NAME__ --auto ]
### Once the migration is created, you then have to apply it with:
### [ python manage.py migrate ]
###

# class Address(models.Model):
#     ''' Model features for an address '''
#     street = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     state = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)

#     def __unicode__(self):
#         return u'%s, %s, %s' % (self.street, self.city, self.state)

#     class Meta:
#         verbose_name_plural = 'Addresses'

class Item(models.Model):
    part_no = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    item_type_id = models.IntegerField()
    template_id = models.IntegerField()
    is_inventory = models.BooleanField()
    is_figure_cost = models.BooleanField()
    is_warehouse = models.BooleanField()
    is_active = models.BooleanField()
    is_template = models.BooleanField()
    is_direct_cost = models.BooleanField()
    is_update = models.BooleanField()
    supplier_id = models.IntegerField()
    mpn = models.CharField(max_length=50)
    cost = models.IntegerField()
    purchase_amt = models.IntegerField()
    purchase_unit_id = models.IntegerField()
    dens_num = models.IntegerField()
    dens_num_unit_id = models.IntegerField()
    dens_den_unit_id = models.IntegerField()
    drawings = models.CharField(max_length=50)
#    thumbnail = models.ImageField()
    attribute_id_1 = models.IntegerField()
    attribute_id_2 = models.IntegerField()
    attribute_id_3 = models.IntegerField()
    attribute_type_id_1 = models.IntegerField()
    attribute_type_id_2 = models.IntegerField()
    attribute_type_id_3 = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    depth = models.IntegerField()
    weight = models.IntegerField()
    revision_id = models.IntegerField()
    lead_time = models.IntegerField()
    create_date = models.DateTimeField()
    moq = models.IntegerField()
    demand_qrt = models.IntegerField()
    min_on_hand = models.IntegerField()
    min_ord_freq = models.IntegerField()
    demand_dly = models.IntegerField()
    low_point = models.IntegerField()
    reorder_point = models.IntegerField()
    reorder_qty = models.IntegerField()
    description = models.CharField(max_length=50)
    is_recomb = models.BooleanField()
    recomb_ratio = models.IntegerField()
    common_name = models.CharField(max_length=50)
    inventory_scaler = models.IntegerField()
    volume = models.IntegerField()
#    image_line = models.???         #==== What is this for? ====#
#    timestamp = models.???          #==== What is this for? ====#
    transfer_sheet_id = models.IntegerField()
    color = models.CharField(max_length=50)
    critical_features = models.CharField(max_length=50)