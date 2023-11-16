from datetime import date
from django.db import models
from .validators import *
from .manager import *

from django.db.models.signals import pre_save
from django.dispatch import receiver


class EstadoCivil(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class EstadoCivil(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Etnia(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Anticonceptivos(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class HcpHcPerinatal(models.Model):
    CHOICES_SI_NO = (
        ('S', 'Si'),
        ('N', 'No')
    )

    CHOICES_ESTUDIOS = (
        ('Ninguno', 'Ninguno'),
        ('Primario', 'Primario'),
        ('Secundario', 'Secundario'),
        ('Universitario', 'Universitario')
    )

    CHOICES_ULTIMO_PREVIO = (
        ('n/c','n/c'),
        ('<2500g','<2500g'),
        ('normal','normal'),
        ('>=4000g','>=4000g')
    )

    hcp_id = models.BigAutoField(primary_key=True) #~VERIFICAR! ESTE CAMPO ERA CHARFIELD
    hcp_personaid = models.CharField(max_length=15, null=True, blank=True)
    hcp_nrodocumento_0019 = models.CharField(max_length=20, null=True, blank=True, help_text="Nro de Documento")
    hcp_telefono_0005 = models.SmallIntegerField(null=True, blank=True, help_text="Teléfono")
    hcp_fechanacimiento_0006 = models.DateField(validators=[validacion_fecha_nacimiento], null=True, blank=True, help_text="Fecha de nacimiento")
    hcp_edad_0009 = models.SmallIntegerField(validators=[validacion_rango_edad], null=True, blank=True, help_text="Edad")
    hcp_alertaedad_0010 = models.BooleanField(blank=True)
    hcp_etnia_0011 = models.ForeignKey(Etnia, on_delete=models.CASCADE, null=True, blank=True, help_text="Etnia")
    hcp_alfabeta_0012 = models.CharField(max_length=1, choices=CHOICES_SI_NO, blank=True, help_text="Alfabeta")
    hcp_estudios_0013 = models.CharField(max_length=40, choices=CHOICES_ESTUDIOS, null=True, blank=True, help_text="Estudios")
    hcp_aniosmayornivel_0014 = models.SmallIntegerField(null=True, blank=True, help_text="Años mayor nivel")
    hcp_estadocivil_0015 = models.CharField(max_length=40, null=True, blank=True, help_text="Estado civil")
    hcp_vivesola_0016 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Vive Sola")
    hcp_establecimientocontrolid_0017 = models.CharField(max_length=40, null=True, blank=True, help_text="Lugar de Control Prenatal")
    hcp_establecimientopartoid_0018 = models.CharField(max_length=40, null=True, blank=True, help_text="Lugar del Parto")
    hcp_ant_tbcfamiliar_0020 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="TBC Familiar")
    hcp_ant_tbcpersonal_0021 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="TBC Personal")
    hcp_ant_diabetfamiliar_0022 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Diabetes Familiar")
    hcp_ant_diabetpersonal_0023 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Diabetes Personal")
    hcp_ant_hipertenfamiliar_0024 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Hipertensión Familiar")
    hcp_ant_hipertenpersonal_0025 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Hipertensión Personal")
    hcp_ant_preeclampsiafamiliar_0026 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Preeclampsia Familiar")
    hcp_ant_preeclampsiapersonal_0027 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Preeclampsia Personal")
    hcp_ant_eclampsiafamiliar_0028 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Eclampsia Familiar")
    hcp_ant_eclampsiapersonal_0029 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Eclampsia Personal")
    hcp_ant_otracondmedicafamiliar_0030 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Otras Cond. Medicas Familiar")
    hcp_ant_otracondmedicapersonal_0031 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Otras Cond. Medicas Personal")
    hcp_ant_cgiagenitourinaria_0032 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Cgia genito-urinaria")
    hcp_ant_infertilidad_0033 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Infertilidad")
    hcp_ant_nefropatia_0035 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Cardiopatía")
    hcp_ant_cardiopat_0034 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Nefropatia")
    hcp_ant_violencia_0036 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Violencia")
    hcp_ant_vih_0432 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="VIH+")
    hcp_ant_ultimoprevio_0038 = models.CharField(max_length=40, choices=CHOICES_ULTIMO_PREVIO, null=True, blank=True, help_text="Ultimo Previo")
    hcp_ant_antecedentegemelar_0039 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Antecedente Gemelar")
    hcp_ant_gestasprevia_0040 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad Gestas Previas")
    hcp_ant_abortos_0041 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad de Abortos")
    hcp_ant_partvaginales_0042 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad de Partos Vaginales")
    hcp_ant_nacidovivo_0043 = models.SmallIntegerField(null=True, blank=True, help_text="Cant. de Nacidos Vivos ")
    hcp_ant_viven_0044 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad de hijos que viven")
    hcp_ant_tresabortosconsecu_0045 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="3 Abortos consecutivos")
    hcp_ant_cesareas_0047 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad de Césareas")
    hcp_ant_embectopico_0409 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad Embarazo Ectópico")
    hcp_ant_partosprevios_0046 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad Partos Previos")
    hcp_ant_nacidomuerto_0048 = models.SmallIntegerField(null=True, blank=True, help_text="Cantidad Nacidos Muertos")
    hcp_ant_muertoantessemana_0049 = models.SmallIntegerField(null=True, blank=True, help_text="Cant. de Muertos Primera Semana")
    hcp_ant_muertodespsemana_0050 = models.SmallIntegerField(null=True, blank=True, help_text="Cant. de Muertos Desp. de la Primera Semana.")
    hcp_ant_fechaembarazoanterior_0051 = models.DateField(null=True, blank=True, help_text="Fecha de Fin Embarazo Anterior")
    hcp_ant_finmenosdeunanio_0052 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Menor a 1 año")
    hcp_ant_embarazoplaneado_0053 = models.CharField(max_length=1, choices=CHOICES_SI_NO, null=True, blank=True, help_text="Embarazo Planeado")
    hcp_ant_fracasoanticonceptivoid_0054 = models.SmallIntegerField(null=True, blank=True, help_text="Fracaso Anticonceptivo")
    #----AUDITORIA-----
    hcp_fechadeapertura = models.DateTimeField(null=True, blank=True)
    hcp_idusuarioapertura = models.CharField(max_length=40, null=True, blank=True)
    hcp_fechacierre = models.DateTimeField(null=True, blank=True)
    hcp_idusuariocierre = models.CharField(max_length=40, null=True, blank=True)
    hcp_usuariobaja = models.CharField(max_length=40, null=True, blank=True)
    hcp_fechabaja = models.DateTimeField(null=True, blank=True)
    hcp_motivobaja = models.CharField(max_length=60, null=True, blank=True)
    hcp_aperturaestableid = models.CharField(max_length=40, null=True, blank=True)
    hcp_bajaestableid = models.CharField(max_length=40, null=True, blank=True)
    hcp_cierraestableid = models.CharField(max_length=40, null=True, blank=True)
    hcp_fechamodificacion = models.DateTimeField(null=True, blank=True)
    hcp_usuariomodificacion = models.CharField(max_length=40, null=True, blank=True)
    #----FIN DE AUDITORIA---
    anticonceptivo = models.ForeignKey(Anticonceptivos, models.DO_NOTHING,null=True,blank=True)

    objects = HcpHcPerinatalManager()

    def calcular_edad(self):
        hoy = date.today()
        fecha_nacimiento = self.hcp_fechanacimiento_0006
        edad = hoy.year - fecha_nacimiento.year - (
                    (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        self.hcp_edad_0009 = edad

    def save(self, *args, **kwargs):
        self.calcular_edad()
        if self.hcp_edad_0009 < 15 or self.hcp_edad_0009 > 35:
            self.hcp_alertaedad_0010 = True
        else:
            self.hcp_alertaedad_0010 = False
        super(HcpHcPerinatal, self).save(*args, **kwargs)

    class Meta:
        db_table = 'hcp_hcperinatalsti'

    def __str__(self):
        return f'{self.hcp_id}'
    
@receiver(pre_save, sender=HcpHcPerinatal)
def pre_save_HcpHcPerinatal(sender, instance, **kwargs):
    '''
    Realiza operaciones previas a la instanciacion de un objeto HcpHcPerinatal
    '''
    validacion_informacion_estudios(instance)
    #validacion_gestas_previas(gesta_actual, gestas_previas)
    validacion_fecha_emb_anterior(instance.hcp_ant_fechaembarazoanterior_0051, instance.hcp_ant_gestasprevia_0040)
    validacion_gestas(instance.hcp_ant_gestasprevia_0040, instance.hcp_ant_abortos_0041, instance.hcp_ant_partosprevios_0046, instance.hcp_ant_embectopico_0409)
    validacion_partos_vagianles_cesarea(instance.hcp_ant_abortos_0041, instance.hcp_ant_partvaginales_0042, instance.hcp_ant_cesareas_0047)
    validacion_nacidos_vivos(instance.hcp_ant_nacidovivo_0043, instance.hcp_ant_viven_0044, instance.hcp_ant_muertoantessemana_0049, instance.hcp_ant_muertodespsemana_0050)
    validacion_nacidos_vivos_muertos(instance.hcp_ant_nacidovivo_0043, instance.hcp_ant_nacidomuerto_0048, instance.hcp_ant_partosprevios_0046)

