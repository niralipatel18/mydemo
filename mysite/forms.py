from django import forms
from .models import signup,post,reviews

class signupform(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'

class postform(forms.ModelForm):
    class Meta:
        model=post
        fields='__all__'

class reviewsform(forms.ModelForm):
    class Meta:
        model=reviews
        fields='__all__'

# class reviewsform(forms.ModelForm):
#     class Meta:
#         model:reviews
#         fields='__all__'
