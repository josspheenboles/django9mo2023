from django.forms import *
from .models import *
class TaskForm(Form):
    #build form
    name=CharField(required=True,max_length=100)

    catgoryfiled=ChoiceField(required=True,choices=[(cat.id,cat.name) for cat in Catagory.objects.all()])

class TaskformModel(ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        labels={
            'name':'task name'
        }
