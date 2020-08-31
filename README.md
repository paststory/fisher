
## 鱼书是什么?
鱼书是一款满足书友互相捐赠获取书籍的平台，在这里会有大量的书籍，把自己读过的好作品与人分享，也可以看看他人的优质藏书

## 鱼书有哪些功能？
* 核心功能：查看全部图书有哪些，可以将喜欢的书籍添加到心愿清单里，向有意愿捐赠书籍的人请求书籍，同时把自己读过的不错的书籍，添加到礼物清单，供需要的人选择，形成一个良好的读书平台。
* 登录注册：新人通过注册成为鱼书用户，获得和其他用户一样的权利。忘记密码时可通过邮箱找重置密码。
* 赠送清单：将允许的书籍捐赠到平台。
* 心愿清单：选择需要的书籍，向所有者请求书籍。
* 鱼漂：查看曾今完成过的交易（捐赠，获取）
* 最近上传：可以看到自己愿意捐赠的书籍

## 如何启动？
* 首先要安装虚拟环境，需要用到pipenv

```python
pipenv install 安装虚拟环境(Pipfile.lock Pipfile 要存在)
pipenv shell 进入虚拟环境
启动 python fish.py
```
* 配置数据库，在secure.py文件中，这个根据个人数据库的配置来
* 邮箱配置，我这里使用的是腾讯qq邮箱，现在邮箱在第三方平台不能直接用密码，需要使用授权码，这个需要注意。

