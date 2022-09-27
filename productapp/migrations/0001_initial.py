# Generated by Django 4.0.6 on 2022-09-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('catImage', models.ImageField(upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product')),
                ('category', models.ManyToManyField(to='productapp.categorymodel')),
            ],
        ),
    ]