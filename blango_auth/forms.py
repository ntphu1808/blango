from crispy_forms.helper import FormHelper #We use FormHelper to set options for a Crispy template tag
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm 

from blango_auth.models import User


class BlangoRegistrationForm(RegistrationForm):      #this class provides a custom form for creating a new user account, we then use this form in templates html
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        # inherite all the attributes of the parent class (RegistrationForm)
        super(BlangoRegistrationForm, self).__init__(*args, **kwargs) 
        
        #and throw in the helper attribute = FormHelper
        self.helper = FormHelper()
        
        #Add the submit button with value=Register
        self.helper.add_input(Submit("submit", "Register"))
