from django.db import models
from django.contrib.auth.models import AbstractUser


class Structure(models.Model):
    """
    组织架构
    """
    type_choices = (("firm", "公司"), ("department", "部门"))
    title = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department", verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类架构")

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserProfile(AbstractUser):
    """
    用户表
    """
    name = models.CharField(max_length=20, default="", verbose_name="中文姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male",
                              verbose_name="性别")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg", max_length=100, null=True,
                              blank=True)
    mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    email = models.EmailField(max_length=100, verbose_name="邮箱")
    department = models.ForeignKey("Structure", null=True, blank=True, verbose_name="部门")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name
