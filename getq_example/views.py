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
    return render_to_response('getq_example.html', {
        'items': get_items(),
    })
