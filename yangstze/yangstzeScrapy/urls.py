from django.conf.urls import url
from yangstzeScrapy import views

urlpatterns=[
 url(r'^$',views.HomePageView.as_view()),
 url(r'^$',views.AboutPageView.as_view()),
 url(r'^$',views.HeadlinesPageView.as_view())
]
