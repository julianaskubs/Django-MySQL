from django.db import models


class Aluno(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=30)
    dt_nasc = models.DateField(db_column='Dt_Nasc')
    rg = models.DecimalField(db_column='RG', max_digits=10, decimal_places=0)
    endereco = models.CharField(db_column='Endereco', max_length=60)
    obs = models.CharField(db_column='Obs', max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Aluno'

    def salvar(self):
        self.save()

    def __str__(self):
        return self.nome
