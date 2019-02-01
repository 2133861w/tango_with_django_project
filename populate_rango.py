import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup() #imports Django projects settings into the context of this script

from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages we want to add
    # into each category.
    # Then, we will create a dictionary of dictionaries for our categories. 
    # This might seem a little bit confusing, but it allows us to iterate through each data structure, 
    # and add the data to our models. 


    # List of Dictionaries of "Python" Category pages... Tile:value, URL:value
    python_pages = [
        {"title": "Official Python Tutorial", "url": "https://docs.python.org/2/tutorial/", "views": 1},
        {"title": "How to think like a Computer Scientist" ,"url": "http://www.greenteapress.com/thinkpython/",  "views": 2},
        {"title": "Learn python in Ten Minutes" ,"url": "https://www.korokithakis.net/tutorials",  "views": 3}
    ]

    # List of Dictionaries of "django" Category pages... Title:value, URL:value
    django_pages = [
        {"title":"Official Django Tutorial" ,"url":"https://docs.djangoprojects.com/en/1.11/intro/tutorial01/",  "views": 4},
        {"title":"Django Rocks" ,"url":"https://www.djangorocks.com",  "views": 5},
        {"title":"How to Tango with Django" ,"url":"https://tangowithdjango.com/",  "views": 6}
    ]

    # List of Dictionaries of "Other" Category pages... Title:value, URL:value
    other_pages = [
        {"title":"Bottle" ,"url":"http://bottlepy.org/docs/dev/",  "views": 7},
        {"title":"Flask" ,"url":"http://flask.pocoo.org/",  "views": 8}

    ]

    # A Dictionary of Categories. Passing the pages defined above to the "pages" attribute (making a page) and then applything the tag to which their definied
    # category. 
    cats = {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
    }

    # If you want to add more categories or pages, add them to the 
    # dictionaies above. 

    # The code below goes through the cats directory, then adds each category. 
        # and then adds all the associated pages for that category.
        # if you are using python 2.x then use cat.iteritems() see
        # https://docs.quantifiedcode.com/python-anti-patterns/readability
        # for more information about how to iterate over a dictionary properly

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p["views"])

    # Print out the categories we have added.    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
        


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango Population script...")
    populate()
