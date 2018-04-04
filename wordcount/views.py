from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.POST['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}
    
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add
            worddictionary[word] = 1
    
    
    context = {
        'fulltext': fulltext,
        'count': len(wordlist),
        'worddictionary': sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True),
    }
    
    return render(request, 'count.html', context)