from django.urls import path
from . views import *
urlpatterns=[path('',index),
             path('login/',login),
             path('register/',register),
             path('success/',success),
             path('send/',send_mail_register),
             path('error/',error),
             path('verify/<auth_token>',verify),
             path('login2/',login2),
             path('register2/',register2),
             path('add/<int:id>',add),
             path('view/<int:id>',view),
             path('update/<int:id>',update),
             path('delete/<int:id>',delete),
             path('view2/',view2),
             path('details/<int:id>',details),
             path('mail/<int:id>',emails),
             path('review/<int:id>',review),
             path('viww/',viww),
             path('viww2/',viww2),
             path('show_review/<int:id>',show_review),
             # path('save/<int:item_id>/', save_item, name='save_item')
             path('feedback/',feedback)


             ]
