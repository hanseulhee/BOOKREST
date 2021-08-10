# Generated by Django 3.2.6 on 2021-08-10 06:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookclassinfo',
            name='borrows',
            field=models.ManyToManyField(blank=True, related_name='borrow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookclassinfo',
            name='wishes',
            field=models.ManyToManyField(blank=True, related_name='wish', to=settings.AUTH_USER_MODEL),
        ),
    ]