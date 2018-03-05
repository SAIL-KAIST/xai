from django.db import models
#from django_summernote import models as summer_model
#from django_summernote import fields as summer_fields

# Create your models here.

# - Home
# - About
#     - Greeting(page)
#     - Member(list)
#     - Lab(list)
#     - Project(page)
# - Research
#     - LectureNote(imagelist,video)
#     - LectureVideo(imagelist)
#     - DemoResource(imagelist)
#     - Publication(textlist)
#     - Patent(textlist)
#     - Report(textlist)
# - News&Info
#     - Notice(textlist)
#     - News(imagelist)
#     - Gallery(imagelist)
#     - Community(board)
# - OPEN SOURCE
#     - Github(textlist)
#     - Related Project(imagelist)
# - Contact(page)

class TopMenu(models.Model):
    title = models.CharField(max_length=100)

    class meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class SubMenu(models.Model):
    title = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey('TopMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

# About
class Greeting(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content= models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.TextField()
    education = models.TextField()
    career = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)
    # IMAGE UPLOAD
    testImage = models.ImageField(upload_to="member", default='noImage')

    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=100, null=True)
    professor = models.CharField(max_length=45)
    research_on = models.TextField()
    link = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class DemoResource(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Patent(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

# News&Info
class Notice(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentk = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Community(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Github(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class RelatedProject(models.Model):
    title = models.CharField(max_length=200, null=True)
    Institutions = models.CharField(max_length=45)
    Authors = models.CharField(max_length=200, null=True)
    Publication_title = models.CharField(max_length=200, null=True)
    Publication_link = models.CharField(max_length=200, null=True)
    Sourcecode =models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='RelatedProject/')
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class AutoNews(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50, default='auto')
    datetime = models.DateTimeField()
    content = models.TextField()
    image_raw = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_predict = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    report_pdf = models.FileField(upload_to='AutomaticNews/%Y/%m/%d')
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
