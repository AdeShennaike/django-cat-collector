from django.db import models
# add this import
from datetime import date
# Import the User
from django.contrib.auth.models import User

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# new code above

# Add the Toy model
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
      # Add the M:M relationship
    toys = models.ManyToManyField(Toy)
      # new code below
    def __str__(self):
        return self.name
      # add this new method
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
      # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='')
  
# Add new Feeding model below Cat model
class Feeding(models.Model):
  # the first optional positional argument overrides the label
  date = models.DateField('Feeding Date')  
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

def __str__(self):
# Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
# change the default sort
class Meta:
    ordering = ['-date']
    
