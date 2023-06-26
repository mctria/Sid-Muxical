from django.urls import path
from .views import contact, home,podcasts,about,privacy, signin, terms, signout

# Create Your Urls Here

urlpatterns = [
    path('',home,name='home'),
    path('podcasts',podcasts,name="pod"),
    path('podcasts/<int:id>-<str:name>',podcasts,name='podcasts'),
    path('about-us',about,name='about'),
    path('contact',contact,name="contact"),

    # Login Logout Operation
    path('login',signin,name="login"),
    path('signout',signout,name="logout"),

    # path('add',add,name="add"),

    # Links

    path('privacy-policy',privacy,name="privacy"),
    path('terms-and-conditions',terms,name="terms"),
]
