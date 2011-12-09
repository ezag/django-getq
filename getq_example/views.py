from django.core.paginator import Paginator
from django.shortcuts import render_to_response

def get_items(sort_index=0, reverse=False):
    items = (
        ("Eraserhead", 1977),
        ("Elephant Man, The", 1980),
        ("Dune", 1984),
        ("Blue Velvet", 1986),
        ("Wild at Heart", 1990),
        ("Fire Walk with Me", 1992),
        ("Lost Highway", 1997),
        ("Straight Story, The", 1999),
        ("Mulholland Drive", 2001),
        ("Inland Empire", 2006),
    )
    return sorted(items, key=lambda i: i[sort_index], reverse=reverse)

def index(request):
    try:
        sort_index = int(request.GET.get('sort'))
    except (TypeError, ValueError):
        sort_index = 0
    else:
        sort_index = min(max(sort_index, 0), 1)
    reverse = (request.GET.get('order') == 'desc')
    items = get_items(sort_index, reverse)
    items_per_page = 3
    p = Paginator(items, items_per_page)
    try:
        page = int(request.GET.get('page'))
    except (TypeError, ValueError):
        page = 1
    else:
        page = min(max(page, 1), p.num_pages)
    return render_to_response('getq_example.html', {
        'items': p.page(page).object_list,
        'page_range': p.page_range,
        'current_page': page,
        'sort_index': sort_index,
        'reverse': reverse,
    })
