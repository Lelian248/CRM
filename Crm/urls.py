from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('',views.LoginView.as_view(), name='login'),
    path('',views.SearchView.as_view(), name='search'),
    path('',views.AddCustomerView.as_view(), name='addCustomer'),
    path('',views.AddServiceView.as_view(), name='addService'),
    path('',views.DeleteView.as_view(), name='delete'),
    path('',views.ListServicesView.as_view(), name='listServices'),
    path('',views.ListAllCustomerServicesView.as_view(), name='listAllCustomerServices'),
    path('',views.StopServiceView.as_view(), name='StopService'),
    path('',views.EditeView.as_view(), name='edite'),
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),

]