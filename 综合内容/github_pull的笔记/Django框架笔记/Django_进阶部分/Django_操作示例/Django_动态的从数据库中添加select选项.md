动态的给select标签添加选项

# views.py 中
 city = forms.ChoiceField(
        choices=models.City.objects.all().values_list("id", "name"),
        label="城市",
        initial=1,
        widget=forms.widgets.Select
    )



# 默认的这个form类中是没有init 方法的
# 为了实现实时更新, 需要重写父类的init方法
# 
def __init__(self, *args, **kwargs):
	super().__init__(*args, **kwargs)	# 父类的也不能丢啊.先把父类的执行了
	# 然后在父类的基础上再加上自己的想要加的字段
	self.fields["city"].widget.choices = models.City.objects.all().values_list("id", "name")






// html中
<div class="form-group {% if form_obj.city.errors.0 %}has-error{% endif %}">
	{{ form_obj.city.label }}
	{{ form_obj.city }}
	<span class="help-block">{{ form_obj.city.errors.0 }}</span>
</div>