from django.db import models


class Musician(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=100, choices=SHIRT_SIZES,default="M")


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE,verbose_name="relation between musician and album")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    def baby_boomer_status(self):
        "Returns the "
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"
    @property
    def full_name(selfs):
        return  f"{selfs.first_name} {selfs.last_name}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person,through="MemberShip")

class MemberShip(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=100)


class Ox(models.Model):
    horn_length = models.IntegerField()
    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"