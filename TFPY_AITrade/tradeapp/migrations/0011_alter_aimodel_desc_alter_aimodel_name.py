# Generated by Django 4.0.3 on 2022-05-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0010_alter_aimodel_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aimodel',
            name='desc',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='aimodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
