from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper #We use FormHelper to set options for a Crispy template tag
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        # inherite all the attributes of the parent class (ModelForm)
        super(CommentForm, self).__init__(*args, **kwargs)
        #and throw in the helper attribute = FormHelper 
        self.helper = FormHelper()
        #Add the submit button with value=Submit
        self.helper.add_input(Submit('submit', 'Submit'))

"""We’re now done with Django Crispy Forms. You can see the advantage 
of the crispy form tag is that you can move all your form setup into 
the form class, and just have a single line in your template to render 
it with all the right options it requires. Since you do all your other 
customization of the form in Python (such as what fields you want to 
display) it makes sense to also choose how to display your buttons, 
form tag and other helper elements in Python too."""