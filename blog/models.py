from django.db import models



class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    category = models.ForeignKey(BlogCategoryModel,on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)



