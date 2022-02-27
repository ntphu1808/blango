from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter # add routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from blog.api.views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #used for JSON Web Token


router = DefaultRouter()
router.register("tags", TagViewSet) #register the paths for Tags api view
router.register("posts", PostViewSet) #register the paths for Post api view

#we can customise the url name of router.register by passing it the third argument router.register("posts", PostViewSet, basename)

urlpatterns = [
    # path("posts/", PostList.as_view(), name="api_post_list"), These two lines are replaced by the router.register("posts", PostViewSet)
    # path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"), #user detail path with the argument by email
    path("auth/", include("rest_framework.urls")),   #add the authentication link.
    path("token-auth/", views.obtain_auth_token), #used for generating a token for clients
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"), #used for authentication first and then obtain the token
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"), #used for refresh the access token
]

urlpatterns = format_suffix_patterns(urlpatterns)

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)
urlpatterns += [   # used for swagger UI
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns += [
    path("", include(router.urls)), #used for routers
    path(      #used for url-based filtering
        "posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
]

