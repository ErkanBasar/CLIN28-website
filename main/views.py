
import os

from django.shortcuts import render

def home(request):
    """Loads the Home page
    """
    if os.getenv('UNDER_CONST', 'False') == 'True':
        request = render(request, 'under_construction.html', {})
    else:
        available_pdfs = [pdf_file.split('.pdf')[0] \
                                for pdf_file in os.listdir('static/on-program') \
                                if pdf_file.endswith('.pdf')]
        request = render(request, 'base.html', {
            'title': 'Personalized Intelligent Conversational Agents Workshop',
            'keys': ('workshop, natural language processing, artificial intelligence, '
                     'machine learning, conversational agents'),
            'available_pdfs': available_pdfs
        })

    return request

def calls(request):
    """Loads the Calls page
    """
    return render(request, 'calls.html', {
        'title': 'Dates & Calls',
        'keys': ('calls, call for paper, submission, instructions, '
                'important dates, dates, abstracts'),
    })

def posters(request):
    """Loads the Gallery page where the posters are displayed

    Convert pdf to png;
    $ for i in $( ls *.pdf); do convert -verbose -density 150 -trim $i -quality 100 -flatten -sharpen 0x1.0 thumbnails/$i.png; done
    Resize the png;
    $ for i in $( ls thumbnails/*.png); do convert -geometry x200 $i $i; done
    """
    poster_paths = sorted([{'thumbnail': 'posters/thumbnails/' + poster + '.png',
                            'original': 'posters/' + poster} \
                           for poster in os.listdir('static/posters') \
                           if poster.endswith('.pdf')],
                          key=lambda k: k['original'])

    return render(request, 'posters.html', {
        'title': 'Gallery',
        'keys': 'PICA, 2021, PICA2021, posters, display posters, dowload posters',
        'poster_paths': poster_paths,
    })

def photos(request):
    """Loads the page the photos are displayed

    # Create the thumbnails (install imagemagick)
    $ for i in $( ls *.jpg); do convert -geometry x200 $i thumbnails/$i; done
    """
    photo_paths = sorted([{'thumbnail': 'images/photos/thumbnails/' + photo,
                           'original': 'images/photos/' + photo} \
                          for photo in os.listdir('static/images/photos') \
                          if photo.endswith('.jpg')],
                         key=lambda k: k['original'])

    return render(request, 'photos.html', {
        'title': 'Gallery',
        'keys': 'PICA, 2021, PICA2021, photos, photo gallery',
        'photo_paths': photo_paths,
    })

def presentations(request):
    """Loads the Presentations page

    Convert pdf to png;
    $ for i in $( ls *.pdf); do convert -verbose -density 150 -trim $i[0] -quality 100 -flatten -sharpen 0x1.0 thumbnails/$i.png; done
    Resize the png;
    $ for i in $( ls thumbnails/*.png); do convert -geometry x200 $i $i; done
    """
    presentations_paths = sorted([{'thumbnail': 'presentations/thumbnails/' + poster + '.png',
                                   'original': 'presentations/' + poster} \
                                  for poster in os.listdir('static/presentations') \
                                  if poster.endswith('.pdf')],
                                 key=lambda k: k['original'])

    return render(request, 'presentations.html', {
        'title': 'Gallery',
        'keys': 'PICA, 2021, PICA2021, presentations, presentation gallery',
        'presentations_paths': presentations_paths,
    })
