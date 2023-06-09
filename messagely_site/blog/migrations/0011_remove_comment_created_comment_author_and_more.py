# Generated by Django 4.1.7 on 2023-06-16 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('draft', 'Unapproved'), ('published', 'Approved')], default='draft', help_text='Set to "Approved" to make this post publicly visible', max_length=10),
        ),
    ]
