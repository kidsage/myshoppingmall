from django.db import models

from core.models import BaseModel
from apps.users.models import User
# from apps.community.utils import user_directory_path


class Post(BaseModel):
    def get_image_path(self, filename): 
        # 'self' will work, because Django is explicitly passing it.
        return f'{self.writer}/{filename}' 

    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to=get_image_path)


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='klass')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')