# Research

##调研目标

* 新的技术，前沿的算法，了解行业前沿发展方向。
* 旧的经典模型，熟悉原理及远码，强化对各个领域的了解。
* 因项目需求，调研一些算法，辅助项目的完成。

##调研时间
* 其他项目训练过程中，抽出部分时间调研。
* 工作之余(主要)。


##调研内容
####基础网络模型
[Batch Normalization](): 

Accelerating Deep Network Training

使用FaceNet找到人脸并提取人脸特征，最后输入到knn中进行分类。原始代码效果一般，速度较慢，具体原理没有研究。

####人脸识别
[RealTimeFaceRecognition](https://github.com/shanren7/real_time_face_recognition)

使用FaceNet找到人脸并提取人脸特征，最后输入到knn中进行分类。原始代码效果一般，速度较慢，具体原理没有研究。

####目标检测
[RealTimeFaceRecognition](https://github.com/shanren7/real_time_face_recognition)

使用FaceNet找到人脸并提取人脸特征，最后输入到knn中进行分类。原始代码效果一般，速度较慢，具体原理没有研究。


##摄像头远程连接使用
* 1、获取远程连接代码
<pre>
git clone https://github.com/Maycbj/Share.git -b intern_sina`
</pre>
[XXXX](#jump)
* 2、修改mac的ip地址 
<pre>
cd Share/fast_style_transfer/code
vim src/receive.py 
address = ('10.236.10.44', 8003) ＝>  address = ('mac.de.i.p', 8003)
</pre>

* 3、登陆远程服务器：
<pre>
ssh root@10.85.125.105
cd /home/yuchen/Project/fast-style-transfer
vim evaluate_server.py 
address_s = ('10.236.10.44', 8003)＝>  address = ('mac.de.i.p', 8003)
</pre>

* 4、运行程序
<pre>
//mac上运行
sh creat_connect.sh
//立即在linux上运行
python evaluate_server.py 
</pre>








