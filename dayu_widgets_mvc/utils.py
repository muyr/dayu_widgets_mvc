#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################
"""
Some helper functions for handling color and formatter.
"""

import collections
import datetime as dt

from singledispatch import singledispatch
from dayu_widgets.qt import QSortFilterProxyModel, QModelIndex, QFont, MIcon

ItemViewMenuEvent = collections.namedtuple('ItemViewMenuEvent', ['view', 'selection', 'extra'])


@singledispatch
def real_model(source_model):
    """
    Get the source model whenever user give a source index or proxy index or proxy model.
    """
    return source_model


@real_model.register(QSortFilterProxyModel)
def _(proxy_model):
    return proxy_model.sourceModel()


@real_model.register(QModelIndex)
def _(index):
    return real_model(index.model())


def real_index(index):
    """
    Get the source index whenever user give a source index or proxy index.
    """
    model = index.model()
    if isinstance(model, QSortFilterProxyModel):
        return model.mapToSource(index)
    return index


def get_obj_value(data_obj, attr, default=None):
    """Get dict's key or object's attribute with given attr"""
    if isinstance(data_obj, dict):
        return data_obj.get(attr, default)
    return getattr(data_obj, attr, default)


def set_obj_value(data_obj, attr, value):
    """Set dict's key or object's attribute with given attr and value"""
    if isinstance(data_obj, dict):
        return data_obj.update({attr: value})
    return setattr(data_obj, attr, value)


def has_obj_value(data_obj, attr):
    """Return weather dict has the given key or object has the given attribute."""
    if isinstance(data_obj, dict):
        return attr in data_obj.keys()
    return hasattr(data_obj, attr)


def apply_formatter(formatter, *args, **kwargs):
    """
    Used for QAbstractModel data method.
    Config a formatter for one field, apply the formatter with the index data.
    :param formatter: formatter. It can be None/dict/callable or just any type of value
    :param args:
    :param kwargs:
    :return: apply the formatter with args and kwargs
    """
    if formatter is None:  # 压根就没有配置
        return args[0]
    elif isinstance(formatter, dict):  # 字典选项型配置
        return formatter.get(args[0], None)
    elif callable(formatter):  # 回调函数型配置
        return formatter(*args, **kwargs)
    # 直接值型配置
    return formatter


@singledispatch
def display_formatter(input_other_type):
    """
    Used for QAbstractItemModel data method for Qt.DisplayRole
    Format any input value to a string.
    :param input_other_type: any type value
    :return: basestring
    """
    return str(input_other_type)  # this function never reached


@display_formatter.register(dict)
def _(input_dict):
    if 'name' in input_dict.keys():
        return display_formatter(input_dict.get('name'))
    elif 'code' in input_dict.keys():
        return display_formatter(input_dict.get('code'))
    return str(input_dict)


@display_formatter.register(list)
def _(input_list):
    result = []
    for i in input_list:
        result.append(display_formatter(i))
    return ','.join(result)


@display_formatter.register(str)
def _(input_str):
    # ['utf-8', 'windows-1250', 'windows-1252', 'ISO-8859-1']
    return input_str.decode('windows-1252')
    # return obj.decode()


@display_formatter.register(unicode)
def _(input_unicode):
    return input_unicode


@display_formatter.register(type(None))
def _(input_none):
    return '--'


@display_formatter.register(int)
def _(input_int):
    return str(input_int)


@display_formatter.register(float)
def _(input_float):
    return '{:.2f}'.format(round(input_float, 2))


@display_formatter.register(object)
def _(input_object):
    if hasattr(input_object, 'name'):
        return display_formatter(getattr(input_object, 'name'))
    if hasattr(input_object, 'code'):
        return display_formatter(getattr(input_object, 'code'))
    return str(input_object)


@display_formatter.register(dt.datetime)
def _(input_datetime):
    return input_datetime.strftime('%Y-%m-%d %H:%M:%S')


@singledispatch
def font_formatter(unknow):
    """
    if user input is not dict/QFont, return a default QFont instance
    :param setting_dict: user input
    :return: default QFont
    """
    _font = QFont()
    return _font


@font_formatter.register(dict)
def _(setting_dict):
    """
    Used for QAbstractItemModel data method for Qt.FontRole
    :param setting_dict: user input
    :return: a QFont instance with given style
    """
    _font = QFont()
    _font.setUnderline(setting_dict.get('underline') or False)
    _font.setBold(setting_dict.get('bold') or False)
    _font.setItalic(setting_dict.get('italic') or False)
    return _font


@font_formatter.register(QFont)
def _(font):
    """
    If user give me a QFont instance, use it.
    :param setting_dict: user input
    :return: QFont
    """
    return font


@singledispatch
def icon_formatter(input_other_type):
    """
    Used for QAbstractItemModel data method for Qt.DecorationRole
    A helper function to easy get QIcon.
    The input can be dict/object, string, None, tuple(file_path, fill_color)
    :param input_other_type:
    :return: a QIcon instance
    """
    return input_other_type  # this function never reached


@icon_formatter.register(dict)
def _(input_dict):
    attr_list = ['icon']
    path = next((get_obj_value(input_dict, attr) for attr in attr_list), None)
    return icon_formatter(path)


@icon_formatter.register(object)
def _(input_object):
    attr_list = ['icon']
    path = next((get_obj_value(input_object, attr) for attr in attr_list), None)
    return icon_formatter(path)


@icon_formatter.register(basestring)
def _(input_string):
    return MIcon(input_string)


@icon_formatter.register(tuple)
def _(input_tuple):
    return MIcon(*input_tuple)


@icon_formatter.register(type(None))
def _(input_none):
    return icon_formatter('confirm_fill.svg')
