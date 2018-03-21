from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import TopMenu, SubMenu, Greeting, Member, Lab, Project, DemoResource, Publication, Patent, Notice, News, Gallery, Community, RelatedProject, AutoNews, CompanyList

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator

from .forms import CommunityForm
# Create your views here.

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
    paginate_by = 10
    queryset = AutoNews.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AutomaticNews, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

    def get(self, request):
        context = {'company_list' : CompanyList.objects.all()}
        return render(request, self.template_name, context)

class AutomaticNewsList(ListView):
    model = AutoNews
    template_name = 'web/automaticnews_list.html'
    paginate_by = 10
    queryset = AutoNews.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AutomaticNews, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

    def get(self, request, company):
        filter_list = filter(lambda x: x.company == company, AutoNews.objects.all())
        context = {'filter_list' : filter_list}
        return render(request, self.template_name, context)

class AutomaticNewsDetail(DetailView):
    model = AutoNews
    template_name = 'web/automaticnews_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AutomaticNewsDetail, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

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
