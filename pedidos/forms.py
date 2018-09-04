from django.contrib.auth.models import User
from django import forms
from .models import Orden, Cliente, DomCliente

statusorden=(
    ('', ''),
    ('a','aprobada'),
    ('c','cancelada'),
)

dias=(
    ('no','no'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31'),
)

tipo=(
    ('CONTADO','CONTADO'),
    ('ANTICIPADO','ANTICIPADO'),
    ('CREDITO','CREDITO'),
)


class FormAprobar(forms.ModelForm):
    status            =forms.ChoiceField(required=True, error_messages={'required': 'Aprueba tu orden'},label="Status Orden", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}), choices=statusorden)
    #cliente           =forms.ModelChoiceField(queryset=Cliente.objects.all(), label="Cliente", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Cliente'}))
    tipoorden         =forms.ChoiceField(label="Tipo de orden", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tipo de orden'}), choices=tipo)
    diasdecredito     =forms.ChoiceField(label="Dias de credito", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Dias de credito'}),choices=dias)
    #domicilio_extra   =forms.ModelChoiceField(queryset=DomCliente.objects.all(), label="Domicilio extra", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Domicilio extra'}))
    comentario        =forms.CharField(label='Comentario', min_length=4, max_length=250,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentario'}))
    cargos            =forms.IntegerField(label='Cargos adicionales', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargos adicionales'}))

   
    class Meta:
        model=Orden
        fields=['status','tipoorden', 'diasdecredito', 'comentario', 'cargos']


statusvalidar=(
    ('',''),
    ('v','validar'),
    ('c','cancelada'),

)

class FormValidar(forms.ModelForm):
    referencia_bancaria = forms.CharField(required=False,label='Referencia Bancaria', min_length=4, max_length=250,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Referencia bancaria'}))
    status      =forms.ChoiceField(required=True, error_messages={'required': 'Valida tu orden'}, label="Status Orden", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}), choices=statusvalidar)
    comentario = forms.CharField(label='Comentario', min_length=4, max_length=250, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentario'}))
    class Meta:
        model=Orden
        fields=['status','referencia_bancaria', 'comentario']




statussurtir=(
    ('s','surtida'),
    ('i','Surtida Incompleto')
)


class FormSurtir(forms.ModelForm):

    status      =forms.ChoiceField(label="Status Orden", widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}), choices=statussurtir)
    comentario  =forms.CharField(label='Comentario', min_length=4, max_length=250, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentario'}))
    class Meta:
        model=Orden
        fields=['status','comentario']



class FormCliente(forms.Form):


    NOMBRE      = forms.CharField(label='nombre del cliente', max_length=250,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}))
    DIRECCIÓN   = forms.CharField(label='Calle y numero',  max_length=250,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle y numero '}))
    COLONIA     = forms.CharField(label='Colonia', max_length=250,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}))
    POBLACIÓN   = forms.CharField(label='Poblacion',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poblacion'}))
    MUNICIPIO   = forms.CharField(label='Municipio',
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Municipio'}))
    CP          = forms.CharField(label='Codigo postal',
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo Postal'}))
    RFC         = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'RFC'}))

    TELÉFONO    = forms.CharField(label='Ingresa nombre de usuario', max_length=20,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}))

    CORREO      = forms.EmailField(label='Correo electronico',  max_length=150,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}))


    #class Meta:
    #    model = Cliente
    #    fields = '__all__'



    def save(self, commit=True):
        cliente = Cliente.objects.create()
        cliente.NOMBRE = self.cleaned_data['NOMBRE'].upper()
        cliente.DIRECCIÓN = self.cleaned_data['DIRECCIÓN'].upper()
        cliente.COLONIA = self.cleaned_data['COLONIA'].upper()
        cliente.POBLACIÓN = self.cleaned_data['POBLACIÓN'].upper()
        cliente.MUNICIPIO = self.cleaned_data['MUNICIPIO'].upper()
        cliente.CP = self.cleaned_data['CP'].upper()
        cliente.RFC = self.cleaned_data['RFC'].upper()
        cliente.TELÉFONO = self.cleaned_data['TELÉFONO'].upper()
        cliente.CORREO = self.cleaned_data['CORREO']


        cliente.save()

        return cliente



