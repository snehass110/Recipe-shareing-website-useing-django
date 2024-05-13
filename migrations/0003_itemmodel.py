# Generated by Django 5.0 on 2024-01-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsapp', '0002_regmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='crudapp/static')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
    ]
