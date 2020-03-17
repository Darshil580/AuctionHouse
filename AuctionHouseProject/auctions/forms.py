from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
# from django import forms


class UserCreateForm(UserCreationForm):
    class Meta():
        fields=('username','email','password1','password2')
        model=get_user_model()

    #Custom Label for model that is predefined in auth.
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label='Email Address'

class ProfileSetupForm():
    class Meta():
        fields=('image','address','mobile','proof_document')
        models=get_user_model()

class BecomeAgentForm(UserCreationForm):
    class Meta():
<<<<<<< HEAD
        fields=('first_name','last_name','email','mobile','birth_date','address','image','resume_document','proof_document')
        model = models.AgentUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       # self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email Address'
        self.fields['mobile'].label = 'Enter Mobile Number'
        self.fields['birth_date'].label = 'Ente Your Birth Date'
        self.fields['address'].label = 'Enter Your Address'
        self.fields['image'].label = 'Select Your Profile Image:'
        self.fields['resume_document'].label = 'Your Resume:'
        self.fields['proof_document'].label = 'Any Valid Id Proof:'
        # self.fields['password1'].disabled =True
        # self.fields['password1'].type = 'hidden'

=======
        models=models.AgentUser
        fields=('','','','')
>>>>>>> f27093f459a4e642b248d5417a1d9ce369f828c8

class MakeAnOffer():
    class Meta():
        models =models.MakeAnOffer
        fields=('title','first_name','last_name','email','offer_amount')
# class AgentCreateFrom(UserCreateForm):
#     class Meta():
#         fields=('username','email','password1','password2')
#         model=get_user_model()
