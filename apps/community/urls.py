from core.urls import viewset_path
from apps.community.views import PostViewSet, CommentViewSet


urlpatterns = [
    viewset_path(PostViewSet, "post"),
    viewset_path(CommentViewSet, "comment"),
]