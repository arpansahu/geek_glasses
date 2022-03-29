from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(redirect_field_name='')
def home(request):
    if request.user.is_authenticated and not request.user.is_kycied:
        return render(request, 'account/getkyc.html')
    return render(request, 'Home.html')
