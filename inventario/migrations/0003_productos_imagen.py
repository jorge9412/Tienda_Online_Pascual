# Generated by Django 4.0.3 on 2022-05-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_productos_id_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]