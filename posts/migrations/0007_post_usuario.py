# Generated by Django 3.1.7 on 2022-02-02 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('posts', '0006_remove_post_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
    ]
