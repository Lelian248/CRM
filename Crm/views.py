from django.shortcuts import render,get_object_or_404
from .models import Service,Customer,Empolyee
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic


class LoginView(generic.LoginView):
    #if request.method=="POST"
        #username =request.Post['username']
       # password = request.method['password']
      #  user
    pass

class SearchView(generic.SearchView):
    pass

class AddCustomerView(generic.AddCustomerView):
    pass

class AddServiceView(generic.AddServiceView):
    pass

class DeleteView(generic.DeleteView):
    pass

class ListServicesView(generic.ListServicesView):
    pass

class ListAllCustomerServicesView(generic.ListAllCustomerServicesView):
    pass

class StopServiceView(generic.StopServiceView):
    pass

class EditeView(generic.EditeView):
    pass



