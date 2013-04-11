from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render;
from models import LinkGroup

def index( request ):
    group_list = LinkGroup.objects.order_by('created_date')
    context = Context({
        'group_list': group_list,
    })
    template = loader.get_template('faves/index.html')
    render = template.render( context )
    return HttpResponse( render )

def group( request, group_id ):
    try:
        group = LinkGroup.objects.get( pk = group_id )
    except LinkGroup.DoesNotExist:
        raise Http404
    return render( request, 'faves/group.html', { 'group': group })

def link( request, link_id ):
    return HttpResponse( 'The Link Detail page')


def redir( request, link_id ):
    return HttpResponse( 'This is the redir page' )

