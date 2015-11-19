from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.base import View
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from chat.forms import LoginForm, ChatForm
from chat.models import Message, MessageUserList


class SignUpView(View):
    """
    Sign Up from for user
    """
    form_class = UserCreationForm
    context = {}
    
    def get(self, request):
        self.context['form'] = self.form_class
        return render_to_response('signup.html', self.context,\
                                  context_instance = RequestContext(request))
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
        self.context['form'] = form
        return render_to_response('signup.html', self.context,\
                                  context_instance = RequestContext(request))
# Create your views here.
class LoginView(View):
    """
    Login Form
    for all user
    """
    template_name = 'login.html'
    form_class = LoginForm
    context = {}
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        form = self.form_class()
        self.context['form'] = form 
        return render_to_response(self.template_name, self.context,\
                                  context_instance = RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        if form.is_valid():
            user = authenticate(username=user_name, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        self.context['form'] = form 
        return render_to_response(self.template_name, self.context,\
                                  context_instance = RequestContext(request))


class LogOutView(View):
    """
    Log out View
    """
    @method_decorator(login_required)
    def get(self, request):
        logout(request)

        return HttpResponseRedirect(reverse('login'))


class ChatView(View):
    """
    Home page
    """
    template_name = 'chat/chat.html'
    form_class = ChatForm
    context = {}
    
    @method_decorator(login_required)
    def get(self, request, user_id=None):
        """
        Populate right side data, mid data and left data
        """
        self.context['message_list'] = None
        self.context['form'] = None
        if user_id:
            message_list = Message.objects.filter(Q(Q(from_user=request.user)| Q(to_user=request.user)) \
                                                  & Q(Q(from_user__id=user_id)| Q(to_user=user_id))).order_by('created_time')
            self.context['message_list'] = message_list
            self.context['form'] = self.form_class(initial={'to_user': user_id})
        all_user_list = User.objects.exclude(id=request.user.id)
        unique_user_list = MessageUserList.objects.filter(requested_user=request.user).order_by('to_user','-created_time').distinct('to_user')
        self.context['all_user_list'] = all_user_list
        self.context['unique_user_list'] = unique_user_list
        return render_to_response(self.template_name, self.context,\
                                  context_instance = RequestContext(request))
    
    @method_decorator(login_required)
    def post(self, request, user_id=None):
        """
        Send message to other user
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.to_user = get_object_or_404(User, id=user_id)
            form.instance.from_user = request.user
            form.save()
            return HttpResponseRedirect(reverse('user_list', args=[user_id]))
        message_list = Message.objects.filter(Q(Q(from_user=request.user)| Q(to_user=request.user)) \
                                              & Q(Q(from_user__id=user_id)| Q(to_user=user_id))).order_by('created_time')
        self.context['message_list'] = message_list
        self.context['form'] = form
        all_user_list = Message.objects.filter(Q(from_user=request.user)| Q(to_user=request.user)).order_by('-created_time')
        unique_user_list = MessageUserList.objects.filter(requested_user=request.user).distinct('to_user').order_by('-created_time')
        self.context['all_user_list'] = all_user_list
        self.context['unique_user_list'] = unique_user_list
        return render_to_response(self.template_name, self.context,\
                                  context_instance = RequestContext(request))
            