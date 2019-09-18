# Linux下永久更换镜像源

**需要修改~/ .pip/pip.conf**

- cd~

- mkdir pip

- cd pip

- vi pip.conf

- 在pip.conf中，添加配置内容

  - i 进入插入状态

  ```python
  [global]
  timeout = 6000
  index-url = http://pypi.douban.com/simple
  trusted-host = pypi.douban.com
  ```

  - 保存退出
    - Esc
    - shift + :
    - wq                  

**然后就修改完毕了！**

