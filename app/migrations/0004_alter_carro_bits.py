# Generated by Django 4.1.7 on 2023-02-16 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_carro_bits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='bits',
            field=models.BinaryField(default=b'x08', max_length=1000),
        ),
    ]
