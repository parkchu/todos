# Generated by Django 3.0.3 on 2020-03-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20200303_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]