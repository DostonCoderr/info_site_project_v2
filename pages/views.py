from django.shortcuts import render, get_object_or_404
from .models import PageContent, OchiqMalumot # OchiqMalumotni qayta import qiling

def home(request):
    home_content = get_object_or_404(PageContent, page_type='home')
    return render(request, 'home.html', {
        'home_content': home_content.content
    })

def ochiq_malumotlar(request):
    # Bu qatorni 'ochiq_malumotlar_sahifasi' deb o'zgartiring
    ochiq_sahifa_content = get_object_or_404(PageContent, page_type='ochiq_malumotlar_sahifasi') 

    # Barcha OchiqMalumot yozuvlarini olish
    all_ochiq_data = OchiqMalumot.objects.all().order_by('-published_date')

    for item in all_ochiq_data:
        item.is_image_file = False
        if item.file:
            file_extension = item.file.name.split('.')[-1].lower()
            if file_extension in ['png', 'jpg', 'jpeg', 'gif', 'webp']:
                item.is_image_file = True

    context = {
        'ochiq_malumotlar': all_ochiq_data, # ochiq_malumotlar_list emas, 'ochiq_malumotlar' bo'lsin
        'ochiq_sahifa_content': ochiq_sahifa_content,
    }
    return render(request, 'pages/ochiq_malumotlar.html', context)

def manzil(request):
    manzil_content = get_object_or_404(PageContent, page_type='manzil')
    return render(request, 'pages/manzil.html', {
        'manzil_content': manzil_content.content
    })

def aloqa(request):
    aloqa_content = get_object_or_404(PageContent, page_type='aloqa')
    return render(request, 'pages/aloqa.html', {
        'aloqa_content': aloqa_content.content
    })

def biz_haqimizda(request):
    biz = get_object_or_404(PageContent, page_type='biz_haqimizda')
    return render(request, 'pages/biz_haqimizda.html', {
        'biz_content': biz.content,
        'company_info': biz.company_info,
        'biz': biz,
    })