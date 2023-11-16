from django import forms
from .models import *
from django.forms.widgets import CheckboxInput


radio_widget_conf = forms.ChoiceField(
        widget=forms.RadioSelect(
        ),
        choices=HcpHcPerinatal.CHOICES_SI_NO,
        required=False
    )

class HcpHcPerinatalForm(forms.ModelForm):

    CHOICES_SI_NO = [
        ('S', 'Si'),
        ('N', 'No')
    ]
    
    hcp_ant_ultimoprevio_0038 = forms.ChoiceField(
        widget=forms.RadioSelect(
        ),
        choices=HcpHcPerinatal.CHOICES_ULTIMO_PREVIO,
        required=False
    )
    
    hcp_edad_0009 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
               'placeholder': 'Edad',
               'class': 'form-control',
               'readonly':'True'
            }
        )
    )

    hcp_fechanacimiento_0006 = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'placeholder': 'Fecha de Nacimiento',
                'type': 'date',
                'class': 'form-control'
            }
        )
    )

    hcp_ant_fechaembarazoanterior_0051 = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
    )

    hcp_alfabeta_0012 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(
            attrs={
            }
        ),
        choices=HcpHcPerinatal.CHOICES_SI_NO,
    )

    hcp_estudios_0013 = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(
            attrs={
                'name': 'hcp_estudios_0013'
            }
        ),
        choices=HcpHcPerinatal.CHOICES_ESTUDIOS,
    )

    hcp_etnia_0011 = forms.ModelChoiceField(
        required=False,
        queryset=Etnia.objects.all()
    )

    hcp_estadocivil_0015 = forms.ModelChoiceField(
        required=False,
        queryset=EstadoCivil.objects.all(),
    )

    hcp_vivesola_0016 = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'selectpicker'}),
        choices=[('','---------')] + CHOICES_SI_NO,
    )
    hcp_ant_antecedentegemelar_0039 = radio_widget_conf
    hcp_alfabeta_0012 = radio_widget_conf
    hcp_ant_tbcfamiliar_0020 = radio_widget_conf
    hcp_ant_tbcpersonal_0021 = radio_widget_conf
    hcp_ant_diabetfamiliar_0022 = radio_widget_conf
    hcp_ant_diabetpersonal_0023 = radio_widget_conf
    hcp_ant_hipertenfamiliar_0024 = radio_widget_conf
    hcp_ant_hipertenpersonal_0025 = radio_widget_conf
    hcp_ant_preeclampsiafamiliar_0026 = radio_widget_conf
    hcp_ant_preeclampsiapersonal_0027 = radio_widget_conf
    hcp_ant_eclampsiafamiliar_0028 = radio_widget_conf
    hcp_ant_eclampsiapersonal_0029 = radio_widget_conf
    hcp_ant_otracondmedicafamiliar_0030 = radio_widget_conf
    hcp_ant_otracondmedicapersonal_0031 = radio_widget_conf
    hcp_ant_cgiagenitourinaria_0032 = radio_widget_conf
    hcp_ant_infertilidad_0033 = radio_widget_conf
    hcp_ant_nefropatia_0035 = radio_widget_conf
    hcp_ant_cardiopat_0034 = radio_widget_conf
    hcp_ant_violencia_0036 = radio_widget_conf
    hcp_ant_vih_0432 = radio_widget_conf
    hcp_ant_tresabortosconsecu_0045=radio_widget_conf

    #hcp_alfabeta_0012 = forms.MultipleChoiceField(
    #    required=False,  # Puedes cambiar esto según tus necesidades
    #    widget=forms.CheckboxSelectMultiple,
    #    choices=[('S', 'Sí'), ('N', 'No')],
    #)

    class Meta:
        
        CHOICES_SI_NO = (
        ('S', 'Sí'),
        ('N', 'No'),
        )
        
        model = HcpHcPerinatal
        fields = '__all__'
        exclude = [
            "hcp_id",
            "hcp_personaid",
            "hcp_fechadeapertura",
            "hcp_idusuarioapertura",
            "hcp_fechacierre",
            "hcp_idusuariocierre",
            "hcp_usuariobaja",
            "hcp_fechabaja",
            "hcp_motivobaja",
            "hcp_aperturaestableid",
            "hcp_bajaestableid",
            "hcp_cierraestableid",
            "hcp_fechamodificacion",
            "hcp_usuariomodificacion",
        ]
        

    
    def __init__(self, *args, **kwargs):
        super(HcpHcPerinatalForm, self).__init__(*args, **kwargs)
        self.fields['hcp_ant_gestasprevia_0040'].initial = 0
        self.fields['hcp_ant_abortos_0041'].initial = 0
        self.fields['hcp_ant_partvaginales_0042'].initial = 0
        self.fields['hcp_ant_nacidovivo_0043'].initial = 0
        self.fields['hcp_ant_viven_0044'].initial = 0
        self.fields['hcp_ant_cesareas_0047'].initial = 0
        self.fields['hcp_ant_partosprevios_0046'].initial = 0
        self.fields['hcp_ant_nacidomuerto_0048'].initial = 0
        self.fields['hcp_ant_muertoantessemana_0049'].initial = 0
        self.fields['hcp_ant_muertodespsemana_0050'].initial = 0
        self.fields['hcp_ant_embectopico_0409'].initial = 0


        for field_name, field in self.fields.items():
            # obtengo  el help_text del campo y establezco el placeholder
            # model_field = self._meta.model._meta.get_field(field_name)
            # field.widget.attrs['placeholder'] = model_field.help_text
            # establezco atributos para bootstrap
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'  ##Controlar aqui
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif not isinstance(field.widget, forms.widgets.RadioSelect ):
                field.widget.attrs['class'] = 'form-control'
        
    

