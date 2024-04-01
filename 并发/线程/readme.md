在Python3中，通过threading模块提供线程的功能。原来的thread模块已废弃。但是threading模块中有个Thread类（大写的T，类名），是模块中最主要的线程类，一定要分清楚了，千万不要搞混了。

threading模块提供了一些比较实用的方法或者属性，例如：


| 方法与属性         | 描述                                                                 |
| -------------------- | ---------------------------------------------------------------------- |
| current_thread()   | 返回当前线程                                                         |
| active_count()     | 返回当前活跃的线程数，1个主线程+n个子线程                            |
| get_ident()        | 返回当前线程                                                         |
| enumerater()       | 返回当前活动 Thread 对象列表                                         |
| main_thread()      | 返回主 Thread 对象                                                   |
| settrace(func)     | 为所有线程设置一个 trace 函数                                        |
| setprofile(func)   | 为所有线程设置一个 profile 函数                                      |
| stack_size([size]) | 返回新创建线程栈大小；或为后续创建的线程设定栈大小为 size            |
| TIMEOUT_MAX        | Lock.acquire(), RLock.acquire(), Condition.wait() 允许的最大超时时间 |

threading模块包含下面的类：

- Thread：基本线程类
- Lock：互斥锁
- RLock：可重入锁，使单一进程再次获得已持有的锁(递归锁)
- Condition：条件锁，使得一个线程等待另一个线程满足特定条件，比如改变状态或某个值。
- Semaphore：信号锁。为线程间共享的有限资源提供一个”计数器”，如果没有可用资源则会被阻塞。
- Event：事件锁，任意数量的线程等待某个事件的发生，在该事件发生后所有线程被激活
- Timer：一种计时器
- Barrier：Python3.2新增的“阻碍”类，必须达到指定数量的线程后才可以继续执行。

## 1. 多线程

有两种方式来创建线程：一种是继承Thread类，并重写它的run()方法；另一种是在实例化`threading.Thread`对象的时候，将线程要执行的任务函数作为参数传入线程。

第一种方法：

```
import threading

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        # 注意：一定要显式的调用父类的初始化函数。
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("%s正在运行中......" % self.name)

if __name__ == '__main__':  
    for i in range(10):
        MyThread("thread-" + str(i)).start()
```

第二种方法：

```
import threading
import time

def show(arg):
    time.sleep(1)
    print('thread '+str(arg)+" running....")

if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=show, args=(i,))
        t.start()
```

对于Thread类，它的定义如下：

```
threading.Thread(self, group=None, target=None, name=None,
     args=(), kwargs=None, *, daemon=None)
```

- 参数group是预留的，用于将来扩展；
- 参数target是一个可调用对象，在线程启动后执行；
- 参数name是线程的名字。默认值为“Thread-N“，N是一个数字。
- 参数args和kwargs分别表示调用target时的参数列表和关键字参数。

Thread类定义了以下常用方法与属性：


| 方法与属性                 | 说明                                                                                                                                                                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start()                    | 启动线程，等待CPU调度                                                                                                                                                                                                                                             |
| run()                      | 线程被cpu调度后自动执行的方法                                                                                                                                                                                                                                     |
| getName()、setName()和name | 用于获取和设置线程的名称。                                                                                                                                                                                                                                        |
| setDaemon()                | 设置为后台线程或前台线程（默认是False，前台线程）。如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止。如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程执行完成后，程序才停止。 |
| ident                      | 获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。                                                                                                                                                           |
| is_alive()                 | 判断线程是否是激活的（alive）。从调用start()方法启动线程，到run()方法执行完毕或遇到未处理异常而中断这段时间内，线程是激活的。                                                                                                                                     |
| isDaemon()方法和daemon属性 | 是否为守护线程                                                                                                                                                                                                                                                    |
| join([timeout])            | 调用该方法将会使主调线程堵塞，直到被调用线程运行结束或超时。参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。                                                                                                     |

在多线程执行过程中，有一个特点要注意，那就是每个线程各执行各的任务，不等待其它的线程，自顾自的完成自己的任务，比如下面的例子：

```
import time
import threading

def doWaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))

t = threading.Thread(target=doWaiting)
t.start()
# 确保线程t已经启动
time.sleep(1)
print('start job')
print('end job')
```

执行结果是：

```
start waiting: 10:50:35
start job
end job
stop waiting 10:50:38
```

