from django.urls import path, re_path
from jobs import views

urlpatterns = [
    # 职位列表
    re_path(r"^joblist/", views.joblist, name="joblist"),
    re_path(r"^job/(?P<job_id>\d+)/$", views.detail, name='detail')
]
