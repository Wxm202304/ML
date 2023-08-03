# 特征归一化
from sklearn.preprocessing import MinMaxScaler
x=[[10001,2],[16020,4],[12008,6],[13131,8]]
min_max_scaler = MinMaxScaler()#这里面可以通过feature属性设置区间范围，默认0-1
X_train_minmax = min_max_scaler.fit_transform(x)#归一化后的结果
