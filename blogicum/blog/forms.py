from django import forms

from .models import Comment, Post, User


# Для использования формы с моделями меняем класс на forms.ModelForm.
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        # Указываем, что надо отобразить все поля.
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'datetime-local'})
        }
