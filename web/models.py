from django.db import models
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

#ABOUT##########################################################################################################################
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

#NEWS&INFO##########################################################################################################################
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
    date = models.DateField()
    content = models.TextField()
    link = models.TextField()
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

#RESEARCH##########################################################################################################################
class DemoResource(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class AutoNews(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    content = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    prediction = models.TextField()
    image_raw = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_predict = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_first = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_second = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    image_third = models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')
    report_pdf = models.FileField(upload_to='AutomaticNews/%Y/%m/%d')
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    journal = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Patent(models.Model):
    title = models.CharField(max_length=100)
    inventor = models.CharField(max_length=45)
    nation = models.CharField(max_length=45)
    date = models.DateField()
    number = models.TextField()
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

#OPEN SOURCE##########################################################################################################################
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
    Related_link = models.CharField(max_length=200, null=True)
    Sourcecode =models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='RelatedProject/')
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Community(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    content = models.TextField()
    submenu_id = models.ForeignKey('SubMenu', on_delete=models.PROTECT, default=13)

    def __str__(self):
        return self.title

class CompanyList(models.Model):
    company_kor = models.TextField()
    company_eng = models.TextField()
