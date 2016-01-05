#coding=utf-8
from django import forms


class ActForm(forms.Form):
    actDist = forms.DecimalField(label='运动距离')
    actType = forms.CharField(label='运动类型')
    actDuration = forms.CharField(label='运动持续时间')
    actStartDate = forms.CharField(label='开始日期')
    actAvgSpd = forms.DecimalField(label='平均速度')
    actCalBurn = forms.IntegerField(label='消耗卡路里')
