from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('test/', test, name='test'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('add_news/', add_news, name='add_news'),
    path('add_prep/', add_prep, name='add_prep'),
    path('add_test/', add_test, name='add_test'),
    path('add_basic_data/', add_basic_data, name='add_basic_data'),
    path('opn_main_window/add_test_data/', add_test_data, name='add_test_data'),
    path('opn_main_window/', opn_main_window, name='opn_main_window'),
    path('opn_main_window/add_goals/', add_goals, name='add_goals'),
    path('opn_main_window/add_plan_res_ed/', add_plan_res_ed, name='add_plan_res_ed'),
    path('opn_main_window/connect_db/', connect_db, name='connect_db'),
    path('opn_main_window/bd_test/', bd_test, name='bd_test'),
    path('opn_main_window/parsing_book/', parsing_book, name='parsing_book'),
    path('opn_main_window/get_comp/', get_comp, name='get_comp'),
    path('opn_main_window/get_commp/', get_commp, name='get_commp')
]
