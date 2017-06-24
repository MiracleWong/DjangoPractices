from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
  return HttpResponse("Hello World")

def about(request, author_no):
    html = "<h2>Here is Author:{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)
def listing(request, list_date):
    html = "<h2>List Date is {}</h2><hr>".format(list_date)
    return HttpResponse(html)
def post(request, yr, mon, day, post_num):
    html = "<h2>{}/{}/{}: Post Number is: {}</h2><hr>".format(yr, mon, day, int(post_num))
    return HttpResponse(html)