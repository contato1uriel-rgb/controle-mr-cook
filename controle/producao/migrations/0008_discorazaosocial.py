from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0007_relacaoitem_pedido_numero"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscoRazaoSocial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cod", models.CharField(max_length=120, unique=True)),
                ("razao_social", models.CharField(blank=True, max_length=255)),
                ("origem", models.CharField(blank=True, max_length=120)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["cod"]},
        ),
    ]
