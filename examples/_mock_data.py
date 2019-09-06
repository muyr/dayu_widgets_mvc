#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *
from dayu_widgets_mvc import Column


def score_color(score, y):
    if score < 60:
        return dayu_theme.error_color
    elif score < 80:
        return dayu_theme.warning_color
    elif score >= 90:
        return dayu_theme.success_color
    return dayu_theme.info_color


column_list = [
    Column('name')
        .underline()
        .icon('user_fill.svg')
        .checkable(),
    Column('sex')
        .icon(
        lambda x, y: ('{}.svg'.format(x.lower()), vars(dayu_theme).get(x.lower() + '_color'))),
    Column('age')
        .width(90)
        .display(lambda x, y: u'{} 岁'.format(x)).bold(),
    Column('city')
        .label('Address')
        .selectable()
        .width(120)
        .display(lambda x, y: ' & '.join(x) if isinstance(x, list) else x)
        .background(lambda x, y: 'transparent' if x else dayu_theme.error_color),
    Column('score')
        .searchable()
        .editable()
        .background(score_color)
        .foreground('#fff'),
    Column('score')
        .label('Score Copy')
        .searchable()
        .editable()
        .foreground(score_color),
]

header_list = [
    {
        'label': 'Name',
        'key': 'name',
        'checkable': True,
        'searchable': True,
        Qt.FontRole: {'underline': True},
        Qt.DecorationRole: 'user_fill.svg'
    }, {
        'label': 'Sex',
        'key': 'sex',
        'searchable': True,
        'selectable': True,
        Qt.DecorationRole: lambda x, y: (
            '{}.svg'.format(x.lower()), vars(dayu_theme).get(x.lower() + '_color'))
    }, {
        'label': 'Age',
        'key': 'age',
        'width': 90,
        'searchable': True,
        'editable': True,
        Qt.DisplayRole: lambda x, y: u'{} 岁'.format(x),
        Qt.FontRole: lambda x, y: {'bold': True},
    }, {
        'label': 'Address',
        'key': 'city',
        'selectable': True,
        'searchable': True,
        'exclusive': False,
        'width': 120,
        Qt.DisplayRole: lambda x, y: ' & '.join(x) if isinstance(x, list) else x,
        Qt.BackgroundRole: lambda x, y: 'transparent' if x else dayu_theme.error_color
    }, {
        'label': 'Score',
        'key': 'score',
        'searchable': True,
        'editable': True,
        Qt.BackgroundRole: score_color,
        Qt.ForegroundRole: '#fff'
    },
    {
        'label': 'Score Copy',
        'key': 'score',
        'searchable': True,
        Qt.ForegroundRole: score_color
    },
]

data_list = [
    {
        'name': 'John Brown',
        'sex': 'Male',
        'sex_list': ['Male', 'Female'],
        'age': 18,
        'score': 89,
        'city': 'New York',
        'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
        'date': '2016-10-03',
    }, {
        'name': 'Jim Green',
        'sex': 'Male',
        'sex_list': ['Male', 'Female'],
        'age': 24,
        'score': 55,
        'city': 'London',
        'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
        'date': '2016-10-01',
    }, {
        'name': 'Zhang Xiaoming',
        'sex': 'Male',
        'sex_list': ['Male', 'Female'],
        'age': 30,
        'score': 70,
        'city': '',
        'city_list': ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou'],
        'date': '2016-10-02',
    }, {
        'name': 'Jon Snow',
        'sex': 'Female',
        'sex_list': ['Male', 'Female'],
        'age': 26,
        'score': 60,
        'city': 'Ottawa',
        'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
        'date': '2016-10-04',
    }, {
        'name': 'Li Xiaohua',
        'sex': 'Female',
        'sex_list': ['Male', 'Female'],
        'age': 18,
        'score': 97,
        'city': 'Ottawa',
        'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
        'date': '2016-10-04',
    }
]
