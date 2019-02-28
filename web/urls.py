from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<subMenu>.+)/$', views.subMenu, name='subMenu'),

    # List
    url(r'^about/greeting/$', views.GreetingPage.as_view(), name='greeting'),
    url(r'^about/member/$', views.MemberImageList.as_view(), name='member'),
    url(r'^about/lab/$', views.LabTextList.as_view(), name='lab'),
    url(r'^about/project/$', views.ProjectPage.as_view(), name='project'),

    url(r'^news&info/notice/$', views.NoticeTextList.as_view(), name='notice'),
    url(r'^news&info/news/$', views.NewsImageList.as_view(), name='news'),
    url(r'^news&info/gallery/$', views.GalleryImageList.as_view(), name='gallery'),

    url(r'^research/automatic_news/$', views.AutomaticNews.as_view(), name='autonews'),
    url(r'^research/automatic_news/list/(?P<company>.+)/$', views.AutomaticNewsList.as_view(), name='autonews_list'),
    url(r'^research/automatic_news/detail/(?P<pk>\d+)/$', views.AutomaticNewsDetail.as_view(), name='autonews_detail'),

    # url(r'^research/demoresource/$', views.DemoresourceImageList.as_view(), name='demoresource'),
    url(r'^research/unist_index/$', views.Index, name='unist_index'),
    url(r'^research/publication/$', views.PublicationTextList.as_view(), name='publication'),
    url(r'^research/patent/$', views.PatentTextList.as_view(), name='patent'),

    #opensource
    url(r'^opensource/github/$', views.githubRedirect, name='github'),
    url(r'^opensource/relatedproject/$', views.RelatedProject.as_view(), name='relatedproject'),
    url(r'^opensource/community/$', views.CommunityBoard.as_view(), name='community'),
    url(r'^opensource/community/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='community_detail'),
    url(r'^opensource/community/new/$', views.community_new, name='community_new'),

    # Symposium
    url(r'^Symposium/2018/$', views.Symposium.as_view(), name='2018Symposium'),
    url(r'^Symposium/2018/korean/$', views.Symposium_ko.as_view(), name='2018Symposium_ko'),
    url(r'^popups/2018/$', views.Popup.as_view(), name='popup'),

    #contact
    url(r'^contact/$', views.Contact, name='contact'),
]
