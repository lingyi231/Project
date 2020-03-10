# --coding:utf-8--
from socket import *
from select import select

s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(3)

# 设置非阻塞
s.setblocking(False)

rlist = [s]
wlist = []
xlist = []
while True:
    print("等待处理IO")
    # select本身是一个阻塞函数
    # 如果读写列表都监控了同一个事件,　读事件就绪的话　写方法列表会为空
    # 监听列表中有人就绪,select就会返回
    # 读是被动,写是主动
    #提交给操作系统关注
    rs, ws, xs = select(rlist, wlist, xlist)
    print(rs)
    # 遍历返回值列表,看看哪个IO就绪
    for r in rs:
        # 分类 s或者c
        if r is s:
            # 一次性做不完　设置非阻塞　看看其他IO
            c, addr = r.accept()
            print("Connect from ", addr)
            c.setblocking(False)
            rlist.append(c)
        else:
            # 希望所有的IO操作都在很短的时间内完成
            # 如果r遍历到客户端链接套接字说明:有客户端给我发消息
            # 除了s就是c
            # 客户端发送的消息大于1024,c还是就绪　继续接收剩下的

            # 由于网络原因　发送方发送了不到1024个字节
            # 先收一部分
            data = r.recv(1024)
            if not data:
                # data为空 说明对方断开链接
                rlist.remove(r)
                r.close()
                # 跳过当前循环进行下次循环
                continue
            print(data.decode())
            r.send(b"ok")
            # wlist.append(r)
    for w in ws:
        # 很多时候不会用wlist
        # 增加了一次外层大循环
        # w.send(b"OK")
        # wlist.remove(w)
        pass
    for x in ws:
        pass
