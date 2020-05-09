import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "浮生未歇"
    site_footer = "浮生若梦"
    #菜单收缩
    menu_style = "accordion"
xadmin.site.register(views.CommAdminView, GlobalSettings)

class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]
xadmin.site.register(VerifyCode, VerifyCodeAdmin)



