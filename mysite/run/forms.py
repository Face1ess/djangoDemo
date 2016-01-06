#coding=utf-8
from django import forms
import re

actTypeChoices =(('跑步','跑步'),('椭圆机','椭圆机'))

class ActForm(forms.Form):
    actDist = forms.DecimalField(label='运动距离',required=True)
    actType = forms.ChoiceField(label='运动类型',choices=actTypeChoices)
    actDuration = forms.CharField(label='运动持续时间',required=True)
    actStartDate = forms.CharField(label='开始日期',required=True)
    actAvgSpd = forms.DecimalField(label='平均速度',required=True)
    actCalBurn = forms.IntegerField(label='消耗卡路里',required=True)

    def clean_actDuration(self):
        duration = self.cleaned_data['actDuration']
        pattern = re.compile(r"(\d*h)?([0-9]|[1-5][0-9])m([0-9]|[1-5][0-9])s")
        if pattern.match(duration):
            pass
        else: 
            msg="运动持续时间输入错误,示例:1h23m45s"
            raise forms.ValidationError(msg)
        return duration

    def clean_actStartDate(self):
        startDate = self.cleaned_data['actStartDate']
        pattern = re.compile(r"\d{4}-([1-9]|[1][0-2])-([1-9]|[1-2][0-9]|[3][0-1])")
        if pattern.match(startDate):
            pass
        else:
            msg="开始日期输入错误，示例:2016-1-4"
            raise forms.ValidationError(msg)
        return startDate
