# Generated by Django 2.2.3 on 2019-12-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserregisterModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('doj', models.DateField(auto_now_add=True)),
            ],
        ),
    ]