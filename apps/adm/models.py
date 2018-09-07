from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AssetType(models.Model):
    """
    资产类型
    """
    name = models.CharField(max_length=30, verbose_name="类型名称", help_text="类型名称")

    class Meta:
        verbose_name = "类型名称"

    def __str__(self):
        return self.name


class Asset(models.Model):
    asset_status = (
        ("0", "闲置"),
        ("1", "在用"),
        ("2", "维修"),
        ("3", "报废"),
    )
    assetNum = models.CharField(max_length=128, default="", verbose_name="资产编号")
    # assetType = models.ForeignKey(AssetType, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="类型名称")
    brand = models.CharField(max_length=20, blank=True, null=True, verbose_name="品牌")
    model = models.CharField(max_length=128, default="", verbose_name="型号")
    service_num = models.CharField(max_length=128, default="", verbose_name="SN码")
    price = models.IntegerField(blank=True, null=True, verbose_name="价格")
    status = models.CharField(choices=asset_status, max_length=20, default="1", verbose_name="资产状态")
    customer = models.CharField(max_length=80, default="", blank=True, null=True, verbose_name="供应商")
    department = models.CharField(max_length=80, blank=True, verbose_name="使用部门")
    owner = models.CharField(max_length=80, blank=True, verbose_name="使用人")
    production_time = models.DateTimeField(verbose_name="生产日期")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加日期")
    desc = models.TextField(default="", blank=True, null=True, verbose_name="备注信息")

    class Meta:
        verbose_name = "资产管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.assetNum


#
#
# class AssetFile(models.Model):
#     asset = models.ForeignKey(Asset, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="资产")
#     upload_user = models.CharField(max_length=20, verbose_name="上传人")
#     file_content = models.ImageField(upload_to="asset_file/%Y/%m", null=True, blank=True, verbose_name="资产文件")
#     add_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
#
#
# class AssetLog(models.Model):
#     asset = models.ForeignKey(Asset, verbose_name="资产")
#     operator = models.CharField(max_length=20, verbose_name="操作人")
#     desc = models.TextField(default="", verbose_name="备注")
#     add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
#
#     class Mate:
#         verbose_name = "变更记录"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.asset
#
#
#
#
#
#
#
#
