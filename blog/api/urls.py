from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views


from blog.api.views import *

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"), #user detail path with the argument by email
    path("auth/", include("rest_framework.urls")),   #add the authentication link.
    path("token-auth/", views.obtain_auth_token), #used for generating a token for clients
]

urlpatterns = format_suffix_patterns(urlpatterns)