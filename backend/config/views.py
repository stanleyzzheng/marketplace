from django.http import HttpResponse


def send_the_homepage(request):
    theIndex = open("static/index.html").read()
    return HttpResponse(theIndex)


#  checking something really quick..
