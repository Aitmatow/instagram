# Generated by Django 2.2 on 2019-12-14 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20191214_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='image_user', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
