from django.shortcuts import redirect
from django.views.generic import  ListView
from django.views import  View

from bookstore.models import Publisher,UploadFileForm,UploadFileModelField
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

class PublisherListView(ListView):
    model = Publisher

class GreetingView(View):
    greeting = "good Day"
    def get(self,request,*args,**kwargs):
        return  HttpResponse(f'{self.greeting},{str(args)},{str(kwargs)}')

class ArticlesView(View):
    def get(self,request,*args,**kwargs):
        return  HttpResponse(f'{str(args)},{str(kwargs)}')

    def post(self,request,*args,**kwargs):
        print('post')
        return  HttpResponse(f'{str(args)},{str(kwargs)}')

class UploadFileView(View):
    def post(self,request):
        form = UploadFileModelField(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            form.save()
            # upload_file = form.cleaned_data['file']
            # # 在这里可以进行文件保存等操作，例如：
            # with open(upload_file.name, 'wb+') as destination:
            #     for chunk in upload_file.chunks():
            #         destination.write(chunk)
            return  HttpResponse(f'{title}ok')
        else:
            return HttpResponse('not ok')

class redirectView(View):
    def get(self,request):
        return redirect("http://www.qq.com")