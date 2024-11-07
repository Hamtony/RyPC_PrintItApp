# Generated by Django 5.1.3 on 2024-11-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaciones',
            fields=[
                ('asignacion_id', models.AutoField(primary_key=True, serialize=False)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_asignacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'asignaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadosSolicitud',
            fields=[
                ('estado_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'estados_solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('facturacion_id', models.AutoField(primary_key=True, serialize=False)),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('fecha_pago', models.DateTimeField(blank=True, null=True)),
                ('estado_pago', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'facturacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Impresoras',
            fields=[
                ('impresora_id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('materiales_soportados', models.CharField(max_length=255)),
                ('dimensiones_maximas', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'impresoras',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'materiales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('solicitud_id', models.AutoField(primary_key=True, serialize=False)),
                ('archivo_stl', models.CharField(max_length=255)),
                ('dimensiones', models.CharField(max_length=50)),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True)),
                ('ubicacion_entrega', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'solicitudes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiposUsuarios',
            fields=[
                ('tipo_usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'tipos_usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('direccion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
    ]