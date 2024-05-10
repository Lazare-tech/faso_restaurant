from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from restaurant import settings

# Create your models here.
class Restaurant(models.Model):
    nom=models.CharField(max_length=40,verbose_name='Nom du restaurant')
    adresse= models.CharField(max_length=255,verbose_name='Adresse du restaurant')
    description= models.TextField(verbose_name='Description du restaurant')
    contact=PhoneNumberField(max_length=30,verbose_name='Numero de telephone')
    email= models.EmailField(verbose_name='Email du restaurant')
    image= models.ImageField(verbose_name='Photo du restaurant')
    
    def __str__(self):
        return self.nom
    
#HORAIRES 
class Horaire(models.Model):
    LUNDI='Lundi'
    MARDI = 'Mardi'
    MERCREDI = 'Mercredi'
    JEUDI = 'Jeudi'
    VENDREDI = 'Vendredi'
    SAMEDI = 'Samedi'
    DIMANCHE= 'Dimanche'
    
    CHOIX_JOUR=(
        (LUNDI,'Lundi'),
        (MARDI,'Mardi'),
        (MERCREDI,'Mercredi'),
        (JEUDI,'Jeudi'),
        (VENDREDI,'Vendredi'),
        (SAMEDI,'Samedi'),
        (DIMANCHE,'Dimanche')
    )
    Horaire= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    jour= models.CharField(max_length=30,choices=CHOIX_JOUR)
    heure_ouverture= models.TimeField(verbose_name='Heure d\'ouverture')
    heure_fermeture= models.TimeField(verbose_name='Heure de fermeture')
    
    def __str__(self):
        return f"{self.jour} - {self.heure_ouverture} a {self.heure_fermeture}"

#SERVICES DU RESTAURANT
class Service(models.Model):
    service= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    nom_service= models.CharField(max_length=30,verbose_name='Nom du service')

    def __str__(self):
        return self.nom_service

#NOTES ET AVIS DES CLIENTS
class Avis(models.Model):
    avis= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    user= models.ManyToManyField(settings.AUTH_USER_MODEL)
    commentaire_client= models.TextField(verbose_name='Commentaire')
    
   
    def __str__(self):
        return f"{self.user} - {self.commentaire_client}"

#MENU DU RESTAURANT/PLATS
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    nom_menu= models.CharField(max_length=30,verbose_name='Menu du restaurant')
    description= models.TextField(verbose_name='Description du plat')
    image= models.ImageField(verbose_name='Photo du menu')
    prix= models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.nom_menu

#TYPE DE PLAT/Ex:burger,pizza,dejeuner,dinner etc
class Plat(models.Model):
    type_plat_restaurant= models.ForeignKey(Restaurant,on_delete=models.PROTECT)
    type_plat_menu= models.ForeignKey(Menu,on_delete=models.PROTECT)
    nom= models.CharField(max_length=30,verbose_name='Type de plat')
    
    def __str__(self):
        return self.nom        

#TYPE DE CUISNE /EX:Africiane,Europeenne etc
class Cuisine(models.Model):
    type_cuisine=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    nom= models.CharField(max_length=30,verbose_name='Type de cuisine')

#TABLE
class Table(models.Model):
    restaurant= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    capacite= models.IntegerField(verbose_name='Nombre de places')
    
#RESERVATION
class Reservation(models.Model):
    table= models.ForeignKey(Table,on_delete=models.CASCADE)
    nom_client= models.CharField(max_length=30,verbose_name='Nom du client')
    numero_telephone= PhoneNumberField(verbose_name='Numero de telephone')
    date_reservation= models.DateField(default=timezone.now)
    heure_reservation= models.TimeField(verbose_name='Heure de la reservation')