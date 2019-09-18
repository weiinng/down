# 安装Docker

- 安装  DockerToolbox-18.01.0-ce.exe 

- 运行  Docker Quickstart Terminal

  1. 报错，出现浏览不到文件：
     - 打开 快捷方式属性
     - 修改目标 "C:\Program Files\Git\bin\bash.exe" --login -i "C:\Program Files\Docker Toolbox\start.sh"
     - 原因是你的Git目录对不上，自己找到自己的Git对上就可以了！
     - 祝你愉快！

  2. 跳过上面的问题直接运行 Docker

     - 按照老师一路next的步骤的话！

     - 路径在这里：

       C:\Program Files\Docker Toolbox    --> 运行 start.sh

     - 如果网速好的话
     
       等一会就会出现小鲸鱼
     
  3. 网速不好：
  
     运行 start.sh 会在 用户文件内生成一个 .docker 文件
  
   `C:\Users\Administrator\.docker\machine\cache`
  
   进入  打开别人下载好的  
  
   复制 `boot2docker.ios`文件，复制到自己的 cache 里面。
  
   然后从新执行第二步
  
- 利用搬运工封装redis的服务，并且可以用蟒服务，为搭建redis的集群做准备

- 在docker内生成redis服务。

  1. 检索的Redis

     ```
     docker search redis
     ```

  2. 拉取官方的镜像，（这个示例中，官方镜像也是明星最多的）

     ```
     docker pull redis
     ```

  3. 查看镜像列表

     ```
     docker images
     ```

  4. 启动镜像

     这里宿主使用6380，是因为6379端口已经被占用

     ```
     docker run -p 6380:6379 -d redis:latest redis-server
     ```

  5. 查看容器运行状态

     ```
     docker ps
     ```



