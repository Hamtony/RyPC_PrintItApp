from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class Asignaciones(models.Model):
    asignacion_id = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey('Solicitudes', models.DO_NOTHING)
    impresora = models.ForeignKey('Impresoras', models.DO_NOTHING)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_asignacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignaciones'


class EstadosSolicitud(models.Model):
    estado_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'estados_solicitud'


class Facturacion(models.Model):
    facturacion_id = models.AutoField(primary_key=True)
    asignacion = models.ForeignKey(Asignaciones, models.DO_NOTHING)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    estado_pago = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'facturacion'


class Impresoras(models.Model):
    impresora_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    materiales_soportados = models.CharField(max_length=255)
    dimensiones_maximas = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'impresoras'


class Materiales(models.Model):
    material_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Materiales'
    def __str__(self):
        return self.descripcion


class Solicitudes(models.Model):
    solicitud_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    archivo_stl = models.FileField(upload_to='archivos_stl/', max_length=255)
    material_id = models.ForeignKey('Materiales', on_delete=models.CASCADE, db_column='material_id')
    dimensiones = models.CharField(max_length=50)
    estado = models.ForeignKey(EstadosSolicitud, models.DO_NOTHING)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    ubicacion_entrega = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Solicitudes'


class TiposUsuarios(models.Model):
    tipo_usuario_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Tipos_Usuarios'
    def __str__(self):
        return self.descripcion


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre, password, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    usuario_id = models.AutoField(primary_key=True)  # Aquí defines que 'usuario_id' es la clave primaria
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)
    tipo_usuario = models.ForeignKey('TiposUsuarios', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']
    
    class Meta:
        db_table = 'Usuarios'