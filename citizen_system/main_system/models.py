import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models


class CitizensGroup(models.Model):
    """
    Group of citizens model.
    """
    import_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'CitizensGroup. Import id: {self.import_id}'


class Citizen(models.Model):
    """
    Citizen model.
    """

    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [(MALE, MALE), (FEMALE, FEMALE)]

    citizen_id = models.IntegerField()
    town = models.TextField('Town, where citizen lives')
    street = models.TextField('Street on which citizen lives')
    building = models.TextField('Number of building')
    apartment = models.IntegerField('Number of flat')
    name = models.TextField('Name of citizen')
    birth_date = models.DateField('Birth date')
    gender = models.TextField('Gender', choices=GENDER_CHOICES)
    relatives = ArrayField(models.IntegerField(), blank=True)
    import_group = models.ForeignKey(CitizensGroup, on_delete=models.CASCADE, null=True, to_field='import_id')
    age = models.IntegerField(default=0, editable=False)

    class Meta:
        unique_together = ('import_group', 'citizen_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count_age()

    def count_age(self):
        """
        Count and set field age by now.
        """
        today = datetime.date.today()
        self.age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return f'{self.citizen_id}: {self.name}'
