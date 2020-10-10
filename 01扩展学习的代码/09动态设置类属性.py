class EnvData:
    # 定义一个类，用来保存用例执行过程中，提取出来的数据！
    pass


data = {"member_id":188,"mobile_phone":13410005678}
token = "hanbja[njfnaigdfnbfnnjnjadgbnadobj[nobnoaibgabgadgabgabfn"

# 动态的设置类属性
setattr(EnvData,"member_id",188)
# setattr(EnvData,"mobile_phone",13410005678)
# setattr(EnvData,"token","hanbja[njfnaigdfnbfnnjnjadgbnadobj[nobnoaibgabgadgabgabfn")

# 获取类属性
print(EnvData.member_id) # 188

print(getattr(EnvData,"member_id"))    # 188
