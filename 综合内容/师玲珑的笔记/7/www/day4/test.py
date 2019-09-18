#导包
from matplotlib import pyplot as plt
import numpy as np
#导入3D模块
from mpl_toolkits.mplot3d.axes3d import Axes3D
import seaborn as sns
import pandas as pd

#定义一个单例模式的装饰器
def singleton(cls):
    #定义实例容器
    instances={}
    #定义嵌套方法
    def wrapper(*args,**kwargs):  #装饰器自身性质 内置函数里的参数就是你穿过来的类的实例化参数
        #判断装饰的类是否为单例
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return wrapper

#建立一个测试类
@singleton
class TestPlt(object):
    #初始化方法
    def __init__(self,plt):
        self.plt = plt
    
    #配置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'

    #定义小费分析方法
    def test_tips(self,pd):
        #读取数据集
        df=pd.read_excel('tips.xlsx','sheet1')
        #绘制散点图证明推论，小费应该随着总帐单的递增而递增
        # df.plot(kind='scatter',x='tip',y='total_bill',label='bill_tip')  #kind是绘图类型，x是x轴别名，y是y轴别名，label是图例
        #计算小费占总帐单的比例
        df['pct'] = df.tip / df.total_bill * 100
        
        #过滤出小费占比比较高的人群
        # print(df[df.pct > 30])
        #删除异常数据
        df = df.drop([67,172,178])
        print(df)
        print(df[df.pct > 30])
        #打印箱型图
        df.pct.plot(kind='box',label='tips pct%')

        #绘制
        plt.show()


    #定义数据分析方法：
    def test_excel(self,pd,sns):
        #读取数据集
        df = pd.read_excel('test.xlsx','sheet1')   #第一个是文件名 第二个是excel页名 
        #需求
        #计算按性别和人体质量分组，求销售额
        #select sum(sales),gender,bim from test group by gender,bmi
        myexcel = df.groupby(['BMI','Gender']).Sales.sum() #先根据gender分组，再根据BMI分组，求sales的和
        # print(df)
        print(myexcel)
        #绘制对比柱状图
        # myexcel.unstack().plot(kind='bar',stacked=True,color=['red','blue'])

        #利用seaborn绘制
        sns.violinplot(df['Age'],df['Gender'])
        #初始化数据
        sns.despine()

        #绘制
        self.plt.show()

    #趋势图方法
    def test_plot(self):
        plt = self.plt
        #定义x轴数据
        x = ['2019-05-01','2019-05-02','2019-05-03','2019-05-04']
        #定义y轴数据
        y1 = [0,5,6,10]  #代表温度
        y2 = [10,15,16,9]   #代表湿度
        # 填充数据
        plt.plot(x,y1,label='temperature')
        plt.plot(x,y2,label='water')
        #设置图例
        plt.legend()    
        #绘制
        plt.show()
    
    #普通散点图方法
    def test_scatter(self):
        plt = self.plt
        #定义数据
        x = list(range(0,101))
        y = [value * np.random.rand() for value in x]
        #填充数据
        plt.scatter(x,y,marker='^',s=30,c='red')
        plt.show()

    #定义3D散点图
    def test_scatter_3d(self):
        plt=self.plt
        #定义数据
        x = np.random.randint(0,10,size=100)
        y = np.random.randint(0,10,size=100)
        z = np.random.randint(0,10,size=100)
        #创建二维对象
        fig = plt.figure()
        #强转
        axes3d = Axes3D(fig)
        plt.xlabel('投球次数')
        plt.ylabel('投球得分')
        #填充数据
        axes3d.scatter(x,y,z)
        plt.show()

    #定义条形图
    def test_barh(self):
        plt=self.plt
        #定义数据
        price = [40,32.8,20,19.6]
        #填充数据
        plt.barh(range(4),price,align='center',color='red',alpha=0.5)
        #设置标签
        plt.xlabel('价格')
        plt.ylabel('商品')
        #编辑数据
        plt.yticks(range(4),['西游记','红楼梦','水浒传','三国演义'])
        #设置标题
        plt.title('四大名著')
        plt.show()
    
    #定义柱状图
    def test_bar(self):
        plt=self.plt
        #定义数据
        GDP=[12404,13908,9350,8000]
        GDP2=[11404,14908,7350,10000]
        #填充数据
        plt.bar(['北京','上海','天津','重庆'],GDP,color='steelblue',alpha=0.8,label='城市')
        plt.bar(['北京2','上海2','天津2','重庆2'],GDP2,color='red',alpha=0.8,label='省')
        #填写标签
        plt.xlabel('生产城市')
        plt.ylabel('生产总值')
        plt.legend()
        #刻度范围
        plt.ylim([5000,15000])

        plt.show()
    
    #定义饼图方法
    def test_pie(self):
        plt=self.plt
        #定义数据
        beijing=[17,18,40,60]
        #定义标签
        labels=['2-3年','3-4年','4-5年','5年以上']
        #颜色
        colors=['red','green','blue','purple']
        #做好容器
        indic=[]
        for index,item in enumerate(beijing):
            #判断优先级
            if item == max(beijing):
                indic.append(0.1)  #向外突出
            else:
                indic.append(0)
        #填充数据
        plt.title('3d饼图突出展示工龄占比')
        plt.pie(beijing,labels=labels,colors=colors,autopct='%1.1f%%',startangle=90,shadow=True,explode=tuple(indic))  #startangle=90 使图形旋转九十度，相当于立起来
        plt.show()

    #定义面积图
    def test_stackplot(self):
        plt=self.plt
        #定义数据
        data = ['2019-05-01','2019-05-02','2019-05-03','2019-05-04']
        #收入
        earn=[156,356,156,30]
        #支出
        morning,lunch,night=[10,30,10,10],[12,50,5,20],[5,15,12,30]
        #填充数据
        plt.stackplot(data,earn,morning,lunch,night,colors=['green','yellow','orange','red'])
        #生成图例
        plt.plot([],[],color='green',label='收入')
        plt.plot([],[],color='yellow',label='早饭')
        plt.plot([],[],color='orange',label='中饭')
        plt.plot([],[],color='red',label='晚饭')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # 实例化一个对象
    testplt = TestPlt(plt)
    # testplt.test_plot()
    # testplt.test_scatter()
    # testplt.test_scatter_3d()
    # testplt.test_barh()
    testplt.test_bar()
    # testplt.test_pie()
    # testplt.test_stackplot()
    # testplt.test_excel(pd,sns)
    # testplt.test_tips(pd)
  


