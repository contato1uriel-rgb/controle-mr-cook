from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0016_relacaoitem_observacao"),
    ]

    operations = [
        migrations.CreateModel(
            name="CacarolaMaquina",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=120, unique=True)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="CacarolaProduto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=255, unique=True)),
                ("ciclo", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="CacarolaRegistro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uid", models.CharField(max_length=64, unique=True)),
                ("data", models.DateField()),
                ("turno", models.CharField(blank=True, max_length=20)),
                ("maquina", models.CharField(blank=True, max_length=120)),
                ("responsavel", models.CharField(blank=True, max_length=120)),
                ("tipo_produto", models.CharField(blank=True, max_length=20)),
                ("produto", models.CharField(blank=True, max_length=255)),
                ("quantidade", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("odf", models.CharField(blank=True, max_length=80)),
                ("inicio", models.TimeField(blank=True, null=True)),
                ("fim", models.TimeField(blank=True, null=True)),
                ("refeicao", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("tempo", models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ("pecas_hora", models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ("paradas_min", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("ciclo", models.DecimalField(decimal_places=4, default=0, max_digits=12)),
                ("perdas", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("material", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("estampo", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("polimento", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("refilador", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("rebite", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("amassado", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("pintura", models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-data", "-id"],
            },
        ),
    ]
