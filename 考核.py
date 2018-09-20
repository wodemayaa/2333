# 2333
print("欢迎使用迷之转换器")
print("请问您想实现什么功能呢?")
print("1.明文的sha256加密")
print("2.明文的base64加密")
print("3.base64乱码解密")
print("4.创建网址二维码")
print("5.玩弄base64")
temp=input("请输入相应的编号:")
temp=int(temp)
import base64
import os
import qrcode
import hashlib
if(temp==5):
    #base64转换
    pw=input("请输入想要加密的明文：")
    jiam=base64.b64encode(pw.encode("utf-8"))
    jiam=str(jiam,'utf-8')
    print("base64加密结果为：",jiam)
    print("要继续将加密结果转换为明文吗？")
    os.system("pause")
    jiem=base64.b64decode(jiam)
    print("再次解密结果为:",str(jiem,'utf-8'))
    os.system("pause")
elif(temp==4):
    #二维码生成
    data=input("请输入想要创建二维码的网址：")
    img_file=r'E:\qrcode\py_qrcode.png'
    img=qrcode.make(data)
    img.save(img_file)
    img.show()
    os.system("pause")
elif(temp==1):
    #sha256加密
    pw=input("请输入想要加密的明文：")
    sha256=hashlib.sha256()
    sha256.update(pw.encode('utf-8'))
    res=sha256.hexdigest()
    print("sha256加密结果：",res)
    os.system("pause")
elif(temp==2):
    pw=input("请输入想要加密的明文：")
    jiam=base64.b64encode(pw.encode("utf-8"))
    jiam=str(jiam,'utf-8')
    print("base64加密结果为：",jiam)
    os.system("pause")
elif(temp==3):
    lm=input("请输入想要解密的base64码：")
    jiem=base64.b64decode(lm)
    print("解码结果为:",str(jiem,'utf-8'))
    os.system("pause")
else:
    print("这样的要求人家做不到啦嘤嘤嘤。")
    print("记得输入正确的数字哦!")
answer=input("还需要继续服务吗:(yes or no)：")
while(answer=='yes'):
    print("请问您想实现什么功能呢?")
    print("1.明文的sha256加密")
    print("2.明文的base64加密")
    print("3.base64乱码解密")
    print("4.创建网址二维码")
    print("5.玩弄base64")
    temp=input("请输入相应的编号:")
    temp=int(temp)
    import base64
    import os
    import qrcode
    import hashlib
    if(temp==5):
        #base64转换
        pw=input("请输入想要加密的明文：")
        jiam=base64.b64encode(pw.encode("utf-8"))
        jiam=str(jiam,'utf-8')
        print("base64加密结果为：",jiam)
        print("要继续将加密结果转换为明文吗？")
        os.system("pause")
        jiem=base64.b64decode(jiam)
        print("再次解密结果为:",str(jiem,'utf-8'))
        os.system("pause")
    elif(temp==4):
        #二维码生成
        data=input("请输入想要创建二维码的网址：")
        img_file=r'E:\qrcode\py_qrcode.png'
        img=qrcode.make(data)
        img.save(img_file)
        img.show()
        os.system("pause")
    elif(temp==1):
        #sha256加密
        pw=input("请输入想要加密的明文：")
        sha256=hashlib.sha256()
        sha256.update(pw.encode('utf-8'))
        res=sha256.hexdigest()
        print("sha256加密结果：",res)
        os.system("pause")
    elif(temp==2):
        pw=input("请输入想要加密的明文：")
        jiam=base64.b64encode(pw.encode("utf-8"))
        jiam=str(jiam,'utf-8')
        print("base64加密结果为：",jiam)
        os.system("pause")
    elif(temp==3):
        lm=input("请输入想要解密的base64码：")
        jiem=base64.b64decode(lm)
        print("解码结果为:",str(jiem,'utf-8'))
        os.system("pause")
    else:
        print("这样的要求人家做不到啦嘤嘤嘤。")
    answer=input("还需要继续服务吗:(yes or no)：")
    yes=str(answer)
    if(answer=='no'):
        break


    
