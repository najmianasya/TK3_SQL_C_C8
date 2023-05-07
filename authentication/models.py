from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('mahasiswa', 'Mahasiswa'),
    ('dosen', 'Dosen'),
    ('tendik', 'Tendik'),
    ('alumni', 'Alumni'),
    ('umum', 'Umum'),
)

class Panitia(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.username
