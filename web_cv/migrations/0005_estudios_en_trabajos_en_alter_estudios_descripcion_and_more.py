# Generated by Django 4.0.2 on 2022-02-16 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_cv', '0004_alter_estudios_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudios_en',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=32)),
                ('grado', models.CharField(max_length=32)),
                ('inicio', models.DateField(null=True)),
                ('fin', models.DateField(null=True)),
                ('descripcion', models.TextField(max_length=254)),
                ('i', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos_en',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=32)),
                ('puesto', models.CharField(max_length=32)),
                ('inicio', models.DateField(null=True)),
                ('fin', models.DateField(null=True)),
                ('descripcion', models.TextField(max_length=254)),
                ('i', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='estudios',
            name='descripcion',
            field=models.TextField(max_length=254),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='descripcion',
            field=models.TextField(max_length=254),
        ),
    ]