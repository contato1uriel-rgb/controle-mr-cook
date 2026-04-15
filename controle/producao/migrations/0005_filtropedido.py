from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0004_relacaoitem_parcial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FiltroPedido",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("numero_pedido", models.CharField(blank=True, max_length=80)),
                ("descricao_produto", models.CharField(blank=True, max_length=255)),
                ("codigo_produto", models.CharField(blank=True, max_length=120)),
                ("saldo_pedido", models.CharField(blank=True, max_length=80)),
                ("fonte", models.CharField(blank=True, max_length=120)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["numero_pedido", "id"]},
        ),
    ]
