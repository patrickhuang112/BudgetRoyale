from django.db import models

class BudgetSubmission(models.Model):
    title = models.CharField(max_length=255);
    budgetPlan = models.TextField();
    BudgetCateg = models.CharField(max_length=255);
    yesVotes = models.IntegerField();

class User(models.Model):
    score = models.IntegerField();
    name = models.CharField(max_length = 255);
    ID = models.CharField(max_length = 12);
    rank = models.IntegerField();

class Room(models.Model):
    roomCode = models.charField(max_length = 20);

    user1 = User()
    budgetSub1 = BudgetSubmission();

    user2 = User()
    budgetSub1 = BudgetSubmission();

    user3 = User()
    budgetSub1 = BudgetSubmission();

    user4 = User()
    budgetSub1 = BudgetSubmission();

    user5 = User();
    budgetSub1 = BudgetSubmission();

