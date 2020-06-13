"""guestbook URL Configuration

`urlpatterns`列表將URL路由到視圖。 有關更多信息，請參閱：
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
例如：
Function views
    1. 導入:  from my_app import views
    2. 新增URL到urlpatterns:  path('', views.home, name='home')
Class-based views
    1. 導入:  from other_app.views import Home
    2. 新增URL到urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. 導入 include() function: from django.urls import include, path
    2. 新增URL到urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django .contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/message/')),
    path('message/', include('web.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
]