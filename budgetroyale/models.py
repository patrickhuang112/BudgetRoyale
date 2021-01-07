from django.db import models

class BudgetSubmission(models.Model):
    title = models.CharField(max_length=255, default="");
    budgetPlan = models.TextField(default="");
    BudgetCateg = models.CharField(max_length=255, default = "");
    yesVotes = models.IntegerField(default=0);

class User(models.Model):
    score = models.IntegerField(default=0);
    name = models.CharField(max_length = 255, default = "");
    rank = models.IntegerField(default=0);

class Room(models.Model):
    roomCode = models.CharField(max_length = 20, default = "");

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