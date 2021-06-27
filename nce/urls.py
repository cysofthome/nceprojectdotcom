from django.urls import path
from . import views
from .views import ( 
	ListOfProject, 
	ProjectDetailView, 
	Home, HireWriter, 
	Services,
	Payment, 
	About)

app_name = 'nce'
urlpatterns = [
	path("", Home.as_view(), name="landingpage"),
	path('contact/', views.contact,name='contact'),
    path("projectlist/", ListOfProject.as_view(), name="projectlist"),
    path('<uuid:pk>', ProjectDetailView.as_view(), name='projectdetail'),
    path("<departments>/", views.department, name="departments"),
    path('hirewriter/', HireWriter.as_view(), name='hire'),
    path('Services/', Services.as_view(), name='services'),
    path('payment/', Payment.as_view(), name='payment'),
    path('about/', About.as_view(), name='about'),

]
