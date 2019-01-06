from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 50)
    reputation = models.IntegerField(default = 0)

    def __str__(self):
        return self.username

class Questions(models.Model):
    title = models.CharField(max_length = 1000)
    body = models.CharField(max_length = 7000)
    tags = models.CharField(max_length = 200)
    is_answered = models.BooleanField(default = False)
    has_correct_answer = models.BooleanField(default = False)
    owner_id = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Answers(models.Model):
    details = models.CharField(max_length = 7000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete = models.CASCADE)
    is_correct = models.BooleanField(default = False)

    def __str__(self):
        return self.details

class Comments(models.Model):
    comment = models.CharField(max_length = 1000)
    question_id = models.ForeignKey(Questions, on_delete = models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.comment

class Upvotes(models.Model):
    question_id = models.ForeignKey(Questions, on_delete = models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE,related_name='to_user')
    upvoter_id = models.ForeignKey(User,on_delete = models.CASCADE, related_name='from_user')
    vote_count = models.IntegerField( default = 0)

    def __str__(self):
        return self.question_id + " " + self.vote_count

class Favourites(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    answer_id = models.ForeignKey(Answers, on_delete = models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete = models.CASCADE)

    def __str__(self):
        return self.user_id