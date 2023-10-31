# Generated by Django 4.2.6 on 2023-10-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_rename_entidad_comunicado_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('INF', 'Informatica'), ('ELE', 'Electrica'), ('MEC', 'Mecanica')], max_length=50),
        ),
    ]
