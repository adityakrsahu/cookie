
from django.shortcuts import render
from datetime import *
# Create your views here.
def set(request):
    data = render(request,'app/set.html')
    data.set_cookie('name','Aditya') # by default
    data.set_cookie('age','22') # by default
    data.set_cookie('City','bhopal')
    data.set_cookie('name','Aditya', expires=datetime.utcnow()+timedelta(days=1)) # set expire time for your cookies.
    data.set_cookie('age','22',max_age=20*60*60) # by default
    data.set_cookie('City','Bhopal',httponly=True,secure=True) # by default
    return data

def get(request):
    name = request.COOKIES['name'] 
    age = request.COOKIES['age'] 
    city = request.COOKIES['city']  
    name = request.COOKIES['city']   # through error because we do not set any cookie against this key.       
    name = request.COOKIES.get('name')
    name = request.COOKIES.get('city') # O/P---None
    name = request.COOKIES.get('city','Guest') # O/P---Guest
    name = request.COOKIES.get('city','Bhopal')
    print(name)   
    print(age)
    print(city)
    name={
        'name':name,
        'age':age,
        'city':city
    }
    return render(request,'app/get.html',{'data':name})

def delete(request):
    data = render(request,'app/delete.html')
    data.delete_cookie('name')
    data.delete_cookie('age')
    data.delete_cookie('City')
    return data

# next day

def login(request):
    emailid=request.POST['email']
    password=request.POST['password']
    
    
    email_id = request.COOKIES['email']
    pwd = request.COOKIES['password']
    
    
    if email_id == emailid and password ==pwd:
        name = request.COOKIES['fname']
        return render(request,'dashboard.html',{'data':name})