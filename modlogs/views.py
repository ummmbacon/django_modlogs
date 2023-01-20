# modlogs/views.py
from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import ModLog

import praw
from environs import Env

env = Env()
env.read_env()


class Home(TemplateView):
    template_name = "home.html"


def index(request, subreddit):
    reddit = praw.Reddit(
        client_id=env('REDDIT_CLIENT_ID'),
        client_secret=env('REDDIT_CLIENT_SECRET'),
        password=env('REDDIT_PASSWORD'),
        user_agent=env('REDDIT_USER_AGENT'),
        username=env('REDDIT_USERNAME'),
    )

    template = loader.get_template('index.html')

    try:
        for log in reddit.subreddit(subreddit).mod.log(limit=10):
            if not ModLog.objects.filter(unique_id=log.id).exists():
                new_log = ModLog()
                new_log.unique_id = log.id
                new_log.mod_name = log.mod
                new_log.sub_user = log.target_author
                new_log.sub_name = log.subreddit
                new_log.mod_action = log.action
                new_log.time = log.created_utc
                new_log.mod_item = log.target_body
                new_log.mod_link = 'http://www.reddit.com' + str(log.target_permalink)
    except:
        return HttpResponse("Not a Mod of that sub")

    all_logs = ModLog.objects.filter(sub_name=subreddit)
    context = {'log_list': all_logs}

    return HttpResponse(template.render(context, request))
