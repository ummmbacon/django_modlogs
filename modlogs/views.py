# modlogs/views.py
from django.template import loader
from django.http import StreamingHttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from datetime import datetime

from .models import ModLog


class Home(TemplateView):
    template_name = "home.html"


def index(request, subreddit):
    template = loader.get_template('index.html')
    all_logs = ModLog.objects.filter(sub_name=subreddit).order_by('-mod_time__date', '-mod_time__time')
    context = {'log_list': all_logs}

    return StreamingHttpResponse(template.render(context, request))


class SearchResultsListView(ListView):
    model = ModLog
    context_object_name = 'log_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        return ModLog.objects.filter(
            Q
        )
