from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.


class BlogUser(AbstractUser):
    nickname = models.CharField(max_length=100, verbose_name='昵称', blank=True)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)
    qq = models.CharField(max_length=100, verbose_name='QQ号码', blank=True, null=True)
    mobile = models.CharField(max_length=11, verbose_name='手机号码', blank=True, null=True)
    
    class Meta:
        verbose_name='用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']
    
    def __str__(self):
        return self.username
    

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '已发布')
    )
    
    title = models.CharField(max_length=255, verbose_name='标题', unique=True)
    desc = models.CharField(max_length=1024, verbose_name='描述')
    body = models.TextField(verbose_name='正文')
    pub_time = models.DateTimeField(blank=True, null=True, verbose_name='发布时间')
    status = models.CharField(max_length=1, verbose_name='文章发布状态', choices=STATUS_CHOICES, default='d')
    view_num = models.PositiveIntegerField(verbose_name='浏览次数', default=0)
    allow_comment = models.BooleanField(verbose_name='是否允许评论', default=True)
    allow_feed = models.BooleanField(verbose_name='是否允许出现在聚合中', default=True)
    order = models.IntegerField(default=999, verbose_name='优先级')
    password = models.CharField(max_length=1024, verbose_name='密码', blank=True, null=True)
    author = models.ForeignKey('BlogUser', verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True)
    
    class Meta:
        ordering = ['-pub_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称', unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True, verbose_name='缩略名')
    order = models.IntegerField(default=999, verbose_name='优先级')
    level = models.IntegerField(default=1, verbose_name='分类等级') # 表示其是几级标签
    parent_category = models.ForeignKey('self', verbose_name='父级分类', blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['order', 'id']
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称', unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True, verbose_name='缩略名')
    order = models.IntegerField(default=999, verbose_name='优先级')
    level = models.IntegerField(default=1, verbose_name='标签级别')
    parent_tag = models.ForeignKey('self', verbose_name='父级标签', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name

