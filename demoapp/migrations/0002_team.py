# Generated by Django 4.2.5 on 2023-10-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew', models.CharField(max_length=50)),
                ('c_img', models.ImageField(upload_to='imgs')),
                ('c_desc', models.TextField()),
            ],
        ),
    ]