# Generated by Django 4.1.7 on 2023-03-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogsmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsmodel',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
