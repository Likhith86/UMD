# Generated by Django 4.0.3 on 2022-04-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0009_requestmodel_purpose_requestmodel_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
