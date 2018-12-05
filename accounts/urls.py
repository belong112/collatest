from django.conf.urls import url
from . import views

app_name = 'accounts'
#name the app

urlpatterns=[
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login_views,name='login_views'),
    url(r'^logout/$',views.logout_views),
]