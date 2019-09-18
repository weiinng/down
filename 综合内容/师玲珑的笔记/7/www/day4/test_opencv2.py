#导入cv2模块
import sys
import importlib
import cv2
importlib.reload(sys)
from pymysql import connect
#cv2 支持 bmp jpg jpeg png tiff gif




#声明一个图像类
class TestCv2(object):
    #初始化方法
    def __init__(self,cv2):
        self.cv2 = cv2

    def CatVideo():
        cv2.namedWindow("shibie")
        #1调用摄像头
        cap=cv2.VideoCapture(0)
        #2人脸识别器分类器
        classfier=cv2.CascadeClassifier("D:/python3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
        while cap.isOpened():
            ok,frame=cap.read()
            if not ok:
                break
            #2灰度转换
            grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
            faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
            if len(faceRects) > 0:                          
                for faceRect in faceRects:  #单独框出每一张人脸
                    print(faceRect)
                    x, y, w, h = faceRect        
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), (0,255,0), 3)
            cv2.imshow("shibie",frame)
            print("ceshi2")
            if cv2.waitKey(10)&0xFF==ord('q'):
                break

    #定义人脸识别方法
    def face_reg(self):
        cv2 = self.cv2
        #定义图片地址
        img = './bao.jpg'
        #读图
        image = cv2.imread(img)
        #定义模型地址
        face_cascade = cv2.CascadeClassifier('D:/python3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
        #探测人脸
        faces = face_cascade.detectMultiScale(image,scaleFactor=1.15,minNeighbors=5,minSize=(5,5),flags=cv2.IMREAD_GRAYSCALE)
        conn=connect(host='localhost',port=3306,database='people',user='root',password='',charset='utf8')
        cur=conn.cursor()
        cur.execute("insert into people(num) values('%s')"%str(faces))
        conn.commit()
        cur.close()
        conn.close()
        print("一共找到了{0}个人脸".format(len(faces)))

        #勾选人脸
        for(x,y,w,h) in faces:
            #圆圈固定写法
            cv2.circle(image,((x+x+w) // 2,(y+y+h) // 2 ),(w // 2),(0,255,0),2)

        cv2.imshow('find face',image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        



    #入门图片操作方法
    def test_base(self):
        cv2 = self.cv2
        #读图
        img = cv2.imread("./new.jpg")
        #创建窗口并且展示图片
        cv2.namedWindow("Image")
        #显示图片
        cv2.imshow('Image',img)
        #延迟窗口
        cv2.waitKey(0)
        #释放窗口
        cv2.destroyAllWindows()

    #图片操作方法
    def test_do_img(self):
        cv2 = self.cv2
        #读取原图
        img = cv2.imread("./new.jpg")

        #降噪操作
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #改变图片尺寸
        img_copy = cv2.resize(img,(200,150))

        #写入新图
        cv2.imwrite('admin_new.jpg',img_copy)

        #压缩图片  压缩jpg 阈值范围是 0-100
        cv2.imwrite('admin_small.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),20])


        cv2.imshow('Image',img_copy)
        #延迟窗口
        cv2.waitKey(0)
        #释放窗口
        cv2.destroyAllWindows()



if __name__ == "__main__":
    #实例化对象
    testcv2 = TestCv2(cv2)
    #调用方法
    # testcv2.test_base()
    testcv2.face_reg()