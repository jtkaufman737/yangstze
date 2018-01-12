from django.conf.urls import url
from yangstzeapp import views

urlpatterns=[
 url(r'^$',views.HomePageView.as_view()),
]
