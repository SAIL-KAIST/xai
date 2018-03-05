from django.contrib import admin
from web.models import TopMenu, SubMenu, Greeting, Member, Lab, Project, DemoResource, Publication, Patent, Notice, News, Gallery, Community, Github, RelatedProject, AutoNews

# Register your models here.

admin.site.register(TopMenu)
admin.site.register(SubMenu)

admin.site.register(Greeting)
admin.site.register(Member)
admin.site.register(Lab)
admin.site.register(Project)

admin.site.register(DemoResource)
admin.site.register(Publication)
admin.site.register(Patent)

admin.site.register(Notice)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Community)

admin.site.register(Github)
admin.site.register(RelatedProject)
admin.site.register(AutoNews)