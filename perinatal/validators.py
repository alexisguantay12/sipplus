from django.core.exceptions import ValidationError
from django.utils import timezone


def validacion_fecha_nacimiento(value):
    hoy = timezone.now().date()
    if (hoy - value).days < 3650:  # 3650 días = 10 años
        raise ValidationError("La fecha de nacimiento debe ser al menos 10 años antes de la fecha actual.")


def validate_fecha_valida(value):
    hoy = timezone.now().date()
    if value > hoy:
        raise ValidationError("La fecha no puede ser posterior a la fecha actual.")


def validacion_rango_edad(value):
    if value < 0 or value > 100:
        raise ValidationError("La edad debe estar entre 0 y 100 años.")
    
def validacion_informacion_estudios(instance):
    if instance.hcp_alfabeta_0012 == 'N':
        instance.hcp_estudios_0013 = 'Ninguno'
        instance.hcp_aniosmayornivel_0014 = None
    elif instance.hcp_alfabeta_0012 == 'S':
        if instance.hcp_estudios_0013 == 'Ninguno':
            raise ValidationError('Seleccione otro valor para la variable Estudios, ya que el pte es Alfabeta')
        if instance.hcp_estudios_0013 != 'Ninguno' and instance.hcp_aniosmayornivel_0014 is None:
            raise ValidationError('Ingrese cantidad de años que realizo')


def validacion_gestas_previas(gesta_actual, gestas_previas):  # o partos
    if (gesta_actual - 1) != gestas_previas:
        raise ValidationError("Gesta previa: Debe ser igual a la gesta actual menos uno.")

def validacion_gestas(gesta_previa, aborto, parto, emb_ectopico):
    if gesta_previa != (aborto + parto + emb_ectopico):
        raise ValidationError("Gestas Previas: debe ser igual a la suma de abortos + partos + embarazos ectópicos.")

def validacion_partos_vagianles_cesarea(partos, vaginales, cesareas):
    if partos != (vaginales + cesareas):
        raise ValidationError("Los partos deben ser igual a vaginales + cesáreas.")

def validacion_nacidos_vivos(nacidos_vivos,viven, muertos_1raSemana, muertos_desp1raSem):
    if nacidos_vivos != (viven + muertos_1raSemana + muertos_desp1raSem):
        raise ValidationError("Los Nacidos Vivos: Deben ser igual a la suma de viven + muertos 1ra Semana + muertos desp. de la 1ra Semana.")

def validacion_nacidos_vivos_muertos(nacidos_vivos, nacidos_muertos, partos_previos):
    if partos_previos != (nacidos_vivos + nacidos_muertos):
        raise ValidationError("Partos Previos: Debe ser igual a la suma de nacids vivos + nacidos muertos.")

def validacion_fecha_emb_anterior(fecha_emb_anterior, gestas_previas):
    if fecha_emb_anterior is None and gestas_previas != 0:
        raise ValidationError("Debe completarse la fecha de fin de embarazo, ya que tiene gestas previas cargadas.")
