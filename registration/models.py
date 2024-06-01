from django.db import models

class Participant(models.Model):
    MILITARY_GRADES = [
        ('marinero', 'Marinero'),
        ('cabo', 'Cabo'),
        ('tercer maestre', 'Tercer Maestre'),
        ('segundo maestre', 'Segundo Maestre'),
        ('primer maestre', 'Primer Maestre/Guardiamarina'),
        ('teniente corbeta', 'Teniente de Corbeta'),
        ('teniente fragata', 'Teniente de Fragata'),
        ('teniente navio', 'Teniente de Navío'),
        ('capitan corbeta', 'Capitán de Corbeta'),
        ('capitan fragata', 'Capitán de Fragata'),
        ('capitan navio', 'Capitán de Navío'),
        ('contralmirante', 'Contralmirante'),
        ('vicealmirante', 'Vicealmirante'),
        ('almirante', 'Almirante'),
    ]

    grade = models.CharField(max_length=50, choices=MILITARY_GRADES)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    email = models.EmailField()
    will_attend = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.grade})'