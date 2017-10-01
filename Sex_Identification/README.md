# Sex_Identification

## 项目介绍
由于图像分类是图像处理领域中一大的研究方向，imagenet中都会涌现出大量优秀的模型，故踩在巨人的肩膀上，借用imagenet中优秀的模型，可以较容易的对图像进行分类。
项目对线上图片进行分类，共有9个类，主要以人像为主。

##数据采集使用
实时爬取线上的图片数据，图片共分为9类，数据采集路径`/data0/users/mayuchen/Project/GrabPic`

1. 先通过Kafka获得图片pid和分类，共有四个通道(四个ip地址)，但观察发现四个通道的图片信息格式基本相似。
2. 使用`consumer.py`对Kafka队列的数据实时采集，平均每秒大约2张图片的信息。爬去得到图片的pid和类别信息，以存放在对应日期下的`info`文件夹下。
3. 使用`get_img.py`对读取前一天采集到的图片pid信息获取图片，并放到对应日期下的`img`文件夹下。

使用`run_all.sh`可以一键式启动数据采集，每天0点会自动关闭consumer，同时重启一个新的consumer获取数据，同时对前一天的图片`get_img`获取图片。


##网络结构设计
* 谈不上设计了，就是最基础的ResNet-50,网络模型  [可视化](http://ethereon.github.io/netscope/#/gist/6c1cb523a01d8f81a2387c132c08fa6d)  
* 数据集共40W张图片，训练测试集比例4:1，输入图像大小不定，且包含部分脏数据，过滤掉大小小于5KB的图片，将图像最短边缩放至256，中心裁剪得到(256*256)的图像。
* 由于fine-tuning的ResNet的边长为224，在训练集上随机裁剪(224*224)的图像，测试集上中心裁剪(224＊224)。
* 数据增强，翻转，随机裁剪。

##模型调参
* 由于GPU紧张，故开始只用了一张卡的一半内存，batchsize=16定的较小，训练出现了震荡，收敛比较慢，后来为了不占用过多内存，batchsize仍保持不变，12个batchsize的loss平均更新模型，即itersize=12。虽然迭代次数变小了(只迭代了1w次)，但训练总时间缩短了。
* 观察训练集和测试集loss曲线，测试集loss略低于训练集，没有出现明显的过拟合情况，故没有加入Dropout层。
* 未来可以加入Dropout防止过拟合，加入BatchNorm加速收敛。
* 提升模型准确率的方向：
 * 加大网络深度，同时也要保证数据集能cover的了模型复杂度。
 * 使用ResNet系，ImageNet2017冠军 [SENet](https://github.com/hujie-frank/SENet)，显式地建模特征通道之间的相互依赖关系。
 * 超参数的调整等。
 
<p align='center'><img src="https://raw.githubusercontent.com/Maycbj/Share/intern_sina/Sex_Identification/images/loss.jpg" width=500 height=300 align="center"></p>

## 模型修改
将原始的ResNet-50最后一层的全连接层输出类别个数改为10类。

## 预测结果
<p align='center'>
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
</p>

## Training
	1. ssh root@10.85.125.105
	2. cd /home/yuchen/Project/nsfw
	3. caffe/build/tools/caffe train \
		--solver=model/resnet50_cvgj_solver.prototxt  \
		--gpu=0 \
		--weights=snapshot/resnet50_cvgj_20170917/resnet50_cvgj_iter_2000.caffemodel

## Testing
	1. cd /home/yuchen/Project/nsfw
	2. python ./classify_resnet.py \
		--pretrained_prototxt model/resnet50_cvgj_deploy.prototxt \
		--pretrained_model snapshot/resnet50_cvgj_20170918_poly/resnet50_cvgj_iter_10000.caffemodel \
		--input_file final_data_resize/tag/val.txt
	
	
`--pretrained_prototxt`:模型的结构的路径

`--pretrained_model`:模型训练好的模型的路径

`--input_file`:测试图片的地址文件，包括文件路径和真实的label

最终输出在该测试集上预测的准确率。

#### 输出结果

	                   File_path				         | True label |Predict label|    Score
	                   						...
	selfie_handsome_005ILOTely1fjbd4o0wu2j30ku112add.jpg |          8 |           8 |    7.32968
	           girl_005FbHZmly1fjfwjg7c1rj30m80m8wmu.jpg |          6 |           6 |    10.7992
	    sexy_beauty_a3ae3f61ly1fjbrq7m4xoj20cs0cs401.jpg |          9 |           9 |     9.1538
	            boy_005KOqgSly1fjerbbaz23j30qo1417lc.jpg |          3 |           3 |    7.64662
	            cat_6f05b989ly1fjehx2ojfaj20qo1bf4a7.jpg |          4 |           4 |    11.4872
	            dog_62daab0dgy1fjb1y4o86kj21lg1lgtrs.jpg |          5 |           5 |    11.1144
	The accuracy of 1000 pictures is 0.945 (945/1000)





