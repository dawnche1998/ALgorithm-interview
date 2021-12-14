



## pre-process

1. 读取图片 

   `img=cv2.imread(image_names[cnt]) # 720*1280*3 `

2. 对图片进行预处理

   ```python
   # pre_process : Crop, resize, and normalize image. Gather meta data for post processing and tracking.
   1. _transform_scale
   2. get_affine_transform
   ```

## model

```python
heads = {
	'hm':opt.num_classes, #1
	'reg': 2, 
	'wh': 2,
	'tracking': 2,
	'hps': dataset.num_joints * 2, #34
	'hm_hp': dataset.num_joints, # 1
	'hp_offset': 2 }
```





1. create model 

```python
   if 'multi_pose' in opt.task:
        opt.heads.update({
        'hps': dataset.num_joints * 2, 'hm_hp': dataset.num_joints,
        'hp_offset': 2})
```

```
model = DLA([1, 1, 1, 2, 2, 1],
            [16, 32, 64, 128, 256, 512],
            block=BasicBlock, **kwargs)
```

model的结构



## decode

1. decode
2. post-process
3. merge-output
4. show-results

## tracker





---

## Ques

### open-cv

1. cv2.waitkey() https://blog.csdn.net/weixin_44049693/article/details/106271643

   ```python
   if cv2.waitKey(100) == 27:
   """
   等待用户触发事件,等待时间为100ms，
   如果在这个时间段内, 用户按下ESC(ASCII码为27),执行if体
   如果没有按，if函数不做处理
   """
   ```

2. 

### python

```python
self.__setattr__(keys, values) 
```

###  [raise NotImplementedError](https://blog.csdn.net/qq_40666620/article/details/105026716)

```python
raise NotImplementedError
raise NotImplementedError的使用感觉很类似于C++中虚函数的效果，它的意思是如果这个方法没有被子类重写，但是调用了，就会报错。
```



### pytorch

```python
torch.cuda.synchronize()
torch.clamp()
```

---

1. pytorch中常用的相似度评估方法 https://mp.weixin.qq.com/s/OVB-QuHFzKe43Naf5kmiSQ pytorch中六种常用的向量相似度评估方法pytorch中六种常用的向量相似度评估方法







---





