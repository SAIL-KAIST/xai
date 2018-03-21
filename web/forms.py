from django import forms
from .models import News, Community, DemoResource

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'content', 'submenu_id')

class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ('title', 'content', 'writer')

class DemoForm(forms.ModelForm):

    class Meta:
        model = DemoResource
        fields = ('title', 'content', 'writer', 'submenu_id')

