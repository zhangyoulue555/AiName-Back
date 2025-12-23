# AIname - AI智能起名助手后端

AIname是一个基于FastAPI构建的AI智能起名助手后端服务，利用大语言模型为用户提供个性化的名字生成服务。

## 功能特性

- **用户认证系统**：邮箱注册、登录和JWT认证
- **AI名字生成**：基于用户提供的姓氏、性别、字数等要求生成个性化名字
- **邮件服务**：发送验证码和通知邮件
- **数据库集成**：使用SQLAlchemy和Alembic进行数据库管理

## 技术栈

- **后端框架**：FastAPI
- **数据库**：SQLAlchemy ORM + SQLite/MySQL
- **数据库迁移**：Alembic
- **邮件服务**：FastAPI-Mail
- **AI模型**：LangChain + DeepSeek
- **认证**：JWT Token
- **密码加密**：pwdlib

## 项目结构

```
AIname/
├── alembic/             # 数据库迁移文件
├── core/                # 核心功能模块
│   ├── agent.py         # AI名字生成核心逻辑
│   ├── auth.py          # 认证相关功能
│   └── mail.py          # 邮件配置
├── models/              # 数据库模型
│   └── user.py          # 用户和验证码模型
├── repository/          # 数据访问层
│   └── user_repo.py     # 用户和验证码操作
├── routers/             # API路由
│   ├── auth_router.py   # 认证相关路由
│   └── name_router.py   # 名字生成路由
├── schemas/             # 数据模型定义
│   ├── agent_schemas.py # AI相关Schema
│   ├── name_schemas.py  # 名字相关Schema
│   └── user_schemas.py  # 用户相关Schema
├── settings/            # 配置文件
├── dependencies.py      # 依赖注入
├── main.py              # 应用入口
├── alembic.ini          # Alembic配置
└── test_main.http       # HTTP测试文件
```

## 快速开始

### 环境要求

- Python 3.10+
- pip

### 安装步骤

1. **克隆项目**

```bash
git clone <repository-url>
cd AIname
```

2. **创建虚拟环境**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**

使用pip安装项目所需的依赖库。

4. **配置环境变量**

根据项目需求配置相关环境变量，如邮箱设置和API密钥等。

5. **数据库迁移**

```bash
# 生成迁移文件
alembic revision --autogenerate -m "Initial migration"

# 应用迁移
alembic upgrade head
```

6. **启动应用**

```bash
uvicorn main:app --reload
```

应用将在 `http://localhost:8000` 运行

## API文档

启动应用后，可以访问以下地址查看API文档：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 注意事项

1. 确保在生产环境中使用安全的密码和密钥
2. 定期备份数据库
3. 根据需要调整AI模型的参数
