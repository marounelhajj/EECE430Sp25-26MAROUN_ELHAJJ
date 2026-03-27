from django.db import models


class VolleyPlayer(models.Model):
    POSITION_CHOICES = [
        ('setter', 'Setter'),
        ('outside_hitter', 'Outside Hitter'),
        ('opposite', 'Opposite Hitter'),
        ('middle_blocker', 'Middle Blocker'),
        ('libero', 'Libero'),
        ('defensive_specialist', 'Defensive Specialist'),
    ]

    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact_person = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
