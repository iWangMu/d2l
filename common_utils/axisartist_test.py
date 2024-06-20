import mpl_toolkits.axisartist as axisartist
import matplotlib.pyplot as plt
import numpy as np

#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0, 0)
#给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("-|>", size = 1.0)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")
# x、y轴的颜色
ax.axis["x"].line.set_color("black")
ax.axis["y"].line.set_color("black")


# # x, y
# x = np.arange(-7, 1.01, 0.1)
# y = [v ** 2 + 6 * v + 12 for v in x]

# # 设置x、y坐标轴的范围
# plt.xlim(-7.5, 1.5)
# plt.ylim(-1, 21)
# # 设置x、y坐标轴的刻度
# ax.set_xticks([xt for xt in np.arange(-7, 1.1, 1)])
# ax.set_yticks([yt for yt in np.arange(0, 20.1, 2) if yt != 0])
# # 绘制图形
# plt.plot(x, y, color='blue', linewidth="1")
# plt.show()



x = np.arange(0, 8.01, 0.1)
y = [8*v-v**2 for v in x]
# 设置x、y坐标轴的范围
plt.xlim(-0.5, 8.5)
plt.ylim(-0.5, 17)
# 设置x、y坐标轴的刻度
ax.set_xticks([xt for xt in np.arange(0, 8.1, 1)])
ax.set_yticks([yt for yt in np.arange(0, 16.1, 2) if yt != 0])
# 绘制图形
plt.plot(x, y, color='blue', linewidth="1")
plt.show()


