# Generated by Django 4.1.5 on 2023-03-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='kufgefge', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
