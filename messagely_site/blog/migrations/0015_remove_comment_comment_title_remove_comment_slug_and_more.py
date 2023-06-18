# Generated by Django 4.1.7 on 2023-06-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_title',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
