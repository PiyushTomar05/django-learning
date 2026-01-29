from django.shortcuts import render


def index(request):
   peoples=[
       {'name': 'Piyush', 'age': 20, 'gender': 'Male'},
       {'name': 'Rohan', 'age': 14, 'gender': 'Male'},
       {'name': 'Sandeep', 'age': 21, 'gender': 'Male'},
       {'name': 'Anjali', 'age': 19, 'gender': 'Female'},
       {'name': 'Priya', 'age': 22, 'gender': 'Female'},
   ]

   return render(request, 'index.html',context={'peoples':peoples})