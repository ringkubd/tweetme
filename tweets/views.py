import random
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

from .forms import TweetForm


# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")


def tweet_details_view(request, tweet_id):
    """
    REST API VIEW
    Consume by JavaScript, or Swift/Java
    """

    data = {
        "id": tweet_id
    }
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data["content"] = tweet.content
    except Tweet.DoesNotExist:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status=status)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript, or Swift/Java/IOS/Android
    """
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 100)} for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list
    }
    return JsonResponse(data)


def tweet_create_view(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()

    return render(request, 'components/form.html', {"form": form})
