#### Tensorflow training time depending on the instance configuration  

<!--

| CPU/GPU | Instance | Tensorflow | Training image | Time, sec (lower better) |
|:-:|:-:|:-:|:-:|:-|
| CPU | c4.4xlarge | 1.11.0 | default<sup>1</sup> | <span style="display: inline-block; overflow: hidden; width:166px; background-color:lightgray;">&nbsp;552</span> |
| CPU | c5.4xlarge | 1.11.0 | default<sup>1</sup> | <span style="display: inline-block; overflow: hidden; width:143px; background-color:lightgray;">&nbsp;475</span> |
| CPU | c5.4xlarge | 2.0.0 | default | <span style="display: inline-block; overflow: hidden; width:122px; background-color:lightgray;">&nbsp;407</span> |
| CPU | c5.4xlarge | 2.1.0 | manually upgraded | <span style="display: inline-block; overflow: hidden; width:79px; background-color:lightgray;">&nbsp;262</span> |
| GPU | p3.2xlarge | 2.0.0 | default | <span style="display: inline-block; overflow: hidden; width:93px; background-color:lightgray;">&nbsp;311</span> |
| GPU | p3.2xlarge | 2.1.0 | manually upgraded <sup>2</sup> | <span style="display: inline-block; overflow: hidden; width:130px; background-color:lightgray;">&nbsp;433</span> |

-->

<div style="text-align: left">
<img src="table.png" alt="drawing" width="600"/>
</div>
    
___  

<sup>1</sup> SageMaker default, if no `framework_version` parameter is provided.  
<sup>2</sup> fallback to CPU due to unmet dependencies.

* c4 is based on Intel Xeon E5-2666 v3 (Haswell) with AVX2 (256).
* C5 is based on Intel Xeon Scalable Processors (Cascade Lake) with AVX512.
* p3 is based on NVIDIA Volta V100 GPU.