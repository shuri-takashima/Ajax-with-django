# Generated by Django 3.2 on 2021-04-20 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample2', '0002_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]
