# Generated by Django 4.1.3 on 2023-01-04 21:49

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profilemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_picture',
            field=models.ImageField(default='users/img/UserDefaultPicture.webp', upload_to=users.models.img_upload),
        ),
    ]
