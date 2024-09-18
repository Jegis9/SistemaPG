from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# aqui se manejan los diferentes perfiles que tendra el usuario para poder redirigirlo a cierta pagina segun tenga su perfil relacionado con el usuario

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # se relaciona el perfil con un usuario
    is_internal = models.BooleanField(default=False) # se crea el campo para ver a que pertenece, por defecto False en views se cambia esto
                                                     # si el usuario no es interno lo dirigira a la pagina de emergencias
                                                     # si el susuario es interno lo digiriga a la pagina de administracion

    image = models.ImageField(default='avatar.jpg', upload_to='Profile_images')
# cuando el usuario es creado en esta parte se asegura que el perfil es creado con su respectivo perfil
@receiver(post_save, sender=User) # primero se crea el perfil segun el usuario 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # y aqui se guarda el perfil que se creo segun el usuario relacion
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


