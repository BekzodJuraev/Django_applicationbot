from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProposalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Proposal.Status.PUBLISHED)

class Proposal(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'WT', 'Waiting'
        PUBLISHED = "DN", "Done"
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_request = models.AutoField(primary_key=True)
    id_user = models.IntegerField(null=True)
    fullname=models.CharField(max_length=200)
    text=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.DRAFT)


    def __str__(self):
        return self.fullname



    class Meta:
        ordering=['created']

