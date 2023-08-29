# I have created this file - Asad
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


# def index(request):
#     return HttpResponse ('''<h1>Asad</h1> <a href="https://careers.teradata.com/categories/1/group-1/3/it"> Django Code With Asad</a><br><br>
#                          <a href= "https://www.sai.uni-heidelberg.de/"> SAI</a><br><br>
#                          <a href= "https://www.google.com/"> GooglyGu</a><br><br>
#                          ''')

# def about(request):
#     return HttpResponse ("<p>About Asad</p> <p>Asad is a good boy<p><br><p>He eats his food on time</p>")

def index(request):
    return render(request, 'index.html')
    
    # return HttpResponse('Home')

def analyse(request):
    # Get the text
    djtext= request.GET.get('text', 'default')
    # check checkbox values
    removepunc= request.GET.get('removepunc', 'off')
    fullcaps= request.GET.get('fullcaps', 'off')
    newlineremover= request.GET.get('newlineremover', 'off')
    charcount= request.GET.get("charcount",'off')
    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analysed= ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params= {'purpose':'Removed Punctutions','analysed_text': analysed}
        return render(request, 'analyse.html', params)
    elif(fullcaps=='on'):
        analysed=""
        for char in djtext:
            analysed = analysed + char.upper()
        params= {'purpose':'Changed to Uppercase','analysed_text': analysed}
        return render(request, 'analyse.html', params)
    elif(newlineremover=='on'):
        analysed=""
        for char in djtext:
            if char != '\n':
                analysed= analysed + char
                params= {'purpose':'Removed New Lines','analysed_text': analysed}
        return render(request, 'analyse.html', params)
    elif(charcount=='on'):
        analysed=""
        djtext_without_spaces=djtext.replace(" ","")
        character_count= len(djtext_without_spaces)
        params= {'purpose':'Characters Counted','character_count':character_count,'analysed_text': analysed}
        return render(request, 'analyse.html', params)
       
    else:
        return HttpResponse('Error')

# def removepunc(request):
#     djtext= request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse('remove punc')

# def capfirst(request):
#     return HttpResponse('capitalize first')

# def newlineremove(request):
#     return HttpResponse('new line removed')

# def spaceremover(request):
#     return HttpResponse("space removed")

# def charcount(request):
#     return HttpResponse('character count')
    