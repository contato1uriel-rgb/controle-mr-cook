from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("producao", "0008_discorazaosocial"),
    ]

    operations = [
        migrations.AddField(
            model_name="discorazaosocial",
            name="bairro",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="discorazaosocial",
            name="cidade",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="discorazaosocial",
            name="segmento",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="discorazaosocial",
            name="telefone",
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name="discorazaosocial",
            name="uf",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
