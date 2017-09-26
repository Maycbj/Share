# fast-style-transfer

## 项目介绍
由于图像分类是图像处理领域中一大的研究方向，imagenet中都会涌现出大量优秀的模型，故踩在巨人的肩膀上，借用imagenet中优秀的模型，可以较容易的对图像进行分类。

##网络结构



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








