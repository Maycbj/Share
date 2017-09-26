# fast-style-transfer

## 项目地址
[论文地址](https://arxiv.org/abs/1508.06576)
[代码地址](https://github.com/lengstrom/fast-style-transfer#stylizing-video)

## 项目介绍
Add styles from famous paintings to any photo in a fraction of a second! [You can even style videos!](#video-stylization)

Our implementation is based off of a combination of Gatys' [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576), Johnson's [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://cs.stanford.edu/people/jcjohns/eccv16/), and Ulyanov's [Instance Normalization](https://arxiv.org/abs/1607.08022). 

https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/wave1.jpg

##网络结构

<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/net.jpg' height=70% width=70%/>
</p>

* 项目分为两个网络结构，分为图片转换模块和特征提取模块。
 * 图片转换模块：输入图片(内容图片)先用多个卷积层提取高维特征，再通过残差网络对高维特征进行转换，再反卷积为低维特征。(ImageTransformNet)
 * 特征提取模块：将转换后图片、风格图片、内容图片都通过Vgg,提取高维特征，同时对转换后图片相关矩阵和风格图片相关矩阵做loss,对转换后图片相关矩阵和内容图片像素级做loss。一般来说，层级越高，表示就越抽象。
(LossNet)
* 由大量实验发现
 * 风格重建：越用高层的特征，风格重建的就越粗粒度化。(下图的上面一行)
 * 内容重建：越是底层的特征，重建的效果就越精细，越不容易变形。(下图的下面一行)

<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/ratio.jpg' height='400' width='600'/>
</p>

* 由于是提升预测部分的计算性能，压缩计算时间，所以只要压缩imageTransformNet部分的网络结构，而不用关心Vgg的耗时。

* 本项目对VGG-16没有压缩，对ImageTransformNet进行压缩，缩小卷积核、减小特征图的通道数、减小层数等方式。


##Trainging
使用`style.py`训练模型。用单块M40上训练4小时左右，具体的字段解释请[单击这](https://github.com/lengstrom/fast-style-transfer/blob/master/docs.md#style)。

	python style.py --style examples/style/wave.jpg \
	  --checkpoint-dir model/snapshot/wave/ \
	  --test examples/content/stata.jpg \
	  --test-dir output/train_res/${NAME}/ \
	  --content-weight 100 \
	  --content-layer relu4_2 \
	  --checkpoint-iterations 500 \
	  --batch-size 4\
	  --log-name wave.log
	  	  
##Testing
使用`evaluate.py`可以测试该模型。
	
	python evaluate.py \
	  --checkpoint model/final_model/wave/fns.ckpt \
	  --in-path examples/single_content/ \
	  --out-path output/single_content/ \
	  --batch-size 1 \
	  --allow-different-dimensions
  
## 风格转换结果(时间压缩版本)
<p align='center'>
  <img src='https://raw.githubusercontent.com/Maycbj/Share/intern_sina/fast_style_transfer/images/stata.jpg' height='200' width='300'/>
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



[模型下载](https://github.com/Maycbj/Share/tree/intern_sina/fast_style_transfer/code/final_model)

## 最终效果比对
* Loss及耗时比对
<table>
    <tr>
        <th></th>
        <th>耗时</th>
        <th>模型大小</th>
    </tr>
    <tr>
        <th>原始模型</th>
        <td>100ms</td>
        <td>19MB</td>
    </tr>
    <tr>
        <th>压缩模型</th>
        <td>14ms</td>
        <td>344KB</td>
    </tr>
    <tr>
        <th>压缩比例</th>
        <td>14%</td>
        <td>1.8%</td>
    </tr>
</table>


##摄像头远程连接使用
* 1、获取远程连接代码
<pre>
git clone https://github.com/Maycbj/Share.git -b intern_sina`
</pre>

* 2、修改mac的ip地址 
<pre>
cd Share/fast_style_transfer/code/socket
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








