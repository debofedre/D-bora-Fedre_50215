# Generated by Django 5.0.2 on 2024-03-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_acerca_options_alter_acrónimos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acrónimos',
            name='definición',
            field=models.CharField(max_length=100),
        ),
    ]
