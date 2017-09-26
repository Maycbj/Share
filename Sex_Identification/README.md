# fast-style-transfer

## 项目介绍
由于图像分类是图像处理领域中一大的研究方向，imagenet中都会涌现出大量优秀的模型，故踩在巨人的肩膀上，借用imagenet中优秀的模型，可以较容易的对图像进行分类。
项目对线上图片进行分类，共有9个类，主要以人像为主。

##网络结构设计
* 谈不上设计了，就是最基础的ResNet-50,网络模型  [可视化](http://ethereon.github.io/netscope/#/gist/6c1cb523a01d8f81a2387c132c08fa6d)  
* 数据集共40W张图片，训练测试集比例4:1，输入图像大小不定，且包含部分脏数据，过滤掉大小小于5KB的图片，将图像最短边缩放至256，中心裁剪得到(256*256)的图像。
* 由于fine-tuning的ResNet的边长为224，在训练集上随机裁剪(224*224)的图像，测试集上中心裁剪(224＊224)。
* 数据增强，翻转，随机裁剪。

##模型调参
* 由于GPU紧张，故开始只用了一张卡的一半内存，batchsize=16定的较小，训练出现了震荡，收敛比较慢，后来为了不占用过多内存，batchsize仍保持不变，12个batchsize的loss平均，更新模型，即itersize=12。虽然迭代次数变小了，但训练总时间缩短了。
* 观察训练集和测试集loss曲线，测试集loss略低于训练集，没有出现明显的过拟合情况，故没有加入Dropout层。
* 未来可以加入Dropout防止过拟合，加入BatchNorm加速收敛。
* 提升模型准确率的方向：
 * 加大网络深度，同时也要保证数据集能cover的了模型复杂度。
 * 使用ResNet系，ImageNet2017冠军 [SENet](https://github.com/hujie-frank/SENet)，显式地建模特征通道之间的相互依赖关系,对特征重标定。
 * 超参数的调整等。
 
##预测结果
<table>
    <tr>
        <th></th>
        <th>training set</th>
        <th>validation set</th>
        <th>testing set</th>
    </tr>
    <tr>
        <th>accuracy</th>
        <td>0.97</td>
        <td>0.95</td>
        <td>0.94</td>
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








