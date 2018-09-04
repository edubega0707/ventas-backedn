from django.db import models
from django.contrib.auth.models import User
from productos.models import Tarifa
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    CODIGO      =models.AutoField(primary_key=True)
    NOMBRE      =models.CharField(max_length=250,null=True,blank=True)
    DIRECCIÓN   =models.CharField(max_length=200,null=True,blank=True)
    COLONIA     =models.CharField(max_length=200,null=True,blank=True)
    POBLACIÓN   =models.CharField(max_length=100,null=True,blank=True)
    MUNICIPIO   =models.CharField(max_length=150,null=True,blank=True)
    CP          =models.CharField(max_length=200,null=True,blank=True)
    RFC         =models.CharField(max_length=50,null=True,blank=True)
    TELÉFONO    =models.CharField(max_length=50,null=True,blank=True)
    CORREO      =models.EmailField(blank=True,null=True)
    def __str__(self):
        return self.NOMBRE

    class Meta:
        permissions = (
            ('vendedor', 'vendedor'),
            ('cajero', 'cajero'),
            ('surtidor', 'surtidor'),
            ('validador','validador')
        )

    def get_absolute_url(self):
        return reverse('pedidos:detallecliente', kwargs={'pk': self.pk})




class DomCliente(models.Model):
    cliente     = models.ForeignKey(Cliente, related_name="cliente_domicilio", on_delete=models.CASCADE)
    calle       = models.CharField(max_length=200, null=True, blank=True)
    colonia     = models.CharField(max_length=200, null=True, blank=True)
    poblacion   = models.CharField(max_length=100, null=True, blank=True)
    municipio   = models.CharField(max_length=150, null=True, blank=True)
    cp          = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return 'domicilio {}  {}  del cliente {}'.format(self.calle, self.colonia, self.cliente.NOMBRE)


    @receiver(post_save, sender=Cliente)
    def ensure_profile_exists(sender, instance, **kwargs):
        if kwargs.get('created', False):
             DomCliente.objects.get_or_create(cliente=instance, calle=instance.DIRECCIÓN, colonia=instance.COLONIA,
                                      poblacion=instance.POBLACIÓN, municipio=instance.MUNICIPIO, cp=instance.CP)
                # Muro.objects.get_or_create(user=kwargs.get('instance'))


statusorden=(
    ('g','generada'),
    ('a','aprobada'),
    ('c','cancelada'),
    ('v','validar'),
    ('s','surtida '),
    ('i','surtida incompleto'),


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


class Orden(models.Model):
    numerodeorden       =models.CharField(max_length=30)
    vendedor            =models.ForeignKey(User, related_name="orden", on_delete=models.PROTECT)
    cliente             =models.ForeignKey(Cliente,related_name="cliente",on_delete=models.CASCADE)
    status              =models.CharField(choices=statusorden, default='a', max_length=1)
    tipoorden           =models.CharField(choices=tipo,default='CONTADO',max_length=20)
    diasdecredito       =models.CharField(max_length=2, choices=dias, default='no' )
    otrodomicilio       =models.BooleanField(default=False)
    domicilio_extra     =models.ForeignKey(DomCliente, related_name="cliente_dom",on_delete=models.CASCADE, blank=True,null=True)
    fechageneracion     =models.DateTimeField(auto_now_add=True)
    comentario          =models.TextField(null=True,blank=True)
    referencia_bancaria =models.CharField(null=True,blank=True, max_length=50)
    cargos              =models.FloatField(default=0)
    total               =models.FloatField(default=0)


    def __str__(self):
        return self.numerodeorden
    def get_absolute_url(self):
        return reverse('pedidos:detalle',args=[self.id])


class Pedido(models.Model):
    orden       =models.ForeignKey(Orden,related_name='items',on_delete=models.CASCADE, blank=True, null=True )
    producto    =models.ForeignKey(Tarifa,related_name='order_items',on_delete=models.SET_NULL, blank=True, null=True)
    cantidad    =models.IntegerField(null=False,blank=False)
    subtotal    =models.FloatField(default=0)
    def __str__(self):
        return 'item {} of order {}'.format(self.producto.Nombre, self.orden.id)



def directorio_pedido(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'pedidos/{0}/{1}'.format(instance.orden.numerodeorden, filename)

class Archivo(models.Model):
    orden           =models.ForeignKey(Orden, related_name='archivos', on_delete=models.CASCADE, blank=True, null=True)
    impresion       = models.FileField(null=True, blank=True, upload_to=directorio_pedido)

    def __str__(self):
        return self.orden.numerodeorden

class Archivodos(models.Model):
    orden           =models.ForeignKey(Orden, related_name='archivos_dos', on_delete=models.CASCADE, blank=True, null=True)
    impresiondos    =models.FileField(null=True, blank=True, upload_to=directorio_pedido)

    def __str__(self):
        return self.orden.numerodeorden
