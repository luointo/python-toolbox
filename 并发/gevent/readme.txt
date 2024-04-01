pip install gevent

# https://blog.csdn.net/weixin_42143550/article/details/105452663


g=gevent.spawn(func,1,……,x=3,……)
#创建一个协程对象g ,spawn括号内第一个参数是函数名，后面可以有多个参数（位置参数，关键字参数）。
g.join()#等待结束
g.value#拿到func的返回值。


gevent.sleep(2)模拟的是gevent可以识别的IO阻塞。

而time.sleep()或其它的阻塞，gevent是不能直接识别的，需要下面一行代码，打补丁识别。

from gevent import monkey;mokey.patch_all()

这一行代码必需放在打补丁者的前面。为了方便，不如直接方在文件的开头位置。
————————————————
版权声明：本文为CSDN博主「miaoqinian」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/miaoqinian/article/details/80170824


gevent.spawn()方法会创建一个新的greenlet协程对象，并运行它

gevent.joinall()方法的参数是一个协程对象列表，它会等待所有的协程都执行完毕后再退出