class TestForm(forms.ModelForm):
    hcp_fechanacimiento_0006 = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
    )

    hcp_ant_fechaembarazoanterior_0051 = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = HcpHcPerinatal
        fields = '__all__'
        exclude = [
            "hcp_fechadeapertura",
            "hcp_idusuarioapertura",
            "hcp_fechacierre",
            "hcp_idusuariocierre",
            "hcp_usuariobaja",
            "hcp_fechabaja",
            "hcp_motivobaja",
            "hcp_aperturaestableid",
            "hcp_bajaestableid",
            "hcp_cierraestableid",
            "hcp_fechamodificacion",
            "hcp_usuariomodificacion",
        ]

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # obtengo  el help_text del campo y establezco el placeholder
            model_field = self._meta.model._meta.get_field(field_name)
            field.widget.attrs['placeholder'] = model_field.help_text
            # establezco atributos para bootstrap
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    def get_elements(self):
        field_names = [
            ["hcp_alfabeta_0012", "hcp_estudios_0013", "hcp_etnia_0011", "hcp_aniosmayornivel_0014"],
            ["hcp_ant_tbcpersonal_0021", "hcp_ant_tbcfamiliar_0020"],
            ["hcp_ant_ultimoprevio_0038", "hcp_ant_antecedentegemelar_0039"],
            ["hcp_ant_gestasprevia_0040", "hcp_ant_abortos_0041", "hcp_ant_partvaginales_0042",
             "hcp_ant_nacidovivo_0043",
             "hcp_ant_viven_0044", "hcp_ant_tresabortosconsecu_0045", "hcp_ant_partosprevios_0046",
             "hcp_ant_cesareas_0047",
             "hcp_ant_nacidomuerto_0048", "hcp_ant_muertoantessemana_0049", "hcp_ant_muertodespsemana_0050",
             "hcp_ant_embectopico_0409"],
            ["hcp_ant_fechaembarazoanterior_0051", "hcp_ant_finmenosdeunanio_0052", "hcp_ant_embarazoplaneado_0053",
             "hcp_ant_fracasoanticonceptivoid_0054"]
        ]
        grouped_fields = []

        for group in field_names:
            field_group = [self[field_name] for field_name in group]
            grouped_fields.append(field_group)

        return grouped_fields