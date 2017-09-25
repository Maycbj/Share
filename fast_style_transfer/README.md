# fast-style-transfer

## 项目地址
[论文地址](https://arxiv.org/abs/1508.06576)
[代码地址](https://github.com/lengstrom/fast-style-transfer#stylizing-video)

## 项目介绍
Add styles from famous paintings to any photo in a fraction of a second! [You can even style videos!](#video-stylization)

Our implementation is based off of a combination of Gatys' [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576), Johnson's [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://cs.stanford.edu/people/jcjohns/eccv16/), and Ulyanov's [Instance Normalization](https://arxiv.org/abs/1607.08022). 

https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/wave1.jpg

##网络结构
[](https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/net.jpg)
## 风格转换结果(时间压缩版本)
<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/wave1.jpg' height='200' width='300'/>
</p>
<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/wave1.jpg' height='200' width='300'/>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/wave.jpg' height='200' width='300'/>
</p>

<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/mountains1.jpg' height='200' width='300'/>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/mountains.jpg' height='200' width='300'/>
</p>

<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/la_muse1.jpg' height='200' width='300'/>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/la_muse.jpg' height='200' width='300'/>
</p>


<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/star1.jpg' height='200' width='300'/>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/star.jpg' height='200' width='300'/>
</p>

<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/strange1.jpg' height='200' width='300'/>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/strange.jpg' height='200' width='300'/>
</p>



0823_wave_contentweight_15_relu4_2/1_1500.png
0823_la_muse_contentweight_25_relu4_2/0_10000.png
0823_star_contentweight_15_relu4_2/1_500.png
0823_strange_contentweight_100_relu3_3/1_10000.png
0823_mountains_contentweight_25_relu4_2/0_9500.png



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
    <th>ModelName</th>
    <th>StyleImage</th>
    <th>ResultImage</th>
</tr>
<tr>
    <td>wave</td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/mobile2.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/resnet2.png" width=100% height=70%></td>
</tr>
<tr>
    <td>mountains</td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/mobile3.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/resnet3.png" width=100% height=70%></td>
</tr>
<tr>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/vgg4.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/mobile4.png" width=100% height=70%></td>
    <td><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Realtime_MultiPerson_Pose_Estimation/resnet4.png" width=100% height=70%></td>
</tr>
</table>

##摄像头远程连接使用
* 1、获取远程连接代码
<pre>
git clone https://github.com/Maycbj/Share.git -b intern_sina`
</pre>

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








