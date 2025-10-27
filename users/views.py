from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def logout_views(request):
    logout(request)
    return HttpResponseRedirect(render("learning_logs:index"))
