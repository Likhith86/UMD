# Generated by Django 4.0.3 on 2022-04-13 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0025_alter_feedbackmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinestockmodel',
            name='medicine_quantity',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
