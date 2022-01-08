from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from django.contrib import messages


def home(request):
    posts = Post.objects.filter(published=True).order_by('-timestamp')
    return render(request, 'coreapp/home.html', {'posts': posts})

 
def dashboard(request):
    posts = Post.objects.filter(owner=request.user)
    return render(request, 'coreapp/dashboard.html', {'posts': posts})


def addpost(request):

    if request.method == 'POST':
        post = Post()

        post.title = request.POST['title']
        post.description = request.POST['description']
        post.published = request.POST['published']
        post.owner = request.user

        post.save()
        if post:
            messages.success(request, 'Post added successfully')
            return redirect('/dashboard#dashboard')

    return render(request, 'coreapp/addpost.html')

def editpost(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'coreapp/editpost.html', {'post': post})

def updatepost(request, id):
    post = Post.objects.get(id=id)
    post.title = request.POST['title']
    post.description = request.POST['description']
    post.published = request.POST['published']
    post.save()
    if post:
        messages.success(request, 'Post updated successfully')
        return redirect('/dashboard#dashboard')

    return render(request, 'coreapp/editpost.html')

def deletepost(request, id):
    post = Post.objects.get(id=id).delete()
    
    if post:
        messages.success(request, 'Post deleted successfully')
        return redirect('/dashboard#dashboard')

    return render(request, 'coreapp/dashboard.html')

def published(request, id):
    post = Post.objects.get(id=id)
    post.published = True
    post.save()
    if post:
        messages.success(request, 'Post published successfully')
        return redirect('/dashboard#dashboard')

    return render(request, 'coreapp/dashboard.html#dashboard')


def unpublished(request, id):
    post = Post.objects.get(id=id)
    post.published = False
    post.save()
    if post:
        messages.success(request, 'Post unpublished successfully')
        return redirect('/dashboard#dashboard')

    return render(request, 'coreapp/dashboard.html#dashboard')











# class TestView(APIView):
    
#     permissions_classes = (IsAuthenticated,)
    
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# def home(request):
    # if request.method == 'POST':
    #     appkey = request.POST.get('appkey')
    #     secretkey = request.POST.get('secretkey')
        
    #     payload = {
    #         "client_id": appkey,
    #         "client_secret": secretkey,
    #         "grant_type": "client_credentials"
    #     }

    #     r = requests.post('https://api.yotpo.com/oauth/token', data=payload)
    #     context = {
    #         'utoken': r.json()['access_token'],
    #         }       
    #     return render(request, 'home.html', context)
    
    # data = {
    #     'name': 'john',
    #     'age': '25',
    # }
    # return JsonResponse(data)    
    # return render(request, 'home.html')

# def result(request):
#     return render(request, 'result.html')

# def uploadcsv(request):
    
#     # form = CsvModelForm(request.POST or None, request.FILES or None)
#     # # return render(request, 'uploadcsv.html', {'form': form})
#     # if form.is_valid():
#     #     form.save()
#     #     form = CsvModelForm()
#     #     # messages.success(request, 'Your file has been uploaded successfully')
#     #     # return redirect('/')
    
#     with open(os.path.join(settings.MEDIA_ROOT, 'uploaded.csv'), 'r', encoding="utf-8") as f:
#         reader = csv.reader(f)
#         next(reader)
#         data = {"products_orders": []}
#         for row in reader:
#             data['products_orders'].append({
#                'email': row[0],'customer_name': row[1], 'order_id': row[2], 'order_date': row[3], 'product_id': row[4], 'product_url': row[5], 'product_title': row[6] 
#             })
#         # print(row)
    
#     # with open ("product_orders.json", 'w', encoding="utf-8") as f:
#     #     payload = json.dump(data, f, indent=4)
#     #     # return HttpResponse(outputjson, content_type="application/json")
        
    
#     # if request.method == 'POST':
#         # appkey = request.POST.get('appkey')
#         # secretkey = request.POST.get('secretkey')
        
        

#         r = requests.post('https://api.yotpo.com/apps/pX24FKZoDxZliIxSRQQyJJpC4RFUyRNePwdgWzv5/purchases/', data=data)
#         context = {
#             'response': r.status_code,
#             }
#         if r.status_code == 200:
#             messages.success(request, 'Your file has been uploaded successfully')
#             return render(request, 'result.html', context)
#         else:
#             messages.error(request, 'Something went wrong')
#             return render(request, 'result.html', context)
#     return render(request, 'uploadcsv.html', context)
    
    