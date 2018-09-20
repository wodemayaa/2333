print("欢迎使用迷之转换器")
print("请问您想实现什么功能呢?")
print("1.明文的sha256加密")
print("2.明文的base64加密")
print("3.base64乱码解密")
print("4.创建网址二维码")
print("5.玩弄base64")
temp=input("请输入相应的编号:")
while True:
    try:
        temp=int(temp)
        while(temp<=0 or temp>=6):
            temp=input("请输入正确格式的数字：")
            temp=int(temp)
        break
    except:
        temp=input("请输入正确格式的数字：")
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
    input("要继续将加密结果转换为明文吗？")
    jiem=base64.b64decode(jiam)
    print("再次解密结果为:",str(jiem,'utf-8'))
    
elif(temp==4):
    #二维码生成
    data=input("请输入想要创建二维码的网址：")
    img_file=r'E:\qrcode\py_qrcode.png'
    img=qrcode.make(data)
    img.save(img_file)
    img.show()
    
elif(temp==1):
    #sha256加密
    pw=input("请输入想要加密的明文：")
    sha256=hashlib.sha256()
    sha256.update(pw.encode('utf-8'))
    res=sha256.hexdigest()
    print("sha256加密结果：",res)
    
elif(temp==2):
    pw=input("请输入想要加密的明文：")
    jiam=base64.b64encode(pw.encode("utf-8"))
    jiam=str(jiam,'utf-8')
    print("base64加密结果为：",jiam)
    
elif(temp==3):
    lm=input("请输入想要解密的base64码：")
    t=0
    while(t<1):
        try:
            jiem=base64.b64decode(lm)
            break
        except:
            lm=input("请输入规范的base64码：")
    print("解码结果为:",str(jiem,'utf-8'))
    
answer=input("还需要继续服务吗，输入yes即可继续使用：")
while(answer=='yes'):
    print("请问您想实现什么功能呢?")
    print("1.明文的sha256加密")
    print("2.明文的base64加密")
    print("3.base64乱码解密")
    print("4.创建网址二维码")
    print("5.玩弄base64")
    temp=input("请输入相应的编号:")
    while True:
        try:
            temp=int(temp)
            while(temp<=0 or temp>=6):
                temp=input("请输入正确格式的数字：")
                temp=int(temp)
            break
        except:
            temp=input("请输入正确格式的数字：")
    if(temp==5):
        #base64转换
        pw=input("请输入想要加密的明文：")
        jiam=base64.b64encode(pw.encode("utf-8"))
        jiam=str(jiam,'utf-8')
        print("base64加密结果为：",jiam)
        input("要继续将加密结果转换为明文吗？")
        jiem=base64.b64decode(jiam)
        print("再次解密结果为:",str(jiem,'utf-8'))
        
    elif(temp==4):
        #二维码生成
        data=input("请输入想要创建二维码的网址：")
        img_file=r'E:\qrcode\py_qrcode.png'
        img=qrcode.make(data)
        img.save(img_file)
        img.show()
        
    elif(temp==1):
        #sha256加密
        pw=input("请输入想要加密的明文：")
        sha256=hashlib.sha256()
        sha256.update(pw.encode('utf-8'))
        res=sha256.hexdigest()
        print("sha256加密结果：",res)
        
    elif(temp==2):
        pw=input("请输入想要加密的明文：")
        jiam=base64.b64encode(pw.encode("utf-8"))
        jiam=str(jiam,'utf-8')
        print("base64加密结果为：",jiam)
        
    elif(temp==3):
        lm=input("请输入想要解密的base64码：")
        while True:
            try:
                jiem=base64.b64decode(lm)
                break
            except:
                lm=input("请输入规范的base64码：")
        print("解码结果为:",str(jiem,'utf-8'))
    answer=input("还需要继续服务吗,输入yes即可继续使用:")
    yes=str(answer)
    if(answer!='yes'):
        break
input("感谢您的使用。")



    
