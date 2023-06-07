<img src="fig/stp.png" style="zoom:70%;" />

## STP Toolbox for Python

A Semi-tensor product toolbox adapted from matlab version
http://lsc.amss.ac.cn/~hsqi/soft/STP.zip



## What is STP？

The semi-tensor product (STP) of matrices is a novel matrix product, which is a generalization of conventional matrix product for the case when the two factor matrices even do not meet the dimension matching condition.



## Install 

```Python
pip install semi-tensor-product
```



## Usage

``` Python
import numpy
import stp
A=np.array()
B=np.array()

# performs the (left) semi-tensor product of two matrices
C=stp.sp(A,B)  

# performs the (left) semi-tensor product of finite set of matrices
C=stp.spn(A,A,B)
```

Please see `example01.py ` and `example02.py ` for more use cases.



## Citing STP

To cite this repository:

```
@software{stp2023github,
  author = {Huanianss},
  title = {{STP}: a {S}emi-tensor product toolbox of {P}ython programs},
  url = {https://github.com/Huanianss/semi-tensor-product},
  version = {0.0.4},
  year = {2023},
}
```



## Communication

If you have any requests for calculations using the semi-tensor product, please feel free to submit an issue or contact us huanianss@qq.com
