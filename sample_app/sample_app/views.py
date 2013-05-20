from django.contrib.sites.models import Site
from django.shortcuts import render_to_response

from objectcounters.models import Counter


def home(request):
    site = Site.objects.get_current()
    counter, created = Counter.objects.create_for_object('visits', site)
    counter.value += 1
    counter.save()

    # The template won't get the counter, but can query it with the template
    # tag.  Obviously, if you've got the counter like we do here, you would pass
    # it through to the template.  But this is an example, so we don't.
    return render_to_response('home.html', {'site':site})
