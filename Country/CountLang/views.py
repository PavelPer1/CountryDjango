from django.core.paginator import Paginator
from django.shortcuts import render
from .models import CountLang


def about(request):
    return render(request, 'Countlang/about.html', {'title': 'О мне'})


def country_add(request):
    abz = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array_now = []
    array = CountLang.objects.all()
    for item in array:
        array_now += [item.country]

    paginator = Paginator(array_now, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    array1 = {
        'array': array_now,
        'title': 'Countries',
        'mas': abz,
        'page_object': page_obj
    }

    return render(request, 'Countlang/CountryAdd.html', array1)


def country_lang(request, url_country):
    abz = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array_now = []
    b = 0
    array = CountLang.objects.all()
    if url_country in abz:
        for i in array:
            if str(i.country)[0] == url_country:
                array_now += [i.country]

        paginator = Paginator(array_now, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        array1 = {
            'title': url_country,
            'array': array_now,
            'mas': abz,
            'page_object': page_obj
        }
        return render(request, 'Countlang/CountryAdd.html', array1)
    else:
        for i in array:
            if i.country == url_country:
                b = i.language
        array1 = {
            'title': url_country,
            'array': b,
        }
        return render(request, 'Countlang/language_add.html', array1)


def language(request):
    abz = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array_now = []
    array_now_2 = []
    b = ''
    array = CountLang.objects.all()
    for i in array:
        b = str(i.language)
        array_now = b.split(', ')
        for j in array_now:
            if j not in array_now_2:
                array_now_2 += [j]

    array_now_2 = set(array_now_2)
    array_now_2 = sorted(array_now_2)
    paginator = Paginator(array_now_2, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    array1 = {
        'title': 'Языки',
        'array': array_now_2,
        'mas': abz,
        'page_object': page_obj
    }
    return render(request, 'Countlang/language.html', array1)


def language_count_add(request, url_language):
    abz = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array_now = []
    array_now_2 = []
    array_now_3 = []
    b = ''
    array = CountLang.objects.all()
    if url_language in abz:
        for i in array:
            b = str(i.language)
            array_now = b.split(', ')
            for j in array_now:
                if j not in array_now_2:
                    array_now_2 += [j]

        array_now_2 = set(array_now_2)
        array_now_2 = sorted(array_now_2)
        for j in array_now_2:
            if url_language == j[0]:
                array_now_3 += [j]

        paginator = Paginator(array_now_3, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        array1 = {
            'title': url_language,
            'array': array_now_3,
            'mas': abz,
            'page_object': page_obj
        }
        return render(request, 'Countlang/language.html', array1)
    else:
        for i in array:
            if url_language in i.language:
                b += i.country + ', '
        b = b[:-2]
        array1 = {
            'title': url_language,
            'array': b
        }
        return render(request, 'Countlang/LangCount.html', array1)