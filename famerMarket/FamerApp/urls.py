from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='index'),
    path('get_by_entry/', views.GetByEntry.as_view(), name='get_by_entry'),
    path('all_market/', views.AllMarketView.as_view(), name='all_market'),
    path('infos_market/<str:marketname>', views.DetailMarket.as_view(), name='infos_market'),
    path('comment/<str:marketname>', views.CommentView, name="comment"),
    path('delete_comment/<str:marketname>', views.DeleteCommentView, name="delete_comment"),
    path('rates/', views.SortByEntry.as_view(), name="rates"),
]
