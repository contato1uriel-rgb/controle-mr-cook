from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0012_discorazaosocial_cols_h_i"),
    ]

    operations = [
        migrations.AddField(
            model_name="relacao",
            name="liberacao_producao_data",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="relacao",
            name="previsao_data",
            field=models.DateField(blank=True, null=True),
        ),
    ]
