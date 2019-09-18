```python
1、在 Windows 设置临时环境变量 cmd命令窗口 输入 path=%path%;E:\soft\python-3.5.2-embed-win32  
  永久配置,在系统变量下找到path,在Path的最后面添加Python的安装目录  
  D:\Python34，同样在PATHEXT中添加 .PY;.PYM   
    
  然后，输入python 出现版本信息就成功了。  
    
2、CMD命令窗口,清屏的方法  
   import os  
   os.system('cls')  
   如果不要返回值0就是：  
   import os  
   i=os.system('cls')  
3、查看当前系统时间  
import time  
   #-*-格式时间格式-*-  
localtime = time.asctime( time.localtime(time.time()) )  
   #-*-格式时间格式[格式化成2009-03-20 11:45:39形式]-*-  
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  
   #-*-格式时间格式[时间戳格式]-*-  
time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())  
   #-*-输出格式化后的时间-*-  
print ("本地时间为 :", localtime)  
  
4、在CMD命令行中，输入 “python” + “空格”，即 ”python “；将已经写好的脚本文件拖拽到当前光标位置，然后敲回车运行即可  
  
5、乱码原因：  
    因为你的文件声明为utf-8，并且也应该是用utf-8的编码保存的源文件。但是windows的本地默认编码是cp936，也就是gbk编码，所以在控制台  
  
    直接打印utf-8的字符串当然是乱码了。   
  
    解决方法：  
    在控制台打印的地方用一个转码就ok了，打印的时候这么写：  
    print myname.decode('UTF-8').encode('GBK')   
  
    比较通用的方法应该是：  
    import sys  
    type = sys.getfilesystemencoding()  
    print myname.decode('UTF-8').encode(type)  
      
      
    #-*-coding:UTF-8-*-  或者 import sys  
    reload(sys)  
    sys.setdefaultencoding('UTF-8')  
      
      
6、其实要驱动chrome浏览器必须要依赖Chromedriver文件才行，  
  
    下载地址：  
    http://code.google.com/p/chromedriver/downloads/list  
  
    找到适合你自己系统的包之后下载解压出Chromedriver文件，并将此文件拷贝到java项目的根目录。  
    还是拿上此教程的为例，我们直接爸chromedriver文件拷贝到HelloSelenium项目的根目录下也就  
    是HelloSelenium目录下。这样就可以直接运行了。  
7、  安装pyse ： 将其克隆到本地，将pyse目录放到..\Python27\Lib\site-packages\目录下。  
    https://github.com/defnngj/pyse  
    python setup.py install  安装  
    java -jar selenium-server-standalone-3.4.0.jar -multiWindow  
      
      
8、定位属性  
        #########百度输入框的定位方式##########  
  
        #通过id方式定位  
        browser.find_element_by_id("kw").send_keys("selenium")  
  
        #通过name方式定位  
        browser.find_element_by_name("wd").send_keys("selenium")  
  
        #通过tag name方式定位  
        browser.find_element_by_tag_name("input").send_keys("selenium")  
  
        #通过class name 方式定位  
        browser.find_element_by_class_name("s_ipt").send_keys("selenium")  
  
        #通过CSS方式定位  
        browser.find_element_by_css_selector("#kw").send_keys("selenium")  
  
        #通过xphan方式定位  
        browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")  
  
        ############################################  
  
        browser.find_element_by_id("su").click()  
        time.sleep(3)  
        browser.quit()  
  
  
一、元素的定位  
  
1.webdriver提供的8种页面元素定位方法：  
    id/name/class name/tag name/link text/partial link text/xpath/css selector  
    其中python对应的8种方法：  
    find_element_by_id()                       如： find_element_by_id("kw")    
    find_element_by_name()                     如： find_element_by_name("wd")  
    find_element_by_class_name()               如： find_element_by_class_name("s_ipt")   
    find_element_by_tag_name()                 如： find_element_by_tag_name("input")   
    find_element_by_link_text()                如：find_element_by_link_text(u"新闻")      
    find_element_by_partial_link_text()        如：find_element_by_partial_link_text(u"一个很长的")   
    find_element_by_xpath()                    如： find_element_by_xpath(" .//*[@id='kw']")    
    find_element_by_css_selector()             如： find_element_by_css_selector("#kw")  
      
二、浏览器控制  
    1.控制浏览器大小：set_window_size()    例如：driver.set_window_size(400,500)  
                      maximize_window()    例如：driver.maximize_window()  #无参数  
    2.浏览器后退、前进：back()-后退、farward()-前进  
   
三、鼠标事件  
    ActionChains类提供的常用方法：  
        1.1 perform()：执行ActionChains中存储的所有行为,对整个事件进行提交  
        1.2 context_click():    右击  
        如：  
           from selenium.webdriver.common.action_chains import ActionChains  
                ...  
           ActionChains(dr).context_click(docfile).perform()  
        1.3 double_click():     双击  
        如：  
           from selenium.webdriver.common.action_chains import ActionChains  
                ...  
           doubleClick=dr.find_element_by_id("xxx")  
           ActionChains(dr). double_Click(doubleClick).perform()          
        1.4 drag_and_drop(source,target):    拖动  
        如：  
            from selenium.webdriver.common.action_chains import ActionChains  
                ...  
            dsource=dr.find_element_by_id("xxx")        #拖动的源元素  
            dtarget=dr.find_element_by_id("xxx")        #释放的目标目标元素  
           ActionChains(dr).drag_and_drop(dsource,dtarget).perform()  
        1.5 move_to_element():  鼠标悬停  
        如：  
           from selenium.webdriver.common.action_chains import ActionChains  
                ...  
           above=dr.find_element_by_id("xxx")  
           ActionChains(dr).move_to_element(above).perform()  
四、键盘事件      
    1.首先要导入键盘事件的包  
  
    from selenium.webdriver.common.keys importKeys  
    ...  
    dr.get("http://www.baidu.com")  
    #输入内容  
    dr.find_element_by_id("kw").send_keys("seleniumm")  
    #删除输入内容的最后一个字母,  
    dr.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)  
    #输入：空格+教程  
    dr.find_element_by_id("kw").send_keys(Keys.SPACE)  
    dr.find_element_by_id("kw").send_keys(u"教程")  
    #ctrl+a全选输入框内容  
    dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')  
    #ctrl+x剪贴输入框内容  
    dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')  
    #ctrl+v剪贴输入框内容  
    dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')  
    #回车键操作  
    dr.find_element_by_id("su").send_keys(Keys.ENTER)  
    dr.close()  
  
    常用的键盘操作整理：  
    send_keys(Keys.BACK_SPACE)  #删除键BackSpace  
    send_keys(Keys.SPACE)       #空格键Space  
    send_keys(Keys.TAB)         #制表键Tab  
    send_keys(Keys.ESCAPE)      #回退键Esc  
    send_keys(Keys.ENTER)       #回车键Enter  
    send_keys(Keys.CONTROL,'a') #Ctrl+a  
    send_keys(Keys.CONTROL,'c') #Ctrl+c      
    send_keys(Keys.CONTROL,'x') #Ctrl+x  
    send_keys(Keys.CONTROL,'v') #Ctrl+x  
    send_keys(Keys.F1)          #F1,类似的有F1-F12  
五、获取验证  
  
    六、设置等待      
    1.显示等待：等待某个条件成立时，继续执行，否则达到最大等待时间后抛出异常：TimeoutException，显示等待是针对当前要定位元素使用  
  
    WebDriverWait(driver, timeout,poll_frequency,ignored_exceptions=None).until(method,message)      
    示例：  
    WebDriverWait(dr,5,0.5,None).until(  
        expected_conditions.presence_of_element_located((By.ID,"kw1")),message='test')   
    解释：  
    A.WebDriverWait()：在设置时间内，默认间隔一段时间检测一次当前页面元素是否存在，若超过当前指定时间检测不到则抛出异常；  
    B.driver：webdriver的浏览器驱动，ie、firefox、chromea  
    C.timeout：最长超时时间，以秒为单位  
    D.poll_frequency：休眠间隔时间-步长，默认0.5秒  
    E.ignored_exceptions：超时后异常信息，默认抛出NoSuchElementException异常  
    F.until(method,message): 调用该方法提供的驱动作为一个参数，直到返回值为True  
    G.until_not(method,message):调用该方法提供的驱动作为一个参数，直到返回值为False  
    H.expected_conditions类提供的预期条件实现有：  
        title_is:判断标题是否是xx  
        title_contains:判断标题是否包含xx  
        presence_of_element_located：元素是否存在  
  
        visibility_of_element_located：元素是否存在  
  
        visibility_of：是否可见  
  
        presence_of_all_elements_located：判断一组元素是否存在  
  
        text_to_be_present_in_element：判断元素是否有xx文本信息    
  
        text_to_be_present_in_element_value：判断元素值是否有xx文本信息    
  
        frame_to_be_available_and_switch_to_it：表单是否可见，并切换到该表单  
  
        invisibility_of_element_located：判断元素是否隐藏  
        element_to_be_clickable：判断元素是否点击，它处于可见和启动状态  
        staleness_of：等到一个元素不再依附于DOM  
        element_to_be_selected：被选中的元素  
        element_located_to_be_selected：一个期望的元素位于被选中  
        element_selection_state_to_be：一个期望检查如果给定元素被选中  
        element_located_selection_state_to_be：期望找到一个元素并检查是否是选择状态  
        alert_is_present：预期一个警告信息    
  
   
    2.隐式等待:通过一定的时长等待页面所有元素加载完成，哪个元素超出设置时长没被加载就抛出异常NoSuchElementException，隐式等待是针对所有元素的  
   
        implicitly_wait(5)    #默认单位为秒  
    示例：  
        dr.implicitly_wait(5)  
七、sleep休眠    python中强制的程序等待  
    from time import sleep  
    sleep(4)    #默认单位秒，设置小于1秒的时间可以用小数点如sleep(0.6)  
八、定位一组元素，类似与1中定位单个元素方法  
    find_elements_by_id()                     如： find_elements_by_id("kw")    
    find_elements_by_name()                   如： find_elements_by_name("wd")  
    find_elements_by_class_name()             如： find_elements_by_class_name("s_ipt")   
    find_elements_by_tag_name()               如： find_elements_by_tag_name("input")   
    find_elements_by_link_text()              如：find_elements_by_link_text(u"新闻")      
    find_elements_by_partial_link_text()      如：find_elements_by_partial_link_text(u"一个很长的")   
    find_elements_by_xpath()                  如： find_elements_by_xpath(" .//*[@id='kw']")    
    find_elements_by_css_selector()           如： find_elements_by_css_selector("#kw")  
    使用场景：  
    a.批量操作对象，如选中页面上所有复选框  
    b.先获取一组对象，再在这组对象里定位需要的的一些对象，如定位所有复选框，然后选择最后一个  
   例如：代码如下  
checkbox.htm页面：  
  
    <styletype="text/css">  
    body{font-size:12px; font-family:Tahoma;}  
    .checkbox{vertical-align:middle; margin-top:0;}  
    </style>  
    <body>  
    <inputclass="checkbox"type="checkbox"/>元旦  
    <inputtype="checkbox"name="test"/>圣诞节  
    <inputtype="checkbox"name="test"/>股市  
    <inputtype="checkbox"name="test"/>阿凡达  
    <inputtype="checkbox"name="test"/>十月围城  
    <inputtype="checkbox"name="test"/>水价上调  
    <inputtype="button"value="检测"id="btn"/>  
    </body>  
  
python代码：   
  
       from selenium import webdriver  
       
        dr=webdriver.Firefox()  
        dr.get("D:\\workspace\\pySelenium\\resources\\checkbox.htm")  
    #使用tagname方式选择页面上所有tagname为input的元素  
    select_tagname=dr.find_elements_by_tag_name("input")  
    #使用xpath方式选择页面上所有tagname为input的元素  
    select_xpath=dr.find_elements_by_xpath("//input[@type='checkbox']")  
    #使用css_select方式选择页面上所有tagname为input的元素  
    select_css=dr.find_elements_by_css_selector('input[type=checkbox]')  
    for i in select_tagname:  
    #循环对每个input元素进行点击选中操作  
    if i.get_attribute("type")=='checkbox':  
    i.click()  
    for j in select_xpath:  
    #循环对每个input元素进行点击取消操作  
    j.click()  
    for k in select_css:  
    #循环对每个input元素进行点击选中操作  
    k.click()  
    #打印出checkbox的个数  
    print'----页面上checkbox的个数为：',len(select_css)  
    #使用pop()获取1组元素的第几个元素  
    select_css.pop(0).click()#第一个  
    select_css.pop(1).click()#第二个  
    select_css.pop().click()#最后一个  
    select_css.pop(-1).click()#最后一个  
    select_css.pop(-2).click()#倒数第二个  
    dr.close()  
  
    备注：pop():选择一组元素中的某一个，要注意的是：pop()和pop(-1)都表示最后一个元素  
九、多表单切换（对于有frame嵌套表单的操作）  
frame页面：  
  
    <html>  
    <body>  
    <frameset>  
    <h3>frame</h3>  
    <iframeid='frameid'name='frameName'width="800"height="500"src="http://www.baidu.com"/>  
    </frameset>  
    </body>  
    </html>  
  
python代码：  
  
    dr.get("D:\\workspace\\pySelenium\\resources\\frame.htm")  
    dr.switch_to_frame("frameid")#通过frame的id进入iframe  
    #dr.switch_to_frame("frameName") #通过frame的name进入iframe  
    #下面可以对frame进行操作了  
    dr.find_element_by_id("kw").send_keys("selenium")  
    dr.find_element_by_id("su").click()  
    dr.switch_to_default_content()#退出当前frame返回上一层  
  
备注：1.switch_to_frame()默认直接取表单的id或者name属性来切换  
      2.完成当前frame表单操作后，可以通过switch_to_default_content()方法返回上一层表单，即离的最近的switch_to_frame()方法      
      3.对于frame中没有id和name属性的通过下面方式进入frame（定位到frame以页面对象传入）  
python代码：  
  
    dr.get("D:\\workspace\\pySelenium\\resources\\frame.htm")  
     #定位到frame页面元素  
        framepath=dr.find_element_by_class_name("frameClassname")  
        dr.switch_to_frame(framepath)#通过frame页面对象进入iframe  
    #下面可以对frame进行操作了  
    dr.find_element_by_id("kw").send_keys("selenium")  
    dr.find_element_by_id("su").click()  
    dr.switch_to_default_content()#退出当前frame返回上一层  
  
十、多窗口切换  
    selenium-webdriver中使用switch_to_window()方法来切换任意窗口，常用方法有  
          driver.current_window_handle    #获取当前窗口句柄  
    　　driver.window_handles            #返回所有窗口句柄到当前会话  
    　　driver.switch_to_window()       #进入窗口，用于切换不同窗口  
   
python代码：      
  
    dr.get("http://www.baidu.com")  
    current_handle=dr.current_window_handle #获取百度首页窗口句柄  
    index_login=dr.find_element_by_xpath("//div[@id='u1']/a[@class='lb']")#获取登录按钮对象  
    index_login.click()#点击登录  
    dr.implicitly_wait(5)  
    dr.find_element_by_class_name("pass-reglink").click()#点击立即注册按钮  
    all_handles=dr.window_handles #获取所有打开窗口句柄  
    for handle in all_handles:  
    if handle==current_handle:  
    dr.switch_to_window(handle)  
    ''''' 
    ...对首页窗口进行操作 
    '''  
    print'----首页页面title：',dr.title  
    for handle in all_handles:  
    if handle!=current_handle:  
    dr.switch_to_window(handle)  
    ''''' 
    ...对注册窗口进行操作 
    '''  
    print'----注册页面title：',dr.title  
  
十一、警告框处理  
    webdriver中处理js生成的alert、confirm、prompt处理方法是：使用switch_to_alert()定位到alert/confirm/prompt，然后使用text、accept、dismiss、send_keys来根据需要操作。  
    text：返回alert、confirm、prompt中的文字信息  
    accept：点击确认按钮  
    dismiss：点击取消按钮  
    send_keys：在alert、confirm有对话框时输入值  
python代码：  
  
    dr.get("http://www.baidu.com")  
    set_link=dr.find_element_by_xpath("//div[@id='u1']/a[@class='pf']")#找到设置链接元素  
    ActionChains(dr).move_to_element(set_link).perform()#鼠标移动到设置上  
    dr.find_element_by_xpath("//a[@class='setpref']").click()#点击搜索设置链接  
    time.sleep(3)    #加等待时间 等按钮可用，否则会报错  
    save_set=dr.find_element_by_css_selector("#gxszButton > a.prefpanelgo")#获取保存设置按钮  
    save_set.click()#点击保存设置按钮  
       
    alert=dr.switch_to_alert()                    #进入alert  
    print'----弹出alert中内容为：',alert.text #打印对话框里的文字内容  
    alert.accept()#对话框里点击alert中确定按钮  
    #alert.dismiss() #对话框里点击取消按钮  
    #alert.send_keys("对话框中输入的内容") #在对话框里输入内容  
  
十二、上传文件  
    分2种：普通上传、插件上传  
    普通上传：将本地文件的路径作为一个值放到input标签中，通过form表单提交时，将值传给服务器中去  
    插件上传：指基于flash、javascript或ajax技术实现的上传功能或插件。  
    1.针对普通上传用send_keys实现  
python代码：  
  
    dr.get("D:\\workspace\\pySelenium\\resources\\upload.htm")  
    loadFile=dr.find_element_by_name("filebutton")# 获取上传文件input元素节点  
    loadFile.send_keys("D:\\workspace\\pySelenium\\resources\\frame.htm")#输入上传文件地址来实现上传  
  
    2.插件上传:使用AutoIt实现，--需要安装AutoIt程序  
        AutoIt安装，使用暂时略，需要时再追加，流程为：用AutoIt编写上传文件脚本生成exe文件，在python脚本中进行调用  
python代码：  
  
    loadFile=dr.find_element_by_name("filebutton")# 获取上传按钮  
    loadFile.click()    #点击上传按钮，弹出上传对话框  
    os.system("D:\\autoItFile.exe")    #调用autoIt生成的exe文件，实现导入  
  
十三、下载文件:使用AutoIt实现，--需要安装AutoIt程序，方法同上传  
python代码：  
  
    ffp=webdriver.FirefoxProfile()  
    ffp.set_preference("browser.download.folderList",2)#0:代表下载到浏览器默认路径下；2：下载到指定目录  
    ffp.set_preference("browser.download.manager.showWhenStarting",False)#是否显示开始：True：显示；False：不显示  
    ffp.set_preference("browser.download.dir", os.getcwd())#指定下载文件目录，os.getcwd()无参数，返回当前目录  
    # ffp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")#下载文件类型，  
    #指定下载页面的content-type值，application/octet-stream为文件类型，http-content-type常用对照表搜索百度  
    dr=webdriver.Firefox(firefox_profile=ffp)  
    dr.get("https://pypi.python.org/pypi/selenium#downloads")  
    dr.find_element_by_xpath("//div[@id='content']/div[3]/table/tbody/tr[3]/td[1]/span/a[1]").click()  
    #接下来使用autoIt实现  
  
十四、cookies操作  
    webdriver操作cookies的方法：  
    get_cookies()：获得所有cookies的值  
    get_cookie(name)：获得有特定name值的cookie信息  
    add_cookie(cookie_dict)：添加cookie，必须有name和value  
    delete_cookie(name)：删除特定名称的cookie信息，通过name找到特定的cookie并删除  
    delete_all_cookies()：删除浏览器中所有cookie的信息  
    注意：1.cookie是以字典形式进行存储的；  
    2.使用场景：如登录功能会把用户名写入浏览器cookie指定key为username，那么就可以通过get_cookies()找到username，打印value，找不到说明保存浏览器的cookie是有bug的。  
python代码：  
  
    num=1  
    dr.get("http://www.baidu.com")  
    cookies=dr.get_cookies()#获取cookie的所有信息  
    for ck in cookies:  
    print'----所有cookie',num,':',ck #打印cookie的所有信息  
    num=num+1  
    print'----按name查cookie：',dr.get_cookie("PSTM")#通过cookie的name获取cookie信息  
    dr.add_cookie({'name':'hello','value':'123456789'})#向name和value添加会话信息  
    cookies2=dr.get_cookies()#重新获取cookie的所有信息  
    for ck2 in cookies2:  
    if ck2['name']=='hello':  
    print"----加入的cookie信息：%s-->%s",(ck2['name'],ck2['value'])  
  
十五、javascript调用，python使用的方法：execute_script()  
python代码：  
  
    dr.get("http://www.baidu.com")  
    dr.find_element_by_id("kw").send_keys("selenium")  
    dr.find_element_by_id("su").click()  
    js="var q=document.documentElement.scrollTop=1000"    #滚动条滚到最下面  
    dr.execute_script(js)  
    time.sleep(4)  
    js2="var q=document.documentElement.scrollTop=0"      #滚动条滚到页面顶  
    dr.execute_script(js2)  
  
十六、截图，适用于脚本出错时，对当前窗口进行截图保存，使用函数：get_screenshot_as_file()  
python代码：  
  
    dr.get("http://www.baidu.com")  
    try:  
    dr.find_element_by_id("kw1").send_keys("selenium")  
    dr.find_element_by_id("su").click()  
    exceptNoSuchElementException,msg:  
    dr.get_screenshot_as_file("d:\\error.jpg")    #截图输出到d盘  
    print msg  
    dr.close()  
  
十七、关闭窗口  
    quit()：退出相关驱动程序并关闭所有窗口。  
    close()：关闭当前窗口，打给多个窗口时，可使用来关闭当前窗口  
十八、验证码处理  
    方法1：去掉验证码，问题：如果是在正式环境跑脚本那么在取掉会存在风险  
    方法2：设置万能验证码，不需要取消验证码，在程序中留后门--设置一个万能验证码，输入万能验证码了就标识通过  
python代码：   
  
    import random  
    randnum=random.randint(1000,9999)  
    print"----生成随机数为：",randnum  
    input_num=input(u"请输入验证码:")  
    print"----输入验证码为：",input_num  
    if input_num==randnum:  
    print"随机数正确，登录成功"  
    elif input_num==1234:  
    print"输入正确，登录成功"  
    else:  
    print"登录失败"  
  
    方法3：使用cookie方法获取，读取之前登录的cookie值访问时，直接登录，不需要验证码    
  
--------------------------------------------------- CMD -----------命令启动Python脚本  
    文件命名为：test.bat   貌似不能用  
    @echo off  
    echo.  
    python E:\pythonScript\Auto_linknetwork.py  
    cd /D C:\Python27  
    python.exe  
    rm #!C:\Python27/python.exe  
    import os;  
    i=os.system("清屏",cls);  
    import time;  
    #-*-格式时间格式[格式化成2009-03-20 11:45:39形式]-*-  
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());  
    print ("系统当前时间为 :", localtime);   
1、截屏  
    driver.save_screenshot('E:\\pythonScript\\images\\'+strTime+'baidu.png')  
  
  
三. WebElement接口获取值  
        通过WebElement接口可以获取常用的值，这些值同样非常重要。  
  
    size 获取元素的尺寸  
    text 获取元素的文本  
    get_attribute(name) 获取属性值  
    location 获取元素坐标，先找到要获取的元素，再调用该方法  
    page_source 返回页面源码  
    driver.title 返回页面标题  
    current_url 获取当前页面的URL  
    is_displayed() 设置该元素是否可见  
    is_enabled() 判断元素是否被使用  
    is_selected() 判断元素是否被选中  
    tag_name 返回元素的tagName  
  
 四.得到函数中的返回值  
    函数()  
     def returnval():  
  
     driver = webdriver.Chrome()  
     print u"\n回传值"  
     return driver  
  
     #returnval()  
  
     src = ("http://hos.sf-express.com")  
      
     returnval().get(src)  
  
     print returnval()  
  
   将函数作为返回值返回，不返回结果只返回函数  
     def lazy_sum(*args):  
         def sum():  
             ax = 0  
             for n in args:  
                 ax = ax + n  
             return ax  
          return sum  
     >> f = lazy_sum(1, 3, 2, 7, 9)  
     >> f  
     >> f()     
    #此时才是真正的计算出函数值；  
  
  
新建实例driver = webdriver.Chrome()  
1.获取当前页面的Url函数  
方法：current_url  
实例：  
driver.current_url  
2.获取元素坐标  
  
方法：location  
  
解释：首先查找到你要获取元素的，然后调用location方法  
实例：  
driver.find_element_by_xpath("//*[@id='tablechart']/tbody/tr[14]/td[9]").location  
3.表单的提交  
  
方法：submit  
解释:查找到表单（from）直接调用submit即可  
实例：  
  
driver.find_element_by_id("form1").submit()  
  
4.获取CSS的属性值  
方法：value_of_css_property(css_name)  
实例：  
driver.find_element_by_css_selector("input.btn").value_of_css_property("input.btn")  
5.获取元素的属性值  
方法：get_attribute(element_name)  
实例：  
driver.find_element_by_id("sellaiyuan").get_attribute("sellaiyuan")  
6.判断元素是否被选中  
方法：is_selected()  
实例：  
driver.find_element_by_id("form1").is_selected()  
7.返回元素的大小  
方法：size  
实例：  
driver.find_element_by_id("iptPassword").size  
返回值：{'width': 250, 'height': 30}  
8.判断元素是否显示  
方法：is_displayed()  
实例：  
driver.find_element_by_id("iptPassword").is_displayed()  
9.判断元素是否被使用  
方法：is_enabled()  
实例：  
driver.find_element_by_id("iptPassword").is_enabled()  
10.获取元素的文本值  
方法：text  
实例：driver.find_element_by_id("iptUsername").text  
11.元素赋值  
方法：send_keys(*values)  
实例：  
driver.find_element_by_id("iptUsername").send_keys('admin')  
注意如果是函数需要增加转义符u,eg.  
driver.find_element_by_id("iptUsername").send_keys(u'青春')  
12.返回元素的tagName  
方法：tag_name  
实例：  
driver.find_element_by_id("iptUsername").tag_name  
13.删除浏览器所以的cookies  
方法：delete_all_cookies()  
实例：  
driver.delete_all_cookies()  
14.删除指定的cookie  
方法：delete_cookie(name)  
实例：deriver.delete_cookie("my_cookie_name")  
15.关闭浏览器  
方法：close()  
实例：driver.close()  
16.关闭浏览器并且推出驱动程序  
方法：quit()  
实例：driver.quit()  
17.返回上一页  
方法：back()  
实例：driver.back()  
18.设置等待超时  
方法：implicitly_wait(wait_time)  
实例：driver.implicitly_wait(30)  
19.浏览器窗口最大化  
方法：maximize_window()  
实例：driver.maximize_window()  
20.查看浏览器的名字  
方法：name  
实例：drvier.name  
以上内容转发自http://blog.sina.com.cn/s/blog_b5fe6b270101c8v0.html 
```

