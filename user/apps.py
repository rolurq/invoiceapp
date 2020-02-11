from django.apps import AppConfig

def add_to_public_staff_group(sender, instance, created, **kwargs):
    from django.contrib.auth.models import Group
    
    if created:
        group = Group.objects.get(name='public-staff')
        instance.groups.add(group)

class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        from django.db.models.signals import post_save
        from django.conf import settings
        
        post_save.connect(add_to_public_staff_group, sender=settings.AUTH_USER_MODEL)
