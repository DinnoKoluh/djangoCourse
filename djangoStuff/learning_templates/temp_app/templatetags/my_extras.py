from django import template

register = template.Library()

def custom_filter(value, arg):
    '''
    This cuts out all values of "arg" from value 
    '''
    return value.replace(arg, '')

register.filter('cut_string', custom_filter)