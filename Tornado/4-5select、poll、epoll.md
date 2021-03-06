# select、poll、epoll

select，poll，epoll 都是IO多路复用的机制，I/O多路复用就是通过一种机制，一个进程可以监视多个描述符，一旦某个描述符就绪（一般是度就绪或者写就绪），能够通知程序进行相应的读写操作。但select，poll，epoll本质上都是同步I/O，因为他们都需要在读写事件就绪后自己负责进行读写，也就是说这个读写过程是阻塞的，而异步I/O则无需自己负责进行读写，异步I/O的实现负责吧数据和内核拷贝到用户空间。



# select

select函数监视的文件描述符分三类，分别是writefds（可写文件描述符），readfds（可读文件描述符）和exceptfds（异常文件描述符）。调用select函数会阻塞，直到有描述符就绪（有数据可读、可写、或者有except），或者超时（timeout指定等待时间，如果立即返回设为null即可），函数返回。当select函数返回后，可以通过遍历fdset，来找到就绪的描述符。

select目前几乎再所有平台上都支持，其良好跨平台支持也是他的一个优点，select的一个缺点在于单个进程能够监视的文件描述符的数量存在最大限制，在linux上一般为1024，可以通过修改宏定义甚至重新编译内核的方式提升这一限制，但是这样也会造成效率的降低。

# poll

poll是针对select的一个改进，不同于select使用三个位图来表示三个fdset的方式，pill使用一个pillfd的指针实现。

polldf结构包含了要监视的event和发生的event，不再使用select “参数-值” 传递的方式。同时，pollfd并没有最大数量的限制（但是数量过大后性能也会下降）。和select函数一样，poll返回后，需要轮询pollfd来获取就绪的描述符。

从上面看，select和poll都需要在返回后，通过遍历文件描述符来获取已经就绪的socket。事实上，同时连接的大量客户端在一时刻可能只有很少的处于就绪状态，因此随着监视的描述符数量和增长，其效率也会线性下降。

# epoll

epoll是在2.6内核中提出的，是之前的select和poll的增强版本。相对于select和poll来说，epoll更加灵活，没有描述符限制。epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的一个时间表中，这样在用户空间和内核空间的copy只需一次。

epoll使用的是红黑树的数据类型，效率非常高。epoll使用一个描述符管理多个描述符。