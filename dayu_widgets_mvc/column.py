#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.9
# Email : muyanru345@163.com
###################################################################
import collections
from dayu_widgets.qt import *
import utils

Cell = collections.namedtuple('Cell', ['user_callback', 'final_formatter'])


class Column(object):
    def __init__(self, attr, label=None, width=100):
        super(Column, self).__init__()
        self._font_config_dict = {}
        self._header_dict = {
            'key': attr,
            'label': label or ' '.join([i.title() for i in attr.split('_')]),
            'width': width,
            'hide': False,
            'clickable': False,
            'editable': False,
            'checkable': False,
            'selectable': False,
            'exclusive': False,
            'searchable': False,
            Qt.DisplayRole:
                Cell(user_callback=None, final_formatter=utils.display_formatter),
            Qt.BackgroundRole:
                Cell(user_callback=None, final_formatter=QColor),
            Qt.ForegroundRole:
                Cell(user_callback=None, final_formatter=QColor),
            Qt.EditRole:
                Cell(user_callback=None, final_formatter=None),
            Qt.TextAlignmentRole:
                Cell(user_callback=None, final_formatter=None),
            Qt.ToolTipRole:
                Cell(user_callback=None, final_formatter=utils.display_formatter),
            Qt.DecorationRole:
                Cell(user_callback=None, final_formatter=utils.icon_formatter),
            Qt.FontRole:
                Cell(user_callback=lambda x, y: self._font_config_dict,
                     final_formatter=utils.font_formatter),
            Qt.InitialSortOrderRole:
                Cell(user_callback=None, final_formatter=None),
            Qt.SizeHintRole:
                Cell(user_callback=None, final_formatter=lambda args: QSize(*args)),
            Qt.UserRole:
                Cell(user_callback=None, final_formatter=None),
            Qt.StatusTipRole:
                Cell(user_callback=None, final_formatter=utils.display_formatter),
            Qt.WhatsThisRole:
                Cell(user_callback=None, final_formatter=utils.display_formatter),
        }

    def label(self, text):
        self._update_role('label', text)
        return self

    def width(self, value):
        self._update_role('width', value)
        return self

    def clickable(self):
        self._update_role('clickable', True)
        return self

    def hide(self):
        self._update_role('hide', True)
        return self

    def checkable(self):
        self._update_role('checkable', True)
        return self

    def selectable(self):
        self._update_role('selectable', True)
        return self

    def searchable(self):
        self._update_role('searchable', True)
        return self

    def editable(self):
        self._update_role('editable', True)
        return self

    def exclusive(self):
        self._update_role('exclusive', True)

    def display(self, config):
        self._update_role(Qt.DisplayRole, config)
        return self

    def edit(self, config):
        self._update_role(Qt.EditRole, config)
        return self

    def icon(self, config):
        self._update_role(Qt.DecorationRole, config)
        return self

    def background(self, config):
        self._update_role(Qt.BackgroundRole, config)
        return self

    def foreground(self, config):
        self._update_role(Qt.ForegroundRole, config)
        return self

    def data(self, config):
        self._update_role(Qt.UserRole, config)
        return self

    def size(self, config):
        self._update_role(Qt.SizeHintRole, config)
        return self

    def order(self, config):
        self._update_role(Qt.InitialSortOrderRole, config)
        return self

    def tooltip(self, config):
        self._update_role(Qt.ToolTipRole, config)
        return self

    def underline(self):
        self._font_config_dict.update({'underline': True})
        return self

    def bold(self):
        self._font_config_dict.update({'bold': True})
        return self

    def italic(self):
        self._font_config_dict.update({'italic': True})
        return self

    def left(self):
        self._update_role(Qt.TextAlignmentRole, Qt.AlignLeft)
        return self

    def center(self):
        self._update_role(Qt.TextAlignmentRole, Qt.AlignCenter)
        return self

    def right(self):
        self._update_role(Qt.TextAlignmentRole, Qt.AlignRight)
        return self

    def ascending(self):
        self._update_role(Qt.InitialSortOrderRole, Qt.AscendingOrder)
        return self

    def descending(self):
        self._update_role(Qt.InitialSortOrderRole, Qt.DescendingOrder)
        return self

    def role(self, role):
        return self._header_dict.get(role, None)

    @classmethod
    def from_dict(cls, data_dict):
        column_obj = cls(data_dict.get('key'))
        column_obj.update(data_dict)
        return column_obj

    def update(self, data_dict):
        for role, config in data_dict.items():
            self._update_role(role, config)
        return self

    def _update_role(self, role, value):
        if isinstance(role, Qt.ItemDataRole) and role in self._header_dict:
            value = self.role(role)._replace(user_callback=value)
        self._header_dict.update({role: value})
