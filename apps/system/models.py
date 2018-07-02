from django.db import models

# Create your models here.


class SystemSetup(models.Model):
    loginTitle = models.CharField(max_length=20, null=True, blank=True, verbose_name='登录标题')
    mainTitle = models.CharField(max_length=20, null=True, blank=True, verbose_name='系统标题')
    headTitle = models.CharField(max_length=20, null=True, blank=True, verbose_name='浏览器标题')
    copyright = models.CharField(max_length=100, null=True, blank=True, verbose_name='底部版权信息')
    url = models.CharField(max_length=50, null=True, blank=True, verbose_name='系统URL地址')


    def __str__(self):
        return self.loginTitle

    class Meta:
        verbose_name = "系统设置"
        verbose_name_plural = verbose_name

    @classmethod
    def getSystemSetupLastData(self):
        return dict(system_setup=SystemSetup.objects.last())


class EmailSetup(models.Model):
    emailHost = models.CharField(max_length=30, verbose_name='SMTP服务器')
    emailPort = models.IntegerField(verbose_name='SMTP端口')
    emailUser = models.EmailField(max_length=100, verbose_name='邮箱帐号')
    emailPassword = models.CharField(max_length=30, verbose_name='邮箱密码')

    def __str__(self):
        return self.emailHost

    class Meta:
        verbose_name = '发件邮箱设置'
        verbose_name_plural = verbose_name

    @classmethod
    def getEmailSetupLastData(self):
        return EmailSetup.objects.last()