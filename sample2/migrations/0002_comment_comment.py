# Generated by Django 3.2 on 2021-04-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Comment',
            field=models.CharField(default=4.0, max_length=100),
            preserve_default=False,
        ),
    ]
