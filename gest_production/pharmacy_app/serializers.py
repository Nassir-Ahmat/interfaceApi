from rest_framework import serializers
from .models import Produit, Fournisseur,Entreprise,Commande,Client,Categorie,Achat,User,StkSorti,StkEntre,Reception, LigneCmd

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model= Produit
        fields= '__all__'
        
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model= Fournisseur
        fields= '__all__'
        
class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entreprise
        fields= '__all__'
        
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Commande
        fields= '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= '__all__'
        
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categorie
        fields= '__all__'
        
class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model= Achat
        fields= '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
        
        
class StkSortiSerializer(serializers.ModelSerializer):
    class Meta:
        model= StkSorti
        fields= '__all__'
        
class StkEntreSerializer(serializers.ModelSerializer):
    class Meta:
        model= StkEntre
        fields= '__all__'
        
class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reception
        fields= '__all__'
        
class LigneCmdSerializer(serializers.ModelSerializer):
    class Meta:
     model=   LigneCmd
     fields= '__all__'
 