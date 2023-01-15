# Generated by Django 4.1.3 on 2023-01-14 23:41

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profilemodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_picture',
            field=models.ImageField(blank=True, default='users/img/UserDefaultPicture.webp', null=True, upload_to=users.models.img_upload),
        ),
    ]
