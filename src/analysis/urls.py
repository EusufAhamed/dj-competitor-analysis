from django.urls import path

from analysis import views

app_name = 'analysis'

urlpatterns = [
    path('get-local-finder', views.get_local_finder),
    path('post-local-finder', views.post_local_finder),
    path('get-business-info', views.get_business_info),
    path('post-business-info', views.post_business_info),
    path('get-reviews', views.get_reviews),
    path('post-reviews', views.post_reviews),

]