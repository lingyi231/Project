# --coding:utf-8--
"""
tcp客户端练习
"""
# 先运行服务端　再运行客户端


from socket import *

# 服务器地址
server_addr = ("127.0.0.1", 8888)
# 直接写socket方法
# 创建tcp套接字
sockfd = socket()  # 默认值就是tcp套接字
# 连接服务器
sockfd.connect(server_addr)
while True:
    # 发送接收消息
    data = input(">>")
    sockfd.send(data.encode())
    if not data:
        sockfd.send("文件发送完毕".encode())
        break
    # 输入##表示退出
    # if data == "##":
    #     break
    # 必须是字节串
    data = sockfd.recv(1024)
    print("From server:", data.decode())

sockfd.close()
