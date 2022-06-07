from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Data(models.Model):
    sub_category = models.CharField(max_length=100, verbose_name='Unterrubrik')
    publication_date = models.CharField(max_length=100, verbose_name='Veröffentlichungsdatum')
    publication_number = models.CharField(max_length=100, verbose_name='Meldungsnummer')
    language = models.CharField(max_length=100, verbose_name='Sprache')
    canton = models.CharField(max_length=100, verbose_name='Kanton')
    title = models.CharField(max_length=100, verbose_name='Titel')
    company = models.CharField(max_length=100, verbose_name='Firma')
    street = models.CharField(max_length=100, verbose_name='Strasse')
    house_number = models.CharField(max_length=100, verbose_name='Hausnummer')
    zip_code = models.CharField(max_length=100, verbose_name='PLZ')
    town = models.CharField(max_length=100, verbose_name='Ort')
    company_number = models.CharField(max_length=100, verbose_name='Firmennummer')
    contact_point = models.CharField(max_length=100, verbose_name='Kontaktstelle')
    purpose = models.TextField(verbose_name='Zweck')
    first_name = models.CharField(max_length=100, verbose_name='Vorname')
    last_name = models.CharField(max_length=100, verbose_name='Nachname')
    home_town = models.CharField(max_length=100, verbose_name='Heimatort')
    residence = models.CharField(max_length=100, verbose_name='Wohnort')
    function = models.CharField(max_length=100, verbose_name='Funktion')
    drawing_style = models.CharField(max_length=100, verbose_name='Zeichnungsart')

    def __str__(self):
        return self.title
    
