# Generated by Django 4.1.7 on 2023-02-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_carro_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='bits',
            field=models.BinaryField(default=b'x08'),
        ),
    ]
