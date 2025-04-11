# from django.db import models

# class Patient(models.Model):
#     GENDER_CHOICES = [
#         ('erkak', 'Erkak'),
#         ('ayol', 'Ayol'),
#     ]

#     royhatga_olingan_sana = models.DateField(verbose_name="Ro'yhatga olingan sana")
#     tugallangan_sana = models.DateField(verbose_name="Tugallangan sana")
#     tibbiy_muassasa_nomi = models.CharField(max_length=255, verbose_name="Tibbiy muassasa nomi")
#     fish = models.CharField(max_length=255, verbose_name="FISH")
#     jinsi = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Jinsi")
#     pasport_jshshir = models.CharField(max_length=30, verbose_name="Pasport JSHSHIR")
#     yosh = models.PositiveIntegerField(verbose_name="Yosh")
#     manzil = models.TextField(verbose_name="Manzil")
#     kasallik_turi = models.CharField(max_length=255, verbose_name="Kasallik turi")
#     davolovchi_shifokor = models.CharField(max_length=255, verbose_name="Davolovchi shifokor ismi")
#     bolim_boshligi = models.CharField(max_length=255, verbose_name="Bo‘lim boshlig‘i ismi")

#     def __str__(self):
#         return self.fish

from django.db import models
import random

class Spravka(models.Model):
    ROLES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    royxat_sana = models.DateField(verbose_name="Ro'yxatga olingan sana")
    tugash_sana = models.DateField(verbose_name="Tugallangan sana")
    muassasa_nomi = models.CharField(max_length=255)
    fish = models.CharField(max_length=255)
    jinsi = models.CharField(max_length=10, choices=ROLES)
    jshshir = models.CharField(max_length=14)
    yosh = models.PositiveIntegerField()
    manzil = models.TextField()
    kasallik_turi = models.CharField(max_length=255)
    shifokor = models.CharField(max_length=255)
    bolim_boshligi = models.CharField(max_length=255)

    parol = models.CharField(
        max_length=4,
        unique=True,
        blank=True,
        help_text="4 xonali raqamli parol. Agar kiritilmasa, avtomatik yaratiladi."
    )

    def save(self, *args, **kwargs):
        if not self.parol:
            self.parol = self.generate_unique_parol()
        super().save(*args, **kwargs)

    def generate_unique_parol(self):
        while True:
            random_code = f"{random.randint(0, 9999):04d}"
            if not Spravka.objects.filter(parol=random_code).exists():
                return random_code

    def __str__(self):
        return f"{self.fish} ({self.parol})"
