from rest_framework import serializers
from .models import Proposal

class ProposalSerializers(serializers.ModelSerializer):
    class Meta:
        model=Proposal
        fields=['id_user','fullname','text']