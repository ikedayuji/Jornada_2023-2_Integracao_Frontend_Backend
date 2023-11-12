# Generated by Django 4.2 on 2023-10-31 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alimentacao_asfalto_elevador2_empregado_esteira_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mongo_id', models.BigIntegerField()),
                ('timestamp', models.DateTimeField()),
                ('company_id', models.CharField(max_length=128)),
                ('machine_id', models.SmallIntegerField()),
                ('sensor_id', models.SmallIntegerField()),
                ('value', models.FloatField()),
            ],
        ),
    ]