# user_operation/adminx.py
__author__ = 'derek'

import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


xadmin.site.register(UserFav, UserFavAdmin)


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address"]


xadmin.site.register(UserAddress, UserAddressAdmin)
