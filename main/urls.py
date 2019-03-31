from django.urls import include, path
from .views import *
urlpatterns = [
	path('projects/', PostListView.as_view(), name="proj_home"),
    path('home/', home, name="user_reg"),
    path('project/<int:pk>/',PostDetailView.as_view(), name="proj-content"),
    path('project/new/',PostCreateView.as_view(), name="proj-ccreate"),
    #path('project/<int:pk>/delete/',PostDeleteView.as_view(), name="proj-delete"),
    path('project/add/', show, name = "proj-add"),

    path('project/show/',display, name="proj-show"),
    #path('book/email/',email,name="send-email"),
    #path('book/don/',useless,name="useless"),
    #path('book/<int:pk>/delete/', delete, name = "delete"),
]