from django.shortcuts import render
from mygallery.models import pics
from django.http  import HttpResponse, Http404


def displayimage(request):
    resultsdisplay = pics.objects.all()
    return render(request, 'home.html',{'pics':resultsdisplay})
# def single(request,desc_name,image_id):
#     # images = Image.get_image_by_id(image_id)
#     title = 'Image'
#     # category = Category.get_category_id(id = image_category)
#     image_desc = pics.objects.filter(image_desc__name = desc_name)
#     try:
#         image = pics.objects.get(id = image_id)
#     except:
#         raise Http404()
#     return render(request,"single.html",{'title':title,"image":image,"image_desc":image_desc})
# def gallery(request):
#     user = request.user
#     category = request.GET.get('category')
#     if category == None:
#         photos = pics.objects.filter(category__user=user)
#     else:
#         photos = pics.objects.filter(
#             category__name=category, category__user=user)

#     location = Location.objects.filter(user=user)
#     context = {'location': location, 'photos': photos}
#     return render(request, 'home.html', context)


def viewPhoto(request):
   
    return render(request, 'single.html')
