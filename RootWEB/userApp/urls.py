from django.urls    import path , include
from userApp       import views
#from RootWEB.userApp      import views

urlpatterns = [
    # http://127.0.0.1:8000/user/index
    path('index/',          views.index , name = 'index'),
    path('login/',          views.login),
    path('list/' ,          views.list),
    path('detail/',         views.detail),
    path('registerForm/',   views.registerForm),
    path('join/',           views.join),
    path('join/',           views.logout),

]
