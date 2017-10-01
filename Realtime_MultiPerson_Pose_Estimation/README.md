# Realtime MultiPerson Pose Estimation

## 项目地址
[论文地址](https://arxiv.org/abs/1611.08050)
[代码地址](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation)

## 项目介绍
Code repo for winning 2016 MSCOCO Keypoints Challenge, 2016 ECCV Best Demo Award, and 2017 CVPR Oral paper.  

Watch our video result in [YouTube](https://www.youtube.com/watch?v=pW6nZXeWlGM&t=77s) or [our website](http://posefs1.perception.cs.cmu.edu/Users/ZheCao/humanpose.mp4). 

We present a bottom-up approach for multi-person pose estimation, without using any person detector. For more details, refer to our [CVPR'17 paper](https://arxiv.org/abs/1611.08050) or our [presentation slides](http://image-net.org/challenges/talks/2016/Multi-person%20pose%20estimation-CMU.pdf) at ILSVRC and COCO workshop 2016.

## 模型参数
<table>
    <tr>
        <th>模型</th>
        <th>VggNet</th>
        <th>MobileNet</th>
        <th>ResNet</th>
        <th>description</th>
    </tr>
    <tr>
       <th colspan=5>solver</th>
   </tr>
   <tr>
    <th>base_lr</th>
    <td>4e-5</td>
    <td>4e-5</td>
    <td><font color=red>4e-4</font></td>
    <td></td>
</tr>
<tr>
    <th>momentum</th>
    <td>0.9</td>
    <td>0.9</td>
    <td>0.9</td>
    <td></td>
</tr>
<tr>
    <th>weight_decay</th>
    <td>5e-4</td>
    <td>5e-4</td>
    <td>5e-4</td>
    <td></td>
</tr>
<tr>
    <th>gamma</td>
        <td>0.333</td>
        <td>0.333</td>
        <td>0.333</td>
        <td></td>
    </tr>
    <tr>
        <th>stepsize</th>
        <td>5e4</td>
        <td>5e4</td>
        <td>5e4</td>
        <td></td>
    </tr> 
    <tr>
       <th colspan=5>pre-pocessing</th>
   </tr>
   <tr>
    <th>stride</th>
    <td>8</td>
    <td>8</td>
    <td>8</td>
    <td>输入图像边长／输出图像边长</td>
</tr>
<tr>
    <th>max_rotate_degree</th>
    <td>40</td>
    <td>40</td>
    <td>40</td>
    <td>图像增强</td>
</tr>
<tr>
    <th>crop_size</th>
    <td>224</td>
    <td>224</td>
    <td>224</td>
    <td></td>
</tr>
<tr>
    <th>scale</th>
    <td>0.5~1.1</td>
    <td>0.017</td>
    <td>0.5~1.1</td>
    <td>图像增强，缩放比例(包括mask)</td>
</tr>
<tr>
    <th>target_dist</th>
    <td>0.6</td>
    <td>0.6</td>
    <td>0.6</td>
    <td></td>
</tr>
<tr>
    <th>center_perterb_max</th>
    <td>40</td>
    <td>40</td>
    <td>40</td>
    <td>数据增强,ROI偏移像素</td>
</tr>
<tr>
    <th>do_clahe</th>
    <td>false</td>
    <td>false</td>
    <td>false</td>
    <td>数据增强,ROI偏移像素</td>
</tr>
<tr>
    <th>num_parts</th>
    <td>56</td>
    <td>56</td>
    <td>56</td>
    <td>部位数量</td>
</tr>
<tr>
    <th>np_in_lmdb</th>
    <td>17</td>
    <td>17</td>
    <td>17</td>
    <td>lmdb中存储数据个数</td>
</tr>
<tr>
   <th colspan=5>fine-tuning ratio</th>
</tr>
<tr>
    <th>fine-tuning前层/总层数</th>
    <td>10/19</td>
    <td>11/27</td>
    <td>22/50</td>
    <td></td>
</tr>
</table>

## fine-tuning模型链接:
* VGG19:    [https://gist.github.com/ksimonyan/3785162f95cd2d5fee77](https://gist.github.com/ksimonyan/3785162f95cd2d5fee77)
* MobileNet:    [https://github.com/shicai/MobileNet-Caffe](https://github.com/shicai/MobileNet-Caffe)
* ResNet:   [https://github.com/KaimingHe/deep-residual-networks](https://github.com/KaimingHe/deep-residual-networks)

## 模型结构
![model](https://github.com/ZheC/Multi-Person-Pose-Estimation/raw/master/readme/arch.png)

## 模型修改:
* 使用ResNet-50的前7个block替换Vgg-19，并用ResNet在imagenet上训练好的模型fine－tuning模型。
* 上图中，原始模型有6次修正(stage2～7)，现缩减至1次。

## 模型可视化:
* [VGG19](http://ethereon.github.io/netscope/#/gist/e2a91691f79bc8830a84de24f6d68155)   
* [MobileNet](http://ethereon.github.io/netscope/#/gist/d56116c37c78950b8b84fd937c1a052b)  
* [ResNet](http://ethereon.github.io/netscope/#/gist/41714c30513568c15e6641acb7c0ba12) 

## 学习曲线比对(前65000次迭代)
<table>
    <tr>
        <th>VggNet(baseline)</th>
        <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/vgg.png" width=100% height=50%></td>
    </tr>
    <tr>
        <th>MobileNet </th>
        <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/mobile.png" width=100% height=50%></td>
    </tr>
    <tr>
        <th>ResNet</th>
        <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/resnet.png" width=100% height=50%></td>
    </tr>
</table>


## 预处理验证:
(1) VGG: 零均值 + 归一化, 在ImageNet上效果较好。
![VggNet](https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/vgg1.png)

(2) ResNet:减mean_file,不用scale,(归一化则分类错误)分类结果比VGG要好。
![ResNet](https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/resnet1.png)

## 最终效果比对
最后200次迭代，同样大小的图片(224*224)

* Loss及耗时比对
<table>
    <tr>
        <th></th>
        <th>loss</th>
        <th>耗时(前向传播时间)</th>
    </tr>
    <tr>
        <th>VGG19</th>
        <td>183</td>
        <td>26ms</td>
    </tr>
        <th>MobileNet</th>
        <td>199</td>
        <td>16ms</td>
    </tr>
        <th>ResNet</th>
        <td>182</td>
        <td>21ms</td>
    </tr>
    </tr>
        <th>最终优化ResNet</th>
        <td>182</td>
        <td>17ms</td>
    </tr>
</table>
* 结果图比对
<table>
  <tr>
    <th>VggNet</th>
    <th>MobileNet</th>
    <th>ResNet</th>
</tr>
<tr>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/vgg2.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/mobile2.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/resnet2.png" width=100% height=70%></td>
</tr>
<tr>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/vgg3.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/mobile3.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/resnet3.png" width=100% height=70%></td>
</tr>
<tr>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/vgg4.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/mobile4.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/images/resnet4.png" width=100% height=70%></td>
</tr>
</table>

## Training
1. `cd /home/yuchen/Project/Realtime_Multi-Person_Pose_Estimation/training`
	
2. `sh train.sh r`   #测试ResNet
 
   `sh train.sh v`   #测试VggNet
   
   `sh train.sh m`   #测试MobileNet


## Testing
1. `cd /home/yuchen/Project/Realtime_Multi-Person_Pose_Estimation/testing/python`

2. `python model.py r`   #测试ResNet
 
   `python model.py v`   #测试VggNet
   
   `python model.py m`   #测试MobileNet
	
## 摄像头远程连接使用
* 1、获取远程连接代码
<pre>
git clone https://github.com/Maycbj/Share.git -b intern_sina`
</pre>

* 2、修改mac的ip地址 
<pre>
cd Share/Realtime_MultiPerson_Pose_Estimation/trans
vim receive.py 
address = ('10.236.10.44', 8003) -->  address = ('mac.de.i.p', 8003)
</pre>


* 3、登陆远程服务器：
<pre>
ssh root@10.85.125.105
cd /disk/data0/users/mayuchen/Project/Realtime_Multi-Person_Pose_Estimation/testing/python
vim server.py 
address_s = ('10.236.10.44', 8003) -->  address = ('mac.de.i.p', 8003)
</pre>

* 4、运行程序
<pre>
//本机上运行
sh run.sh
//立即在linux上运行
python server.py v
</pre>








