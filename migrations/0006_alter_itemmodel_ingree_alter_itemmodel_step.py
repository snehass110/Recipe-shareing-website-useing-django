# Generated by Django 5.0 on 2024-02-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsapp', '0005_alter_itemmodel_image_alter_itemmodel_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='ingree',
            field=models.CharField(max_length=1100),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='step',
            field=models.CharField(max_length=3000),
        ),
    ]