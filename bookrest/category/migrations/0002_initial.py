# Generated by Django 3.2.6 on 2021-08-08 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='대출회원'),
        ),
        migrations.AddField(
            model_name='bookwhere',
            name='book_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.bookclassinfo'),
        ),
        migrations.AddField(
            model_name='bookclassinfo',
            name='borrows',
            field=models.ManyToManyField(blank=True, null=True, related_name='borrow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookclassinfo',
            name='wishes',
            field=models.ManyToManyField(blank=True, null=True, related_name='wish', to=settings.AUTH_USER_MODEL),
        ),
    ]
