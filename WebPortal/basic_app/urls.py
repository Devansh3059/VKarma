from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name= 'register'),
    url(r'^user_login/$',views.user_login,name= 'user_login'),
    url(r'^home_profile/$',views.home_profile,name= 'home_profile'),
    url(r"^update_profile/$", views.AddDetail, name="addDetail"),
    url(r"^student_detail/$", views.StudentDetailView.as_view(), name="view_details"),
    url(r"^delete/$", views.DeleteUserProfile, name="deleteDetails"),
]