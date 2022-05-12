# Generated by Django 4.0.3 on 2022-05-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_contacto', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
    ]
