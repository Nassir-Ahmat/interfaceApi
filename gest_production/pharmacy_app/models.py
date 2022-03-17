
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achat(models.Model):
    idac = models.SmallAutoField(db_column='idAc', primary_key=True)  # Field name made lowercase.
    produit = models.ForeignKey('Produit', models.DO_NOTHING)
    client = models.ForeignKey('Client', models.DO_NOTHING)
    qte = models.IntegerField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'achat'



class Categorie(models.Model):
    nom_cat = models.CharField(primary_key=True, max_length=60)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorie'


class Client(models.Model):
    idcli = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=80, blank=True, null=True)
    adresse = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'client'


class Commande(models.Model):
    id_cmd = models.SmallAutoField(primary_key=True)
    fournisseur = models.ForeignKey('Fournisseur', models.DO_NOTHING)
    date_cmd = models.DateTimeField(blank=True, null=True)
    etat = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'commande'



class Entreprise(models.Model):
    ide = models.SmallAutoField(db_column='idE', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='nomE', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'entreprise'


class Fournisseur(models.Model):
    idf = models.SmallAutoField(db_column='idF', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(max_length=70, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'fournisseur'


class LigneCmd(models.Model):
    id_li = models.SmallAutoField(primary_key=True)
    commande = models.ForeignKey(Commande, models.DO_NOTHING)
    produit = models.ForeignKey('Produit', models.DO_NOTHING)
    qte = models.IntegerField(blank=True, null=True)
    prix = models.IntegerField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ligne_cmd'


class Produit(models.Model):
    idpro = models.SmallAutoField(primary_key=True)
    designation = models.CharField(max_length=70, blank=True, null=True)
    categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='categorie', blank=True, null=True)
    qte = models.IntegerField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)
    fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING, db_column='fournisseur')
    entreprise = models.ForeignKey(Entreprise, models.DO_NOTHING, db_column='entreprise')
    emplacement = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'produit'


class Reception(models.Model):
    idr = models.SmallAutoField(db_column='idR', primary_key=True)  # Field name made lowercase.
    commande = models.ForeignKey(Commande, models.DO_NOTHING)
    produit = models.ForeignKey(Produit, models.DO_NOTHING)
    qte_livre = models.IntegerField(blank=True, null=True)
    date_livree = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reception'


class StkEntre(models.Model):
    id_entre = models.SmallAutoField(primary_key=True)
    produit = models.ForeignKey(Produit, models.DO_NOTHING)
    qte = models.IntegerField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)
    date_entre = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stk_entre'


class StkSorti(models.Model):
    id_sor = models.SmallAutoField(primary_key=True)
    produit = models.ForeignKey(Produit, models.DO_NOTHING)
    qte = models.IntegerField(blank=True, null=True)
    prix = models.FloatField(blank=True, null=True)
    date_sorti = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stk_sorti'


class User(models.Model):
    iduser = models.SmallAutoField(primary_key=True)
    nom = models.CharField(max_length=70, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    motps = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
