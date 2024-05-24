from django.urls import path
from . import views

urlpatterns = [
       path("",views.createbook),
    path("detailedview/<int:book_id>/",views.detailedview,name='details'),
    path("updatebook/<int:book_id>/",views.updatebook,name='update'),
    path('author/',views.createauthor,name='author'),
    path("deletebook/<int:book_id>/",views.deletebook,name='delete'),
]
    
