from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("reg/", views.register, name="register"),
    path("save/", views.save_reg, name="save"),
    path("login/", views.login_page, name="login"),
    path("check/", views.check, name='check'),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout_page, name="logout"),
    path('mails/', views.mails, name='mails_page'),
    path('inbox/', views.inbox, name='inbox'),
    path('drafts/', views.draft_mails, name='drafts'),
    path('sent/', views.sent_mails, name="sent"),
    path('spam/', views.spam_mails, name='spam'),
    # path('cancel/', views.cancel_mails, name="cancel"),
]
