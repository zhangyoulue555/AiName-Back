from sqlalchemy import Integer,String,DateTime
from sqlalchemy.orm import mapped_column,Mapped
from . import Base
from pwdlib import PasswordHash
from datetime import datetime
# 初始化密码哈希生成器
password_hash = PasswordHash.recommended()

class User(Base):
    # 数据库中的表名
    __tablename__ = "user"
    # id: 主键，自增。Mapped[int] 告诉 Python 这是一个整数
    id : Mapped[ int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email : Mapped[ str] = mapped_column(String(100), unique=True)
    username : Mapped[ str] = mapped_column(String(100))
    # _password: 这是一个"私有"字段，用来存储"加密后的哈希值"，而不是明文密码
    _password : Mapped[ str] = mapped_column(String(200))

    # User类的初始化方法，初始化时，将密码进行加密
    def __init__(self, *args, **kwargs):
        # 尝试从参数中获取 'password'（明文密码）
        password = kwargs.get("password")
        # 如果存在 password，将其从 kwargs 中移除
        # 因为数据库表中没有 'password' 这一列，只有 '_password'
        if password:
            password = kwargs.pop("password")

        super().__init__(*args, **kwargs)
        self.password = password

    @property
    def password(self):
        # 当你尝试读取 user.password 时，返回内部存储的哈希值
        return self._password

    @password.setter
    def password(self, password):
        # 当你执行 user.password = "secret" 时，这个方法会自动运行
        # 1. 接收明文密码 "secret"
        # 2. 使用 password_hash.hash() 进行加密（加盐、哈希）
        # 3. 将加密后的乱码字符串赋值给数据库字段 self._password
        self._password = password_hash.hash(password)

    def check_password(self, raw_password):
        # 验证登录时的密码
        # raw_password: 用户输入的明文密码 (例如 "123456")
        # self.password: 实际上是调用了上面的 @property，获取数据库里的哈希值
        # .verify(): 对比 明文 和 哈希值 是否匹配
        return password_hash.verify(raw_password, self.password)

class EmailCode(Base):
    __tablename__ = 'email_code'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(10))
    create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)