from django import forms

class SearchForm(forms.Form):
	query = forms.CharField(label="Search keywords", max_length=100)
