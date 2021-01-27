from django.db import models

# Model Personnel.



class Personnel(models.Model):
     identifiant = models.IntegerField(null=True,blank=True,verbose_name="identifiant")
     prenom = models.CharField(max_length=200, null=True, blank=True, verbose_name="Prénom")
     nom = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nom")
     fonction = models.CharField(max_length=200,null=True, blank=True, verbose_name="Fonctions/Grades")
     tel = models.IntegerField(null=True, blank=True, verbose_name="Téléphone")
     email = models.CharField(max_length=200,null=True, blank=True, verbose_name="Email")
     
     
     def __str__(self):
       return self.prenom
