print("numpy")
import numpy as np
x = np.array([1.0, 2.0, 3.0][1.0, 2.0, 8.0])
y = np.array([1.0, 2.0, 3.0][1.0, 2.0, 8.0])
x * y
>>> x = np.array([[1,2,3],[4, 5, 6]])
>>> print(x)
[[1 2 3]
 [4 5 6]]
>>> x*67
array([[ 67, 134, 201],
       [268, 335, 402]])
>>> x=x*3
>>> print(x)
[[ 3  6  9]
 [12 15 18]]
>>> print(x.flatten())
[ 3  6  9 12 15 18]
>>> print(x)
[[ 3  6  9]
 [12 15 18]]
>>> x[0]
array([3, 6, 9])
>>> x[1,2]
18
>>> x[0, :2]
array([3, 6])
>>> import matplotlib.pyplot as plt
/Users/kazumaotsuka/anaconda/lib/python3.6/site-packages/matplotlib/font_manager.py:280: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  'Matplotlib is building the font cache using fc-list. '
>>> x = np.arrange(0, 6, 0.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'numpy' has no attribute 'arrange'
>>> x = np.arange(0, 6, 0.1)
>>> y = np.sin(x)
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x10d821128>]
>>> plt.show()
y1 = np.sin(x)
y2 = np.cos(x)
                                                                                    
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin&cos')
plt.legend()
plt.show()

exit

python
>>> y1 = np.sin(x)
>>> y2 = np.cos(x)
>>> 
>>> plt.plot(x, y1, label="sin")
[<matplotlib.lines.Line2D object at 0x109c91160>]
>>> plt.plot(x, y2, linestyle="--", label="cos")
[<matplotlib.lines.Line2D object at 0x109c91ac8>]
>>> plt.xlabel("x")
<matplotlib.text.Text object at 0x110d8ec50>
>>> plt.ylabel("y")
<matplotlib.text.Text object at 0x10d7c6080>
>>> plt.title('sin&cos')
<matplotlib.text.Text object at 0x111dc7320>
>>> plt.legend()
<matplotlib.legend.Legend object at 0x109c91cf8>
>>> plt.show()


