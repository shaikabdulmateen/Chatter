from django.shortcuts import render
from .models import Tweet ,Like ,Comment
from .forms import TweetForm , UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout
# Create your views here.

@login_required
def index(request):
    return  render(request, 'index.html')

@login_required
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')

    liked_tweet_ids = set(
        Like.objects.filter(
            user=request.user
        ).values_list('tweet_id', flat=True)
    )

    return render(
        request,
        'tweet_list.html',
        {
            'tweets': tweets,
            'liked_tweet_ids': liked_tweet_ids,
        }
    )


@login_required
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    liked = Like.objects.filter(
        user=request.user,
        tweet=tweet
    ).exists()

    return render(
        request,
        'tweet_detail.html',
        {
            'tweet': tweet,
            'liked': liked,
        }
    )



@login_required()
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()

            return redirect('tweet_list')

    else:
        form = TweetForm()

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else :
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        if tweet.image:
            tweet.image.delete(save=False)

        tweet.delete()
        return redirect('tweet_list')

    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    like = Like.objects.filter(user=request.user, tweet=tweet).first()

    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, tweet=tweet)

    return redirect('tweet_list')


@login_required
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()

        if text:
            Comment.objects.create(
                user=request.user,
                tweet=tweet,
                text=text
            )

    return redirect('tweet_list')




@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        user=request.user
    )

    if request.method == 'POST':
        comment.delete()

    return redirect('tweet_list')



@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(
        Comment,
        pk=comment_id,
        user=request.user
    )

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()

        if text:
            comment.text = text
            comment.save()

    return redirect('tweet_list')