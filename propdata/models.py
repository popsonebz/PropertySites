from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator, validate_email

# Content of dropdown when selecting suburb
suburb_names = (
        ('Cowies Hill', 'Cowies Hill'),
        ('Chiltern Hills', 'Chiltern Hills'),
        ('Dawncliffe', 'Dawncliffe'),
        ('Reservoir Hills', 'Reservoir Hills'),
        ('Atholl Heights', 'Atholl Heights'),
        ('Berea West', 'Berea West'),
        ('Rooikoppies', 'Rooikoppies'),
        ('Westville', 'Westville'),
        ('Cato Manor', 'Cato Manor'),
        ('Asherville', 'Asherville'),
        ('Sherwood', 'Sherwood'),
        ('Clare Estate', 'Clare Estate')


    )

# Creating Agent Table


class Agent(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, validators=[validate_email])
    cellPhone = models.IntegerField(blank=False, validators=[MinValueValidator(1)])
    picture = models.ImageField(upload_to='pictures',blank=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        unique_together = ('first_name', 'last_name') # adding a constraint to avoid duplicated name and surname

# Creating the Listing table (HouseDetails)


class HouseDetails(models.Model):
    bedrooms = models.IntegerField(blank=False, validators=[MinValueValidator(1)])
    price = models.DecimalField(decimal_places=2, max_digits=6, validators=[MinValueValidator(0.00)])
    picture = models.ImageField(upload_to='houses',blank=False)
    description = models.TextField(blank=False)
    marketing_Heading = models.CharField(max_length=50, blank=False)
    owners_Ref_Number = models.CharField(max_length=50, blank=False)
    associated_agent = models.ForeignKey(Agent)
    suburb = models.CharField(max_length=25, choices=suburb_names)

    def __str__(self):
        return '%s' % self.owners_Ref_Number

# Creating the Leads Table


class Lead(models.Model):
    first_name = models.CharField(max_length=20,blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False, validators=[validate_email])
    address = models.TextField(blank=False)
    property = models.ForeignKey(HouseDetails)

    def __str__(self):
        return '%s' % self.email

