# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/10/16


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# class LoginRequiredMixin(object):
#     @method_decorator(login_required(login_url='/login/'))
#     def dispath(self, request, *args, **kwargs):
#         return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **init_kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**init_kwargs)
        return login_required(view)