# Generated by Django 3.1.7 on 2021-03-30 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revistas', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='revistaAssociada',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='revistas.revista'),
        ),
    ]
