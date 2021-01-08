from rest_framework import serializers 
from .models import Room, User, BudgetSubmission

 
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('roomCode',
                  'contestantsCount',
                  'submissions',
                  'state')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('score',
                  'name',
                  'rank',
                  'room')

class BudgetSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetSubmission
        fields = ('title',
                  'budgetPlan',
                  'BudgetCateg',
                  'yesVotes',
				  'user')