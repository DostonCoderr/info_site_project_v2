# C:\Users\Doston\Desktop\info_site_project_v2\pages\models.py
from django.db import models

class PageContent(models.Model):
    PAGE_CHOICES = [
        ('home', 'Asosiy Sahifa'),
        ('biz_haqimizda', 'Biz Haqimizda'),
        ('ochiq_malumotlar_sahifasi', 'Ochiq Ma\'lumotlar Sahifasi (Umumiy)'), # Yangi page_type qo'shamiz
        ('manzil', 'Manzil'),
        ('aloqa', 'Aloqa'),
    ]

    page_type = models.CharField(
        max_length=50,
        choices=PAGE_CHOICES,
        unique=True,
        verbose_name="Sahifa turi"
    )

    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Sahifa kontenti (Umumiy)"
    )

    # Bu maydonlar endi PageContent ichidagi ochiq_malumotlar uchun ishlatilmaydi,
    # faqat umumiy kontent uchun ishlatilishi mumkin yoki o'chirib tashlanishi mumkin.
    # Men hozircha ularni qoldiraman, agar boshqa sahifalar uchun kerak bo'lsa.
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Sarlavha (Agar kerak bo'lsa)"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Tavsif (Agar kerak bo'lsa)"
    )
    file = models.FileField(
        upload_to='page_files/',
        blank=True,
        null=True,
        verbose_name="Fayl (Agar kerak bo'lsa)"
    )
    image = models.ImageField(
        upload_to='page_images/',
        blank=True,
        null=True,
        verbose_name="Rasm (Agar kerak bo'lsa)"
    )

    company_info = models.TextField(
        blank=True,
        null=True,
        verbose_name="Kompaniya haqida ma'lumot (Biz Haqimizda uchun)"
    )

    def __str__(self):
        return self.get_page_type_display()

    class Meta:
        verbose_name = "Sahifa kontenti"
        verbose_name_plural = "Sahifa kontentlari"

# Ochiq ma'lumotlar ro'yxati uchun alohida model
class OchiqMalumot(models.Model):
    title = models.CharField(max_length=200, verbose_name="Ma'lumot sarlavhasi")
    description = models.TextField(blank=True, null=True, verbose_name="Qisqacha tavsif")
    file = models.FileField(upload_to='ochiq_malumotlar_files/', verbose_name="Fayl")
    image = models.ImageField(upload_to='ochiq_malumotlar_images/', blank=True, null=True, verbose_name="Rasm (Agar bo'lsa)")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Ochiq Ma'lumot"
        verbose_name_plural = "Ochiq Ma'lumotlar"
        ordering = ['-published_date'] # Yangilari tepada ko'rinsin