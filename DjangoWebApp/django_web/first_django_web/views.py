from django.shortcuts import render
from first_django_web.models import Topic, Webpage, AccessRecord, PeopleRecord
from first_django_web import forms


# Create your views here.
def home(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'home.html', context=date_dict)


def user(request):
    people_list = PeopleRecord.objects.order_by('First_Name')
    people_dict = {'people_records': people_list}
    return render(request, 'user.html', context=people_dict)


def form_name_view(request):
    form = forms.NewUserForm()
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("ERROR")
    return render(request, 'user_input.html', {'form': form})
