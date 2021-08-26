from django.http import HttpResponse
from django.shortcuts import render


def start(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    remove_punc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charectercounter = request.POST.get('charectercounter','off')


    if remove_punc=="on":
        Analyzed=""
        punc='''!()-{}[];:'"\,<>.?@#$%^&*~_'''
        for char in djtext:
            if char not in punc:
                Analyzed=Analyzed+char

        params={'purpose':'Remove Punctuation','Analyzed_text': Analyzed}
        djtext=Analyzed

       # return render(request,'analyze.html',params)

    if(fullcaps == "on"):
        Analyzed=""
        for char in djtext:
            Analyzed = Analyzed + char.upper()
        params = {'purpose': 'Change to Upper', 'Analyzed_text': Analyzed}
        djtext = Analyzed

        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        Analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                 Analyzed = Analyzed + char
        params = {'purpose': 'Removed New Lines', 'Analyzed_text': Analyzed}
        djtext = Analyzed

       # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        Analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                Analyzed = Analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'Analyzed_text': Analyzed}
        djtext = Analyzed

        #return render(request, 'analyze.html', params)

    if (charectercounter == "on"):
        Analyzed = ""
        for char in djtext:
            Analyzed=Analyzed+char
        params = {'purpose': 'Charecter Counted', 'Analyzed_text': Analyzed}

        #return render(request, 'analyze.html', params)

    if(remove_punc!="on" and fullcaps !="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("please select any operation and try again")



    return render(request, 'analyze.html', params)


