# Generated by Django 4.0.4 on 2022-05-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=100, verbose_name='Unterrubrik')),
                ('publication_date', models.CharField(max_length=100, verbose_name='Veröffentlichungsdatum')),
                ('publication_number', models.CharField(max_length=100, verbose_name='Meldungsnummer')),
                ('language', models.CharField(max_length=100, verbose_name='Sprache')),
                ('canton', models.CharField(max_length=100, verbose_name='Kanton')),
                ('title', models.CharField(max_length=100, verbose_name='Titel')),
                ('company', models.CharField(max_length=100, verbose_name='Firma')),
                ('street', models.CharField(max_length=100, verbose_name='Strasse')),
                ('house_number', models.CharField(max_length=100, verbose_name='Hausnummer')),
                ('zip_code', models.CharField(max_length=100, verbose_name='PLZ')),
                ('town', models.CharField(max_length=100, verbose_name='Ort')),
                ('company_number', models.CharField(max_length=100, verbose_name='Firmennummer')),
                ('contact_point', models.CharField(max_length=100, verbose_name='Kontaktstelle')),
                ('purpose', models.CharField(max_length=100, verbose_name='Zweck')),
                ('first_name', models.CharField(max_length=100, verbose_name='Vorname')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nachname')),
                ('home_town', models.CharField(max_length=100, verbose_name='Heimatort')),
                ('residence', models.CharField(max_length=100, verbose_name='Wohnort')),
                ('function', models.CharField(max_length=100, verbose_name='Funktion')),
                ('drawing_style', models.CharField(max_length=100, verbose_name='Zeichnungsart')),
            ],
        ),
    ]