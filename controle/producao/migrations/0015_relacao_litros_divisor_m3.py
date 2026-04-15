from decimal import Decimal

from django.db import migrations, models


def seed_rel_106_divisor(apps, schema_editor):
    Relacao = apps.get_model("producao", "Relacao")
    # 16459 L (soma qtd×litros inferidos) ÷ 695 ≈ 23,68 m³ (PCP)
    Relacao.objects.filter(pk=26).update(litros_divisor_m3=Decimal("695"))


def noop_reverse(apps, schema_editor):
    Relacao = apps.get_model("producao", "Relacao")
    Relacao.objects.filter(pk=26).update(litros_divisor_m3=None)


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0014_filtropedido_volume_m3"),
    ]

    operations = [
        migrations.AddField(
            model_name="relacao",
            name="litros_divisor_m3",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.RunPython(seed_rel_106_divisor, noop_reverse),
    ]
