from django.urls import path
from .views import login_page,logout_session, signup_page

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login_page, name= 'login_page'),
    path('logout/', logout_session, name= 'logout_session'),
    path('signup/', signup_page, name= 'signup_page')
]