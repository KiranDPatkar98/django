# Generated by Django 4.2.7 on 2023-11-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_alter_reciepe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepe',
            name='image',
            field=models.ImageField(upload_to='reciepe/'),
        ),
    ]
