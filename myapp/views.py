from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request,'home.html')

def signup(request):
    if(request.method=='POST'):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()#form when page loads
    return render(request,'signup.html',{'form':form})
