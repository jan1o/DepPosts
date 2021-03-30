# Generated by Django 3.1.7 on 2021-03-30 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('corpo', models.CharField(max_length=1000)),
                ('dataPublicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]