Python默认会等待最后一个线程执行完毕后才退出。上面例子中，主线程没有等待子线程t执行完毕，而是啥都不管，继续往下执行它自己的代码，执行完毕后也没有结束整个程序，而是等待子线程t执行完毕，整个程序才结束。

有时候我们希望主线程等等子线程，不要“埋头往前跑”。那要怎么办？使用join()方法！如下所示：

```
import time
import threading

def doWaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting', time.strftime('%H:%M:%S'))

t = threading.Thread(target=doWaiting)
t.start()
# 确保线程t已经启动
time.sleep(1)
print('start join')
# 将一直堵塞，直到t运行结束。
t.join()
print('end join')
```

执行结果：

```
start waiting: 10:54:03
start join
stop waiting 10:54:06
end join
```

我们还可以使用`setDaemon(True)`把所有的子线程都变成主线程的守护线程，当主线程结束后，守护子线程也会随之结束，整个程序也跟着退出。

```
import threading
import time

def run():
    print(threading.current_thread().getName(), "开始工作")
    time.sleep(2)       # 子线程停2s
    print("子线程工作完毕")

for i in range(3):
    t = threading.Thread(target=run,)
    t.setDaemon(True)   # 把子线程设置为守护线程，必须在start()之前设置
    t.start()

time.sleep(1)     # 主线程停1秒
print("主线程结束了！")
print(threading.active_count())  # 输出活跃的线程数
```

执行结果：

```
Thread-1 开始工作
Thread-2 开始工作
Thread-3 开始工作
主线程结束了！
4
```

## 2. 自定义线程类

对于threading模块中的Thread类，本质上是执行了它的run方法。因此可以自定义线程类，让它继承Thread类，然后重写run方法。

```
import threading

class MyThreading(threading.Thread):

    def __init__(self, func, arg):
        super(MyThreading,self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)

def my_func(args):
    """
    你可以把任何你想让线程做的事定义在这里
    """
    pass

obj = MyThreading(my_func, 123)
obj.start()
```

## 3.线程锁

由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。线程锁用于锁定资源，可以同时使用多个锁，当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。

我们先看一下没有锁的情况下，脏数据是如何产生的。

```
import threading
import time

number = 0

def plus():
    global number       # global声明此处的number是外面的全局变量number
    for _ in range(1000000):    # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))

for i in range(2):      # 用2个子线程，就可以观察到脏数据
    t = threading.Thread(target=plus)
    t.start()


time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
print("主线程执行完毕后，number = ", number)
```

执行结果（每次数值可能都不一样）：

```
子线程Thread-2运算结束后，number = 1144974
子线程Thread-1运算结束后，number = 1181608
主线程执行完毕后，number =  1181608
```

结果并不等于2,000,000，可以很明显地看出脏数据的情况。这是因为两个线程在运行过程中，CPU随机调度，你算一会我算一会，在没有对number进行保护的情况下，就发生了数据错误。如果想获得正确结果，可以使用join()方法，让多线程变成顺序执行，如下修改代码片段：

```
for i in range(2):   
    t = threading.Thread(target=plus)
    t.start()
    t.join()        # 添加这一行就让两个子线程变成了顺序执行
```

上面为了防止脏数据而使用join()的方法，其实是让多线程变成了单线程，属于因噎废食的做法，正确的做法是使用线程锁。Python在threading模块中定义了几种线程锁类，分别是：

- Lock 互斥锁
- RLock 可重入锁
- Semaphore 信号
- Event 事件
- Condition 条件
- Barrier “阻碍”

### 3.1 互斥锁Lock

互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。使用很简单，初始化锁对象，然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。

```
import threading
import time

number = 0
lock = threading.Lock()

def plus(lk):
    global number       # global声明此处的number是外面的全局变量number
    lk.acquire()        # 开始加锁
    for _ in range(1000000):    # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
    lk.release()        # 释放锁，让别的线程也可以访问number

if __name__ == '__main__':
    for i in range(2):      # 用2个子线程，就可以观察到脏数据
        t = threading.Thread(target=plus, args=(lock,)) # 需要把锁当做参数传递给plus函数
        t.start()
    time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
    print("主线程执行完毕后，number = ", number)
```

RLock的使用方法和Lock一模一样，只不过它支持重入锁。该锁对象内部维护着一个Lock和一个counter对象。counter对象记录了acquire的次数，使得资源可以被多次require。最后，当所有RLock被release后，其他线程才能获取资源。在同一个线程中，`RLock.acquire()`可以被多次调用，利用该特性，可以解决部分死锁问题。

### 3.2 信号Semaphore

