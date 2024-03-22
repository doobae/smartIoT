from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# from kakao.forms import KaKaoTalkForm
import json
import requests
from django.contrib import messages
client_id = "85bc3c0185aee494dedacd1cc7f82c33" # 자신의 REST KEY
class KakaoLoginView(TemplateView):
template_name = "kakao_login.html"
def get_context_data(self, **kwargs):
context = super().get_context_data(**kwargs)
context["client_id"] = client_id
return context