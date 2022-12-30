from django import forms

# for getting table/model created in database realated to form
from todo_list.models import Todo 


#here is form related to database ,so we use ModelForm
class TodoForm(forms.ModelForm):
    #for specifying which model(table) we need to connect. (here is --Todo). meta is information about class
    class Meta:
        model = Todo
        fields = '__all__'
