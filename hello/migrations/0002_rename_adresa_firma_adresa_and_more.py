# Generated by Django 4.2.3 on 2023-07-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firma',
            old_name='Adresa',
            new_name='adresa',
        ),
        migrations.RenameField(
            model_name='firma',
            old_name='Datum_reg',
            new_name='datum_reg',
        ),
        migrations.RenameField(
            model_name='firma',
            old_name='Djelatnost',
            new_name='djelatnost',
        ),
        migrations.RenameField(
            model_name='firma',
            old_name='Podrucna_Jedinica',
            new_name='podrucna_Jedinica',
        ),
    ]
