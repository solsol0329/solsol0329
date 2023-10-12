from django import forms
from .models import Article



# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class':'my_title'
            }
        )
    )
    # 모델 등록
    class Meta: 
    # Meta 는 ArticleForm에 대한 데이터를 담고 있다.
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)