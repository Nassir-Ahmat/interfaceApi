from rest_framework import viewsets
from . import models 
from . import serializers

class ProduitViewset(viewsets.ModelViewSet):
    queryset= models.Produit.objects.all()
    serializer_class=serializers.ProduitSerializer
    
class FournisseurViewset(viewsets.ModelViewSet):
    queryset= models.Fournisseur.objects.all()
    serializer_class=serializers.FournisseurSerializer
    
class EntrepriseViewset(viewsets.ModelViewSet):
    queryset= models.Entreprise.objects.all()
    serializer_class=serializers.EntrepriseSerializer
    
class CommandeViewset(viewsets.ModelViewSet):
    queryset= models.Commande.objects.all()
    serializer_class=serializers.CommandeSerializer
    
class ClientViewset(viewsets.ModelViewSet):
    queryset= models.Client.objects.all()
    serializer_class=serializers.ClientSerializer
    
class CategorieViewset(viewsets.ModelViewSet):
    queryset= models.Categorie.objects.all()
    serializer_class=serializers.CategorieSerializer
    
class AchatViewset(viewsets.ModelViewSet):
    queryset= models.Achat.objects.all()
    serializer_class=serializers.AchatSerializer
    
class UserViewset(viewsets.ModelViewSet):
    queryset= models.User.objects.all()
    serializer_class=serializers.UserSerializer
    
class StkSortiViewset(viewsets.ModelViewSet):
    queryset= models.StkSorti.objects.all()
    serializer_class=serializers.StkSortiSerializer
    
class StkEntreViewset(viewsets.ModelViewSet):
    queryset= models.StkEntre.objects.all()
    serializer_class=serializers.StkEntreSerializer
    
class ReceptionViewset(viewsets.ModelViewSet):
    queryset= models.Reception.objects.all()
    serializer_class=serializers.ReceptionSerializer
    
class LigneCmdViewset(viewsets.ModelViewSet):
    queryset= models.LigneCmd.objects.all()
    serializer_class=serializers.LigneCmdSerializer
    