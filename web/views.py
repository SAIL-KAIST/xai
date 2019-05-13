from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from datetime import timedelta, datetime


from .models import TopMenu, SubMenu, Greeting, Member, Lab, Project, DemoResource, Publication, Patent, Notice, News, Gallery, Community, RelatedProject, AutoNews, CompanyList

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

from .forms import CommunityForm

def index(request):
    # topMenus = TopMenu.objects.all()
    # subMenuDict = dict()
    # for topMenu in topMenus:
    #     subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
    #     subMenuDict[topMenu.title] = subMenus
    # return render(request, 'web/index.html', {'topMenus' : topMenus, 'subMenuDict' : subMenuDict})

    return render(request, 'web/index.html', {'subMenuDict':getSubMenuDict()})

def getSubMenuDict():
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.title] = subMenus
    return subMenuDict

# def menu_detail(request, topMenu):
#     topMenu_id = TopMenu.objects.get(title=topMenu)
#     subMenus = get_list_or_404(SubMenu, topmenu_id=topMenu_id.pk)
#     return render(request, 'web/menu_detail.html', {'topMenu': topMenu, 'subMenus': subMenus })

#ABOUT##########################################################################################################################
class GreetingPage(TemplateView):
    model = Greeting
    template_name = 'web/greetingTemp.html'

    def get_context_data(self, **kwargs):
        context = super(GreetingPage, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class MemberImageList(ListView):
    model = Member
    template_name = 'web/memberTemp.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'member_list'
    paginate_by = 5
    queryset = Member.objects.order_by('-id')  

    # context={ 'context_object_name':'news_list', 'subMenuDict':getSubMenuDict() }
    def get_context_data(self, **kwargs):
        context = super(MemberImageList, self).get_context_data(**kwargs)
        context['object_name'] = 'member_list'
        context['subMenuDict'] = getSubMenuDict()
        return context

class LabTextList(ListView):
    model = Lab
    template_name = 'web/lab.html'

    def get_context_data(self, **kwargs):
        context = super(LabTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class ProjectPage(TemplateView):
    model = Project
    template_name = 'web/projectTemp.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectPage, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

#NEWS&INFO##########################################################################################################################
class NoticeTextList(ListView):
    model = Notice
    template_name = 'web/notice.html'

    def get_context_data(self, **kwargs):
        context = super(NoticeTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NewsImageList(ListView):
    model = News
    template_name = 'web/news.html'  # Default: <app_label>/<model_name>_list.html
    queryset = News.objects.order_by('-id')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(NewsImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class GalleryImageList(ListView):
    model = Gallery
    template_name = 'web/imagelist.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context


#RESEARCH##########################################################################################################################
class DemoresourceImageList(ListView):
    model = DemoResource
    template_name = 'web/demoresource.html'

    def get_context_data(self, **kwargs):
        context = super(DemoresourceImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class AutomaticNews(ListView):
    model = CompanyList
    template_name = 'web/automaticnews.html'
    paginate_by = 5
    queryset = AutoNews.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(NewsImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

    def get(self, request):
        context = {'company_list' : CompanyList.objects.all()}
        return render(request, self.template_name, context)

class AutomaticNewsList(ListView):
    model = AutoNews
    template_name = 'web/automaticnews_list.html'
    queryset = AutoNews.objects.order_by('-id')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(NewsImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

    def get(self, request, company):
        filters = list(filter(lambda x: x.company == company, AutoNews.objects.all()))
        filters.reverse()
        paginator = Paginator(filters, self.paginate_by)
        page = request.GET.get('page')
        #if your django version 2.0.4 just you get_page
        if page == None:
            page = 1
        filter_list = paginator.page(page)

        # counting page number
        if filter_list.has_next() == False :
            acc_num = 0
        else :
            mod = paginator.count % self.paginate_by
            acc_num = (paginator.num_pages-int(page)-1) * self.paginate_by + mod

        context = {'filter_list': filter_list, 'acc_num' : acc_num}
        return render(request, self.template_name, context)

class AutomaticNewsDetail(DetailView):
    model = AutoNews
    template_name = 'web/automaticnews_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AutomaticNewsDetail, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

    def get(self, request, pk):
        autonews = AutoNews.objects.get(pk = pk)
        my_company = autonews.company
        my_datetime = autonews.datetime
        my_subid = autonews.submenu_id_id
        predict_date = my_datetime.date()+timedelta(days=28)
        today = datetime.today().date()
        is_future = predict_date > today

        predict = AutoNews.objects.filter(company=my_company, datetime__icontains=predict_date).values('id')
        predict_id = predict.values('id')
        predict_pk = 0
        if(predict_id.exists()) :
            predict_pk = predict_id[0]['id']

        context = {'autonews':autonews, 'predict_pk':predict_pk, 'is_future':is_future,}
        return render(request, self.template_name, context)

def not_come(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.title] = subMenus
    return render(request, 'web/automaticnews_notcome.html', {'subMenuDict':getSubMenuDict()})

def not_exist(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.title] = subMenus
    return render(request, 'web/automaticnews_notexist.html', {'subMenuDict':getSubMenuDict()})

def stock(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.title] = subMenus
    return render(request, 'web/stockTemp.html', {'subMenuDict':getSubMenuDict()})

def Index(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.title] = subMenus
    return render(request, 'web/indexTemp.html', {'subMenuDict':getSubMenuDict()})

class PublicationTextList(ListView):
    model = Publication
    template_name = 'web/publication.html'

    def get_context_data(self, **kwargs):
        context = super(PublicationTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class PatentTextList(ListView):
    model = Patent
    template_name = 'web/patent.html'

    def get_context_data(self, **kwargs):
        context = super(PatentTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

#OPEN SOURCE##########################################################################################################################
def githubRedirect(request):
    return redirect('https://github.com/OpenXAIProject')

class RelatedProject(ListView):
    model = RelatedProject
    template_name = 'web/relatedproject.html'
    queryset = RelatedProject.objects.order_by('-id')
    paginate_by = 4 #how much show your list

    def get_context_data(self, **kwargs):
        context = super(RelatedProject, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

# Community
class CommunityBoard(ListView):
    model = Community
    template_name = 'web/community.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityBoard, self).get_context_data(**kwargs)
        context['object_name'] = 'community_list'
        context['subMenuDict'] = getSubMenuDict()
        return context

class CommunityDetail(DetailView):
    model = Community
    template_name = 'web/community_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityDetail, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

def community_new(request):
    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('community_detail', pk=post.pk)
    else:
        form = CommunityForm()
    return render(request, 'web/community_edit.html', {'form':form})

#Contact##########################################################################################################################
def Contact(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.title] = subMenus
    return render(request, 'web/contact.html', {'subMenuDict':getSubMenuDict()})

#### temporary use greeting model
class Symposium(TemplateView):
    model = Greeting
    template_name = 'web/Symposium18.html'

    def get_context_data(self, **kwargs):
        context = super(Symposium, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class Symposium_ko(TemplateView):
    model = Greeting
    template_name = 'web/Symposium18_ko.html'

    def get_context_data(self, **kwargs):
        context = super(Symposium_ko, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        context['subMenuDict'] = getSubMenuDict()
        return context

class Workshop19(TemplateView):
    model = Greeting
    template_name = 'web/workshop19.html'

    def get_context_data(self, **kwargs):
        context = super(Workshop19, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class Popup(TemplateView):
    model = Greeting
    template_name = 'web/popup.html'

    def get_context_data(self, **kwargs):
        context = super(Popup, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context