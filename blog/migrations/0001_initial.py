# Generated by Django 2.0.2 on 2018-04-17 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
