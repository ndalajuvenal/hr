# Generated by Django 3.2.18 on 2023-03-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_hr', '0013_auto_20230308_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