类名：BoundedSemaphore。这种锁允许一定数量的线程同时更改数据，它不是互斥锁。比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队。

```
import time
import threading

def run(n, se):
    se.acquire()
    print("run the thread: %s" % n)
    time.sleep(1)
    se.release()

# 设置允许5个线程同时运行
semaphore = threading.BoundedSemaphore(5)
for i in range(20):
    t = threading.Thread(target=run, args=(i,semaphore))
    t.start()
```

运行后，可以看到5个一批的线程被放行。

### 3.3 事件Event

类名：Event

事件线程锁的运行机制：全局定义了一个Flag，如果Flag的值为False，那么当程序执行wait()方法时就会阻塞，如果Flag值为True，线程不再阻塞。这种锁，类似交通红绿灯（默认是红灯），它属于在红灯的时候一次性阻挡所有线程，在绿灯的时候，**一次性放行所有**排队中的线程。

事件主要提供了四个方法set()、wait()、clear()和is_set()。

调用clear()方法会将事件的Flag设置为False。

调用set()方法会将Flag设置为True。

调用wait()方法将等待“红绿灯”信号。

is_set():判断当前是否"绿灯放行"状态

下面是一个模拟红绿灯，然后汽车通行的例子：

```
#利用Event类模拟红绿灯
import threading
import time

event = threading.Event()

def lighter():
    green_time = 5       # 绿灯时间
    red_time = 5         # 红灯时间
    event.set()          # 初始设为绿灯
    while True:
        print("\33[32;0m 绿灯亮...\033[0m")
        time.sleep(green_time)
        event.clear()
        print("\33[31;0m 红灯亮...\033[0m")
        time.sleep(red_time)
        event.set()

def run(name):
    while True:
        if event.is_set():      # 判断当前是否"放行"状态
            print("一辆[%s] 呼啸开过..." % name)
            time.sleep(1)
        else:
            print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
            event.wait()
            print("[%s] 看到绿灯亮了，瞬间飞起....." % name)

if __name__ == '__main__':

    light = threading.Thread(target=lighter,)
    light.start()

    for name in ['奔驰', '宝马', '奥迪']:
        car = threading.Thread(target=run, args=(name,))
        car.start()
```

运行结果：

```
绿灯亮...
一辆[奔驰] 呼啸开过...
一辆[宝马] 呼啸开过...
一辆[奥迪] 呼啸开过...
一辆[奥迪] 呼啸开过...
......
 红灯亮...
一辆[宝马]开来，看到红灯，无奈的停下了...
一辆[奥迪]开来，看到红灯，无奈的停下了...
一辆[奔驰]开来，看到红灯，无奈的停下了...
绿灯亮...
[奥迪] 看到绿灯亮了，瞬间飞起.....
一辆[奥迪] 呼啸开过...
[奔驰] 看到绿灯亮了，瞬间飞起.....
一辆[奔驰] 呼啸开过...
[宝马] 看到绿灯亮了，瞬间飞起.....
一辆[宝马] 呼啸开过...
一辆[奥迪] 呼啸开过...
......
```

### 3.3 条件Condition

类名：Condition

Condition称作条件锁，依然是通过acquire()/release()加锁解锁。

wait([timeout])方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。

notify()方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池），其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

notifyAll()方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

下面的例子，有助于你理解Condition的使用方法：

```
import threading
import time

num = 0
con = threading.Condition()

class Foo(threading.Thread):

    def __init__(self, name, action):
        super(Foo, self).__init__()
        self.name = name
        self.action = action

    def run(self):
        global num
        con.acquire()
        print("%s开始执行..." % self.name)
        while True:
            if self.action == "add":
                num += 1
            elif self.action == 'reduce':
                num -= 1
            else:
                exit(1)
            print("num当前为：", num)
            time.sleep(1)
            if num == 5 or num == 0:
                print("暂停执行%s！" % self.name)
                con.notify()
                con.wait()
                print("%s开始执行..." % self.name)
        con.release()

if __name__ == '__main__':
    a = Foo("线程A", 'add')
    b = Foo("线程B", 'reduce')
    a.start()
    b.start()
```

如果不强制停止，程序会一直执行下去，并循环下面的结果：

```
线程A开始执行...
num当前为： 1
num当前为： 2
num当前为： 3
num当前为： 4
num当前为： 5
暂停执行线程A！
线程B开始执行...
num当前为： 4
num当前为： 3
num当前为： 2
num当前为： 1
num当前为： 0
暂停执行线程B！
线程A开始执行...
num当前为： 1
num当前为： 2
num当前为： 3
num当前为： 4
num当前为： 5
暂停执行线程A！
线程B开始执行...
```

