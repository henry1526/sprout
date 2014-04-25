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
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    glycemic_index = models.IntegerField()

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField('Ingredient')
    cook_time = models.CharField(max_length=50)
    COOK_METHODS = (
        ('bake', 'Bake in the Oven'),
        ('microwave', 'Microwave'),
        ('fry', 'Frying Pan'),
        ('dutch_oven', 'Dutch Oven'),
    )
    cook_method = models.CharField(max_length=50, choices=COOK_METHODS)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Template(models.Model):
    part_no = models.CharField(max_length=50)
    item_id = models.IntegerField()
    attribute1 = models.CharField(max_length=50)
    attribute2 = models.CharField(max_length=50)


class Color(models.Model):
    name = models.CharField(max_length=50)


class Material(models.Model):
    name = models.CharField(max_length=50)


class Revision(models.Model):
    pass


class Supplier(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    material = models.ForeignKey("Material") # Logs what material this supplier is responsible for.


class ItemType(models.Model):
    name = models.CharField(max_length=50)
    is_template = models.BooleanField()
    is_recoup = models.BooleanField()
    is_inventory = models.BooleanField()
    abb = models.CharField(max_length=50)
    # qb_parent_account = models.CharField(max_length=50)
    # qb_cogs_account =
    # qb_asset_account =
    # qb_sales_account =
    # qb_track_qty =
    # qb_force_val =
    # exp_to_qb =
    # timestamp = models.? #==== What is this for? TimeField or DateTimeField?====#
    is_non_inventory_item = models.BooleanField()

class AttributeType(models.Model):
    name = models.CharField(max_length=50)

    #Color: blue
    #Color: white
    #Color: gray
    #Material: leather
    #Thickness: really really thick
    #Print: True