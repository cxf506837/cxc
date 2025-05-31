from django.db import models

# Create your models here.
class Student(models.Model):
    # 定义状态选项
    STATUS_CHOICES = (
        (True, '在读'),
        (False, '毕业')
    )

    # 字段定义
    name = models.CharField(max_length=15, verbose_name='姓名', db_index=True)  # 姓名，创建索引
    age = models.IntegerField(verbose_name='年龄', default=0)  # 年龄，默认值为 0
    sex = models.BooleanField(verbose_name='性别', default=True)  # 性别，默认值为 True（男性）
    class_name = models.CharField(db_column='class', max_length=10, verbose_name='班级', default='1')  # 班级名称
    description = models.TextField(verbose_name='个人描述', default='', blank=True)  # 个人描述，允许为空
    mobile = models.CharField(max_length=11, verbose_name='手机号', unique=True)  # 手机号，必须唯一
    status = models.BooleanField(choices=STATUS_CHOICES, verbose_name='状态', default=True)  # 状态，使用 choices
    email = models.EmailField(verbose_name='电子邮件', unique=True, default='default@example.com')  # 新增字段：电子邮件，必须唯一

    # 元数据
    class Meta:
        db_table = 'Student'  # 自定义表名为 Student
        verbose_name = '学生'  # 模型的中文名称
        verbose_name_plural = verbose_name  # 复数形式的中文名称

    # 字符串表示形式
    def __str__(self):
        return self.name  # 返回学生的姓名

# 添加一个空行以触发迁移检测