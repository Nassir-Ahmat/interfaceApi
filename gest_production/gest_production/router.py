from pharmacy_app.viewsets import ProduitViewset, CommandeViewset,EntrepriseViewset,FournisseurViewset,ClientViewset,CategorieViewset,AchatViewset,UserViewset,StkSortiViewset,StkEntreViewset,ReceptionViewset, LigneCmdViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', UserViewset)
router.register('client',ClientViewset)
router.register('categorie', CategorieViewset)
router.register('produit', ProduitViewset)
router.register('commande',CommandeViewset)
router.register('Achat', AchatViewset)
router.register('entreprise',EntrepriseViewset)
router.register('fournisseur',FournisseurViewset)
router.register('stkSorti', StkSortiViewset)
router.register('stkEntree', StkEntreViewset)
router.register('reception', ReceptionViewset)
router.register('ligneCmd', LigneCmdViewset)


