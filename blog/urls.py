from django.urls import path


from .views import post_list, post_detail
from .views import Book_list
from .views import greet
from django.conf import settings
from django.conf.urls.static import static


app_name='blog'

urlpatterns = [
      
      path("Book_list/",Book_list),
      path("contact/",greet),
      

      # post views
      path("",post_list, name='home'),
      path("<int:year>/<int:month>/<int:day>/<slug:post>/",post_detail, name='post_detail')

]
if settings.DEBUG:
      urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
