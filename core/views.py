from django.shortcuts import render, HttpResponse

html_base = '''
<h1>Web Personal<h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Porta Folio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
'''


def home(request):
    return HttpResponse(html_base + '''
        <h2>Portada</h2>
        <p>Esto es la portada</p>
    ''')


def about(request):
    return HttpResponse(html_base + '''
        <h2>Acerca de</h2>
        <p>Me llamo Luis</p>
    ''')


def portfolio(request):
    return HttpResponse(html_base + '''
        <h2>Portafolio</h2>
        <p>Contenido del portafolio</p>
    ''')


def contact(request):
    return HttpResponse(html_base + '''
        <h2>Contacto</h2>
        <p>Contenido de contacto</p>
    ''')