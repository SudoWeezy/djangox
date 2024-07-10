from django.urls import path
from . import methods

def generate_urlpatterns(module):
    urlpatterns = []
    for attr_name in dir(module):
        view = getattr(module, attr_name)
        if callable(view) and hasattr(view, 'url_pattern'):
            urlpatterns.append(
                path(view.url_pattern, view, name=attr_name)
            )
    return urlpatterns

urlpatterns = generate_urlpatterns(methods)



# urlpatterns = [
#     path("dog_picture/", methods.dog_picture, name="dog_picture"),
#     path('random_user/', methods.random_user, name='random_user'),
#     path('blog_create/', methods.blog_create, name='blog_create'),
#     path('blog_delete/<int:pk>/', methods.blog_delete, name='blog_delete'),
#     path('login/options/', methods.login_options, name='login_options'),
#     path('register/', methods.register, name='register'),
#     path('user_login/', methods.user_login, name='user_login'),
#     path('user_logout/', methods.user_logout, name='user_logout'),
#     # path('show_initial_login_form/', methods.show_initial_login_form, name='show_initial_login_form'),
#     # path('register/options/', methods.register_options, name='register_options'),
#     # path('register/complete/', methods.register_complete, name='register_complete'),
#     # path('login/options/', methods.login_options, name='login_options'),
#     # path('login/complete/', methods.login_complete, name='login_complete'),
# ]