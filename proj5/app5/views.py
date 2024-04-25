from django.shortcuts import render
import math
def cyndarea(request):
    context={}
    context['area']="0"
    context['l']="0"
    context['r']="0"
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length','0')
        r = request.POST.get('radius','0')
        print('request=',request)
        print('Length=',l)
        print('Radius=',r)
        area = 2*math.pi*float(r)*float(l) + 2*math.pi*float(r)*float(r)
        context['area'] = area
        context['l'] = l
        context['r'] = r
        print('Area=',float(area))
    return render(request,'app5/math.html',context)