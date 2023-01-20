from django.core.management.base import BaseCommand, CommandError
from modlogs.models import ModLog

import praw
from datetime import datetime
from environs import Env

env = Env()
env.read_env()

class Command(BaseCommand):
    help = '--limit, sets limit on number of logs, --subbreddit, specify a specif sub to pull from; default all'

    def add_arguments(self, parser):
        parser.add_argument('--subreddit', type=str, help='Specify the Sub')
        parser.add_argument('--limit', type=int, help='Specify a limit')


    def handle(self, subreddit=None, limit=None, **kwargs):
        reddit = praw.Reddit(
            client_id=env('REDDIT_CLIENT_ID'),
            client_secret=env('REDDIT_CLIENT_SECRET'),
            password=env('REDDIT_PASSWORD'),
            user_agent=env('REDDIT_USER_AGENT'),
            username=env('REDDIT_USERNAME'),
        )

        mod_list = []

        for sub in reddit.user.me().moderated():
            mod_list.append(sub.display_name)

        if options['subreddit']:

        elif options['subreddit', 'limit']:

        else:
            try:
                for log in reddit.subreddit("mod").mod.stream.log():
                    if not ModLog.objects.filter(unique_id=log.id).exists():
                        new_log = ModLog()
                        new_log.unique_id = log.id
                        new_log.mod_name = log.mod
                        new_log.sub_user = log.target_author
                        new_log.sub_name = log.subreddit
                        new_log.mod_action = log.action
                        new_log.time = datetime.utcfromtimestamp(log.created_utc)
                        new_log.mod_item = log.target_body
                        new_log.mod_link = 'http://www.reddit.com' + str(log.target_permalink)
                        new_log.save()

            except Exception as e:
                raise CommandError(e)


