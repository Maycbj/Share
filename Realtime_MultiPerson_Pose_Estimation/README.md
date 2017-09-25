# Realtime MultiPerson Pose Estimation

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

## 学习曲线比对(前65000次迭代)
<table>
    <tr>
        <th>VggNet(baseline)</th>
        <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/vgg.png" width=100% height=100%></td>
    </tr>
    <tr>
        <th>MobileNet </th>
        <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/mobile.png" width=100% height=100%></td>
    </tr>
    <tr>
        <th>ResNet</th>
        <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/resnet.png" width=100% height=100%></td>
    </tr>
</table>


## 预处理验证:
(1) VGG: 零均值 + 归一化, 在ImageNet上效果较好。
![VggNet](https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/vgg1.png)

(2) ResNet:减mean_file,不用scale,(归一化则分类错误)分类结果比VGG要好。
![ResNet](https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/resnet1.png)

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
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/vgg2.png" width=100% height=100%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/mobile2.png" width=100% height=100%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/resnet2.png" width=100% height=100%></td>
</tr>
<tr>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/vgg3.png" width=100% height=100%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/mobile3.png" width=100% height=100%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/resnet3.png" width=100% height=100%></td>
</tr>
<tr>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/vgg4.png" width=100% height=100%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/mobile4.png" width=100% height=100%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/SharePictures/master/internship/sina/Realtime_MultiPerson_Pose_Estimation/resnet4.png" width=100% height=100%></td>
</tr>
</table>

##摄像头远程连接使用
* 1、获取远程连接代码

 `git clone https://github.com/Maycbj/Share.git -b intern_sina`
 
* 2、修改mac的ip地址 
<pre>
	`cd Share/internship/sina/Realtime_MultiPerson_Pose_Estimation/trans
	vim receive.py 
	address = ('10.236.10.44', 8003) -->  address = ('mac.de.i.p', 8003)`
</pre>


* 3、登陆远程服务器：
<pre>
`ssh root@10.85.125.105
cd /disk/data0/users/mayuchen/Project/Realtime_Multi-Person_Pose_Estimation/testing/python
vim server.py 
address_s = ('10.236.10.44', 8003) -->  address = ('mac.de.i.p', 8003)`
</pre>

* 4、运行程序
<pre>
`//本机上运行
sh run.sh
//立即在linux上运行
python server.py v` 
</pre>