## 4. 定时器Timer

定时器Timer类是threading模块中的一个小工具，用于指定n秒后执行某操作。一个简单但很实用的东西。

```
from threading import Timer

def hello():
    print("hello, world")

# 表示1秒后执行hello函数
t = Timer(1, hello)
t.start()
```

## 5. 通过with语句使用线程锁

所有的线程锁都有一个加锁和释放锁的动作，非常类似文件的打开和关闭。在加锁后，如果线程执行过程中出现异常或者错误，没有正常的释放锁，那么其他的线程会造到致命性的影响。通过with上下文管理器，可以确保锁被正常释放。其格式如下：

```
with some_lock:
    # 执行任务...
```

这相当于：

```
some_lock.acquire()
try:
    # 执行任务..
finally:
    some_lock.release()
```

## 6. 全局解释器锁（GIL）

既然介绍了多线程和线程锁，那就不得不提及Python的GIL问题。

在大多数环境中，单核CPU情况下，本质上某一时刻只能有一个线程被执行，多核CPU时则 可以支持多个线程同时执行。但是在Python中，无论CPU有多少核，同时只能执行一个线程。这是由于GIL的存在导致的。

GIL的全称是`Global Interpreter Lock`(全局解释器锁)，是Python设计之初为了数据安全所做的决定。Python中的某个线程想要执行，必须先拿到GIL。可以把GIL看作是执行任务的“通行证”，并且在一个Python进程中，GIL只有一个。拿不到通行证的线程，就不允许进入CPU执行。GIL只在CPython解释器中才有，因为CPython调用的是c语言的原生线程，不能直接操作cpu，只能利用GIL保证同一时间只能有一个线程拿到数据。在PyPy和JPython中没有GIL。

**Python多线程的工作流程：**

1. 拿到公共数据
2. 申请GIL
3. Python解释器调用操作系统原生线程
4. cpu执行运算
5. 当该线程执行一段时间消耗完，无论任务是否已经执行完毕，都会释放GIL
6. 下一个被CPU调度的线程重复上面的过程

**Python针对不同类型的任务，多线程执行效率是不同的：**

对于CPU密集型任务(各种循环处理、计算等等)，由于计算工作多，ticks计数很快就会达到阈值，然后触发GIL的释放与再竞争（多个线程来回切换是需要消耗资源的），所以Python下的多线程对CPU密集型任务并不友好。

IO密集型任务(文件处理、网络通信等涉及数据读写的操作)，多线程能够有效提升效率(单线程下有IO操作会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率)。所以Python的多线程对IO密集型任务比较友好。

**为什么不能去掉GIL？**

首先，在早期的Python解释器依赖较多的全局状态，传承下来，使得想要移除当今的GIL变得更加困难。其次，对于程序员而言，仅仅是理解GIL的实现就需要对操作系统设计、多线程编程、C语言、解释器设计和CPython解释器的实现有着非常彻底的理解，更不用说对它进行修改删除了。总之，整体技术难度大，会对当前内部框架产生根本性的影响，牵一发而动全身。

在1999年，针对Python1.5，一个叫做“freethreading”的补丁已经尝试移除GIL，用细粒度的锁来代替。然而，GIL的移除给单线程程序的执行速度带来了一定的负面影响。当用单线程执行时，速度大约降低了40%。虽然使用两个线程时在速度上得到了提高，但这个提高并没有随着核数的增加而线性增长。因此这个补丁没有被采纳。

虽然，在Python的不同解释器实现中，如PyPy就移除了GIL，其执行速度更快（不单单是去除GIL的原因）。但是，我们通常使用的CPython解释器版本占有着统治地位的使用量，所以，你懂的。

**在实际使用中的建议：**

Python中想要充分利用多核CPU，就用多进程。因为每个进程有各自独立的GIL，互不干扰，这样就可以真正意义上的并行执行。在Python中，多进程的执行效率优于多线程(仅仅针对多核CPU而言)。同时建议在IO密集型任务中使用多线程，在计算密集型任务中使用多进程。另外，深入研究Python的协程机制，你会有惊喜的。

更多的详细介绍和说明请参考下面的文献： 英文原版：[Python's Hardest Problem](https://jeffknupp.com/blog/2012/03/31/pythons-hardest-problem/) 中文翻译：[Python 最难的问题](http://www.oschina.net/translate/pythons-hardest-problem)
