# Generated by Django 4.0.3 on 2022-04-13 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0026_alter_medicinestockmodel_medicine_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationmodel',
            name='medicine_quantity',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='medicinestockmodel',
            name='medicine_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='medicine_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
