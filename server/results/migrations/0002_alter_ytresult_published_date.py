# Generated by Django 3.2.7 on 2021-09-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ytresult',
            name='published_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
