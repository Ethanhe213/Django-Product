from django.shortcuts import render
from profiles.models import Profile
from django.http import JasonResponse
from .utils import get_report_image
from .models import Report
# Create your views here.
def create_report_view(request):
    if request.is_ajax():
        name=request.POST.get('name')
        remark=request.POST.get('remarks')
        image=request.POST.get('image')
        img=get_report_image(image)
        author=Profile.objects.get(user=request.user)
        Report.objects.create(name=name,remarks=remark,image=img,author=author)
        return JasonResponse({'msg':'send'})
    return JasonResponse({})