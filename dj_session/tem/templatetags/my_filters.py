from django import template

register=template.Library()#自定义过滤器

@register.filter('my_mobile')
def filter_mobile(my_mobile_num,flag='****'):
    return my_mobile_num[:3]+flag+my_mobile_num[-4:]

@register.filter('my_sex')
def filter_sex(my_sex):
    if my_sex=='1':
        return '男'
    else:
        return '女'
