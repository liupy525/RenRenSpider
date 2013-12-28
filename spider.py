#!/usr/bin/env python
#encoding=utf-8

import urllib, urllib2, cookielib, re, sys, threading

myemail = ''
mypassword = ''
myid = ''

class  Renren(threading.Thread):

    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.origURL='http://www.renren.com/Home.do'
        self.domain='renren.com'
        self.cj = cookielib.LWPCookieJar()

        try:
            self.cj.revert('renren,cookie')
        except:
            None

        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self):
        params = {'email':self.email,'password':self.password,'origURL':self.origURL,'domain':self.domain}
        req = urllib2.Request(
            'http://www.renren.com/PLogin.do',
            urllib.urlencode(params)      
        )
        r = self.opener.open(req)

    def friends(self):
        print "Get my friends"
        f = self.getmyfriends()
        print "friends list"
        print f,len(f)

        #todo
        self.todolist=f     
        self.donelist=[]

        #write data
        fdata=open('data00.txt','w')
        for item in f:
            fdata.write(item+' ')
        fdata.close()

    def realfun(self, x):
        filename="data"+x+'.txt'
        fp=open(filename,'w')
        
        while True:
            rrid=self.getone()
            if rrid==1:
                break
            print rrid
            f=self.getfriends(rrid)
            templst=''
            for eachid in f:
                templst=eachid+' '+templst

            fp.write(rrid+'@@@@@@@@@@@@@@@\n'+templst)
            fp.write('\n')
        fp.close()

    def realrun(self):
        th1 = threading.Thread(target=self.realfun,args=('1'))
        th2 = threading.Thread(target=self.realfun,args=('2'))
        th3 = threading.Thread(target=self.realfun,args=('3'))
        th4 = threading.Thread(target=self.realfun,args=('4'))
        th5 = threading.Thread(target=self.realfun,args=('5'))
        th6 = threading.Thread(target=self.realfun,args=('6'))
        th7 = threading.Thread(target=self.realfun,args=('7'))
        th8 = threading.Thread(target=self.realfun,args=('8'))
        th9 = threading.Thread(target=self.realfun,args=('9'))
        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th6.start()
        th7.start()
        th8.start()
        th9.start()

    def getfriends(self,rrid):
        friends=[]
        count=0

        while True:
            count1 = str(count)
            req="http://friend.renren.com/GetFriendList.do?curpage="+count1+'&id='+str(rrid)
            print 'Get',req
            r=self.opener.open(req)
            data=r.read()
            f=re.findall('<a id="addFriend(\d{5,15})"',data)
            friends=friends+f
            count=count+1
            if f == []:
				return friends

    def getmyfriends(self):
		friends = []
		count=0

		while True:
			count1 = str(count)
			req="http://friend.renren.com/GetFriendList.do?curpage="+count1+'&id='+str(myid)
			print 'Get',req
			r=self.opener.open(req)
			data=r.read()
			f=re.findall('Poke.do\?id=(\d{5,15})" oncl',data)
			print f
			friends=friends+f
			count=count+1
			if f == []:
				return friends

    def getone(self):
        if self.todolist==[]:
            print "Empty todo list"
            return 1
        popup=self.todolist[0]   
        self.donelist.append(popup) 
        del self.todolist[0]        
        return popup                
                
if __name__ == "__main__":
    a=Renren(myemail, mypassword)
    print "your account and password are %s %s" % (myemail, mypassword)
    a.login()
    a.friends()
    a.realrun()
    
