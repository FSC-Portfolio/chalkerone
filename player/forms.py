from django import forms


class UpdateProfile(forms.Form):
    big_name = forms.CharField(label='Your big name', max_length=255)
    player_club = forms.ChoiceField(label='Your club')
    cc_notes = forms.ChoiceField(label='Quick quote that describes you')
