# Ex.05 Design a Website for Server Side Processing
## Date:

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :



    <html>
    <head>
        <style>
            h1{

                color: red;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                text-align: center;
                
                }
            .edge {
                 width: 1080px;       
                margin-left: auto;
                margin-right: auto;
                padding-top: 200px;
                padding-left: 300px;
}
            .box {
                display:block;
                border: Thick dashed lime;
                width: 500px;
                min-height: 300px;
                font-size: 20px;
                background-color: pink;
}
            .formelt{
                color: Red;
                text-align: center;
                margin-top: 5px;
                margin-bottom: 5px;
            }

        </style>

    </head>
    <body bgcolor="blue">
        <div class="edge">
        <div class="box">
        <h1>Area of Cylinder</h1>
        <form method="POST">
        {% csrf_token %}
        <div class="formelt">
        length : <input type="text" name="length" value="{{l}}"></input>(in m)<br/>
        </div>
        <div class="formelt">
        radius : <input type="text" name="radius" value="{{r}}"></input>(in m)<br/>
        </div>
        <div class="formelt">
            <input type="submit" value="Calculate"></input><br/>
        </div>
        <div class="formelt">
            
            Area: <input type="text" name="radius" value="{{area}}"></input>m<sup>2</sup><br/>
        </div>

        </form>

        </div>
        </div>
    </body>
    </html>



## SERVER SIDE PROCESSING:

## Views.py:
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


## urls.ppy

from django.contrib import admin
from django.urls import path
from app5 import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('areaofcylinder/',views.cyndarea,name="AreaofCylinder"),
    path('',views.cyndarea,name="AreaofCylinderroot")
]


## HOMEPAGE:
![alt text](<Screenshot 2024-04-17 171919.png>)

## RESULT:
The program for performing server side processing is completed successfully.
