from django.db import models


STATUSES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In progress'),
        ('PENDING', 'Pending'),
        ('BLOCKED', 'Blocked'),
        ('DONE', 'Done'),
]


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=50, unique_for_date='deadline')
    description = models.TextField()
    category = models.ManyToManyField(Category)
    status = models.CharField(
        max_length=30,
        default='NEW',
        choices=STATUSES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# Create your models here.


class SubTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30,
        default='NEW',
        choices=STATUSES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

