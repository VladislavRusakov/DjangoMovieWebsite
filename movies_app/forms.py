from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма рецензий"""
    class Meta:
        model = Reviews
        fields = ("text", "name", "email")
        