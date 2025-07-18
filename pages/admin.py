from django.contrib import admin
from .models import PageContent, OchiqMalumot # OchiqMalumotni ham import qiling

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page_type', 'title', 'file', 'image')
    list_filter = ('page_type',)
    search_fields = ('page_type', 'content', 'title', 'description')

    fieldsets = (
        (None, {
            'fields': ('page_type', 'content'),
        }),
        # Bu bo'limlar endi PageContent ichidagi ochiq_malumotlar uchun kamdan-kam ishlatiladi.
        # Agar siz PageContent ichida ochiq_malumotlar joylashmasligiga amin bo'lsangiz,
        # bu fieldsets bo'limlarini PageContentAdmin dan olib tashlashingiz mumkin.
        ('Ochiq Ma\'lumotlar uchun (faqat bitta turdagi kontent uchun)', {
            'classes': ('collapse',),
            'fields': ('title', 'description', 'file', 'image'),
            'description': 'Bu maydonlar faqat "Ochiq Ma\'lumotlar Sahifasi (Umumiy)" turidagi kontent uchun. Bir nechta ma\'lumot uchun OchiqMa\'lumot modelini ishlating.'
        }),
        ('Biz Haqimizda uchun', {
            'classes': ('collapse',),
            'fields': ('company_info',),
            'description': 'Bu maydon faqat "Biz Haqimizda" sahifasi uchun to\'ldiriladi.'
        }),
    )

# OchiqMalumot modelini ro'yxatdan o'tkazamiz
@admin.register(OchiqMalumot)
class OchiqMalumotAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'file', 'image')
    list_filter = ('published_date',)
    search_fields = ('title', 'description')
    ordering = ('-published_date',)