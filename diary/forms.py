from django import forms
from .models import Day


class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'  # ('title', 'text', 'date')



class SearchForm(forms.Form):
    # year = forms.ChoiceField(choices=[('', '---')], required=False)
    # month = forms.ChoiceField(choices=[('', '---')], required=False)
    # day = forms.ChoiceField(choices=[('', '---')], required=False)
    search = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        # year_choices = [('','---')] + sorted(list(set([(str(year.year), str(year.year)) for year in Day.objects.dates('date', 'year').distinct()])), key=lambda x: int(x[0]))
        # month_choices = [('','---')] + sorted(list(set([(str(month.month), month.strftime('%B')) for month in Day.objects.dates('date', 'month').distinct()])), key=lambda x: int(x[0]))
        # day_choices = [('','---')] + sorted(list(set([(str(day.day), str(day.day)) for day in Day.objects.dates('date', 'day').distinct()])), key=lambda x: int(x[0]))

        # self.fields['year'].choices = year_choices
        # self.fields['month'].choices = month_choices
        # self.fields['day'].choices = day_choices
