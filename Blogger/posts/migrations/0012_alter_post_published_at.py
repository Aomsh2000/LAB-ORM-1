# Generated by Django 5.1.2 on 2024-11-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]