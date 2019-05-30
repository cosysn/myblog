#Mysql数据库表格设计
##博客用户 BlogUser


<table>
    <tr>
        <th>name</th>
        <th>real_name</th>
        <th>type</th>
        <th>是否为空</th>
        <th>外键</th>
        <th>是否为主键</th>
    </tr>
    <tr>
        <th>id</th>
        <th>编号</th>
        <th>IntgerField（32）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>是</th>
    </tr>
    <tr>
        <th>username</th>
        <th>用户名</th>
        <th>CharField（64）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>password</th>
        <th>登录密码</th>
        <th>CharField（64）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>gender</th>
        <th>性别</th>
        <th>CharField(男/女)（16）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>age</th>
        <th>年龄</th>
        <th>IntegerField（32）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>profession</th>
        <th>职业</th>
        <th>CharField（32）</th>
        <th>NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>telephone</th>
        <th>手机号</th>
        <th>CharField（32）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>email</th>
        <th>邮件</th>
        <th>CharField（32）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>introduction</th>
        <th>介绍</th>
        <th>TextField</th>
        <th>NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>createTime</th>
        <th>创建时间</th>
        <th>DateTimeField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>updateTime</th>
        <th>更新时间</th>
        <th>DateTimeField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
</table>

##博客信息表 Article
<table>
    <tr>
        <th>name</th>
        <th>real_name</th>
        <th>type</th>
        <th>是否为空</th>
        <th>外键</th>
        <th>是否为主键</th>
    </tr>
    <tr>
        <th>blog_id</th>
        <th>博客编号</th>
        <th>CharField（32）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>是</th>
    </tr>
    <tr>
        <th>title</th>
        <th>标题</th>
        <th>TextField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>是</th>
    </tr>
    <tr>
        <th>desc</th>
        <th>描述</th>
        <th>CharField(1024）</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>readtimes</th>
        <th>阅读次数</th>
        <th>IntegerField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>readtimes</th>
        <th>最后阅读时间</th>
        <th>DateTimeField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>tags</th>
        <th>类别</th>
        <th>CharFiled</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>body</th>
        <th>正文</th>
        <th>TextField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>status</th>
        <th>状态</th>
        <th>CharField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>allow_content</th>
        <th>是否允许评论</th>
        <th>BooleanField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>pub_time</th>
        <th>发布时间</th>
        <th>DateTimeField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>update_time</th>
        <th>更新时间</th>
        <th>DateTimeField</th>
        <th>NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>allow_feed</th>
        <th>是否允许出现聚合中</th>
        <th>BooleanField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>order</th>
        <th>优先级</th>
        <th>IntegerField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>password</th>
        <th>阅读密码</th>
        <th>CharField</th>
        <th>NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>author</th>
        <th>作者</th>
        <th>CharField</th>
        <th>CharField</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>category</th>
        <th>分类</th>
        <th>CharField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
        <tr>
        <th>category_parent</th>
        <th>父级标签</th>
        <th>IntgerField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
</table>

##博客类别 Category

<table>
    <tr>
        <th>catagory_id</th>
        <th>类别编号</th>
        <th>IntegerField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>是</th>
    </tr>
    <tr>
        <th>category_name</th>
        <th>分类名</th>
        <th>CharField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>category_slug</th>
        <th>缩略名</th>
        <th>CharField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>category_order</th>
        <th>优先级</th>
        <th>IntegerField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
    <tr>
        <th>category_level</th>
        <th>分类等级</th>
        <th>IntegerField</th>
        <th>NOT NULL</th>
        <th></th>
        <th>否</th>
    </tr>
</table>