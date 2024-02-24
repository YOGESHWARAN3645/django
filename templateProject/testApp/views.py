from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    time = datetime.datetime.now()
    date={'insert_date':time}
    
    return render(request,'testApp/wish.html',context=date)

def result(request):
    name='yogesh'
    rollno='9231'
    marks='100'
    student={'name':name,'rollno':rollno,'marks':marks}
    return render(request,'testApp/results.html',context=student)