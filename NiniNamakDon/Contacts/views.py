from django.shortcuts import render
from .models import Company,Preson
# Create your views here.


def ContactList(request):
    Q1 = Company.objects.filter(FullName__isnull=False).values_list('id','FullName')
    Q2 = Preson.objects.all().values_list('id','FullName')

    Q3 = Q1.union(Q2)

    context = {
        # 'ContactOne': ContactOne,
        'ContactAll': Q3
    }
    return render(request, 'Contacts/ContactList.html', context)

def ContactListDitel(request,Contact_id):
#     q = Company.objects.get(pk=Contact_id)
    context = {
        # 'ContactOne': ContactOne,
        # 'qq': q
    }
    return render(request, 'Contacts/ContactListDetil.html', context)    