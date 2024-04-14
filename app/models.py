from django.db import models

# Create your models here.
task={
    "pending":"pending",
    "Done":"Done"
}
class Task(models.Model):
    task_details = models.TextField(max_length=100)
    task_type = models.CharField(max_length=100,choices=task)

    def __str__(self):
        return str(self.task_details)


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.IntegerField()
    ID=models.AutoField(primary_key=True)
    task = models.ForeignKey(Task,on_delete=models.CASCADE,null=True)

    class Meta:
        
        db_table= 'usermodel'

    def __str__(self):
        return self.name