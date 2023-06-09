# Generated by Django 4.2.1 on 2023-07-12 12:58

import apps.community.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default=1, upload_to=apps.community.models.Post.get_image_path
            ),
            preserve_default=False,
        ),
    ]
