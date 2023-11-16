from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import HcpHcPerinatal
from .validators import validacion_informacion_estudios

