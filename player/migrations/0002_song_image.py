# Generated by Django 4.0.2 on 2022-03-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default='idea.png', upload_to=''),
        ),
    ]