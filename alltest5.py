from werkzeug.security import generate_password_hash, check_password_hash

# for i in range(30):
#     pw = 'itrim100po'
#     pw_hash = generate_password_hash(pw, salt_length=12)
#     print(len(pw_hash), pw_hash)

# print(check_password_hash('pbkdf2:sha256:150000$9ymHYUlg$eb745944827e25cdaf804da896e3d1fb7347927f091415a294575ffec9fbc087', 'itrim100po'))

# print(len('pbkdf2:sha256:150000$4Qx6i5Lq$a7defc39b527d48ec6ceb5c3a832c1b79140805f232cb8841223a284a59d6132'))
# print(len('pbkdf2:sha256:150000$9ymHYUlg$eb745944827e25cdaf80'))
# new = 'pbkdf2:sha256:150000$YdytqVy2$a8566d2f544c1b358013'

# print(check_password_hash(new, 'itrim100po'))


# import pymongo
# myclient = pymongo.MongoClient("mongodb://140.96.89.218:27017/")
# print(myclient.list_database_names())
# mydb = myclient["mydatabase"]

from sklearn import datasets
iris = datasets.load_iris()
# print(iris.keys())
# print(iris['data'])

dd = {"RX1_1":"-2762893094328157.5","RX1_2":"-2762893094328147.0","RX1_3":"-2762893094328149.0","RX1_4":"-2762893094328130.0","RX1_5":"-2762893094328130.5","RX1_6":"-2762893094328123.0","RX1_7":"-2762893094328116.5","RX1_8":"-2762893094328106.5","RX2_1":"-2762893094328063.0","RX2_2":"-2762893094328048.5","RX2_3":"-2762893094328074.0","RX2_4":"-2762893094328051.5","RX2_5":"-2762893094328037.0","RX2_6":"-2762893094328027.0","RX2_7":"-2762893094328017.0","RX2_8":"-2762893094328007.0","RX3_1":"-2762893094327987.0","RX3_2":"-2762893094327977.0","RX3_3":"-2762893094327970.0","RX3_4":"-2762893094327960.0","RX3_5":"-2762893094327951.0","RX3_6":"-2762893094327939.0","RX3_7":"-2762893094327896.5","RX3_8":"-2762893094327883.0","RX3_9":"-2762893094327874.5","VXX2_1":"-2762893094327864.5","CWXR_1":"-2762893094327854.5","CWXR_2":"-2762893094327844.5","CWXR_3":"-2762893094327839.0","RX4_1":"-2762893094327829.0","RX4_2":"-2762893094327814.5","RX4_3":"-2762893094327804.5","RX4_4":"-2762893094327794.5","RX4_5":"-2762893094327784.5","RX4_6":"-2762893094327774.5","RX4_7":"-2762893094327764.5","RX4_8":"-2762893094327754.5","VXXX_1":"-2762893094327744.5","EXXX1_1":"-2762893094327739.0","YXX_1":"-2762893094327709.0"}
print(dd['RX2_2'])
print(float(dd['RX2_2']))

import pickle
print(pickle.format_version)

#python3
x = {1:1, 0:0, 2:2}
x.pop(1)
print(x)
# {0: 0, 2: 2}

y = {1:1, 0:0, 2:2}
del y[1]
print(y)
# {0: 0, 2: 2}

# 兩種方式皆可用

# 更新+刪除
y[1] = y.pop(0)
print(y)
d = {'test':[0,1,2]}

d[0] = d.pop('test')
print(d)