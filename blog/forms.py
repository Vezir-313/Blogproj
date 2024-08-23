from django import forms
from .models import BlogModel


class BlogModelForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ("title","content","category")
        labels = {
            "title":"Blog Title",
        }

    def __init__(self, *args, **kwargs):
        super(BlogModelForm,self).__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Blog Category"