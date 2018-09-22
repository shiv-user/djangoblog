from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def posts_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request," Not created Try again!")


	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

	
def posts_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	context = {
		"title":instance.title,
		"instance":instance

	}

	return render(request,"post_detail.html",context)
def posts_list(request):
	queryset = Post.objects.all().order_by("timestamp")
	paginator = Paginator(queryset, 5)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)

		
	context = {
		"object_list":queryset,
		"title":"List",

	}

	return render(request,"post_list.html",context)




def posts_update(request,id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())
        
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def posts_delete(request,id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"successfully Created")
	return redirect("posts:list") 