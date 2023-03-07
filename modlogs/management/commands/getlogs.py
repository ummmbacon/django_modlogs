from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime
from modlogs.models import ModLog

import praw
from zoneinfo import ZoneInfo
from datetime import datetime
from environs import Env


env = Env()
env.read_env()


def save_logs(self, log):
    if not ModLog.objects.filter(unique_id=log.id).exists():
        new_log = ModLog()
        new_log.unique_id = log.id
        new_log.mod_name = log.mod
        new_log.sub_user = log.target_author
        new_log.sub_name = log.subreddit
        new_log.mod_action = log.action
        log.created_utc = parse_datetime(datetime.utcfromtimestamp(log.created_utc).
                                         strftime("%Y-%m-%d %H:%M:%S")).replace(tzinfo=ZoneInfo("UTC"))
        new_log.mod_time = log.created_utc
        new_log.mod_item = log.target_body
        new_log.mod_link = 'http://www.reddit.com' + str(log.target_permalink)
        new_log.save()
        self.stdout.write(f'saved new log {log.id}')


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

        if subreddit is not None:
            try:
                for log in reddit.subreddit(subreddit).mod.stream.log():
                    save_logs(self, log)

            except Exception as e:
                raise CommandError(e)

        elif limit is not None:
            try:
                for log in reddit.subreddit('mod').mod.log(limit=limit):
                    save_logs(self, log)

            except Exception as e:
                raise CommandError(e)

        elif subreddit is not None and limit is not None:
            try:
                for log in reddit.subreddit(subreddit).mod.log(limit=limit):
                    save_logs(self, log)

            except Exception as e:
                raise CommandError(e)
        else:
            try:
                for log in reddit.subreddit("mod").mod.stream.log():
                    save_logs(self, log)

            except Exception as e:
                raise CommandError(e)
