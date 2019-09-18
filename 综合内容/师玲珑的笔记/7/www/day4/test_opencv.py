#导入cv2模块
import cv2
import sys
import importlib
importlib.reload(sys)
#cv2 支持 bmp jpg jpeg png tiff gif

#声明一个图像类
class TestCv2(object):
    #初始化方法
    def __init__(self,cv2):
        self.cv2=cv2

    #定义人脸识别方法
    def face_reg(self):
        cv2=self.cv2
        #定义图片地址
        img='./宝华哥.jpg'
        #读图
        image=cv2.imread(img)
        #定义模型地址
        face_cascade = cv2.CascadeClassifier('D:/python3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        #探测人脸
        faces=face_cascade.detectMultiScale(image,scaleFactor=1.15,minNeighbors=5,minSize=(5,5),flags=cv2.IMREAD_GRAYSCALE)

        print('一共找到了{0}个人脸'.format(len(faces)))

        #勾选人脸
        for(x,y,w,h) in faces:
            cv2.circle(image,((x+x+w)//2,(y+y+h)//2),(w//2),(0,255,0),2)
        cv2.imshow('find face',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #入门图片操作方法
    def test_base(self):
        cv2=self.cv2
        #读图
        img = cv2.imread("bao.jpg")
        #创建窗口并且展示图片
        # cv2.namedWindow("Image")
        #显示图片
        cv2.imshow('Image',img)
        #延迟窗口
        cv2.waitKey(0)   #0是无效参数
        #释放窗口
        cv2.destroyAllWindows()
    
    #图片操作方法
    def test_do_img(self):
        cv2=self.cv2
        #读取原图
        img=cv2.imread('bao.jpg')
        #改变图片尺寸 
        # img_copy=cv2.resize(img,(200,150))

        #降噪操作
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #写入新图
        cv2.imwrite('new.jpg',gray)

        #压缩图片  将图片分辨率降低 阈值范围是 0-100
        cv2.imwrite('new2.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),20])

        #显示图片
        cv2.imshow('Image',gray)
        #延迟窗口
        cv2.waitKey(0)
        #释放窗口
        cv2.destroyAllWindows

if __name__ == "__main__":
    #实例化对象
    testcv2=TestCv2(cv2)
    #调用方法
    # testcv2.test_base()
    testcv2.test_do_img()
    # testcv2.face_reg()

