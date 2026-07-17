# python-backend-foundation

## 项目定位

一个面向 AI 应用与通用 API 服务的 Python 后端基础项目。当前阶段聚焦于建立清晰、可测试、便于持续演进的 FastAPI 最小骨架，而不是提前引入尚未需要的基础设施。

## 当前已实现能力

- FastAPI 应用工厂与统一应用入口
- `/api/v1` 版本化路由组织
- 存活探针（liveness probe）
- 基于环境变量和 `.env` 文件的类型化配置
- 配置缓存及测试间的缓存隔离
- 健康检查与配置行为的自动化测试

## 技术栈

### 当前使用

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic Settings
- pytest 与 HTTPX
- Ruff（代码检查工具）
- uv（依赖管理与命令运行）

### 后续规划

以下能力属于后续路线，当前尚未实现：

- 数据库与持久化层
- Redis 与缓存能力
- Docker 容器化
- CI 自动化流程
- 更完整的可观测性、鉴权与业务模块示例

## 项目结构

```text
.
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── v1/
│       │       ├── __init__.py
│       │       ├── health.py
│       │       └── router.py
│       └── core/
│           ├── __init__.py
│           └── config.py
├── tests/
│   ├── conftest.py
│   ├── test_config.py
│   └── test_health.py
├── .env.example
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

## 本地启动

项目使用 `uv` 管理环境与依赖。安装好 `uv` 后，在项目根目录执行：

```bash
uv sync
uv run uvicorn app.main:app --reload
```

服务默认监听 `http://127.0.0.1:8000`。

- API 文档（Swagger UI）：<http://127.0.0.1:8000/docs>
- 存活检查：<http://127.0.0.1:8000/api/v1/health/live>

存活检查的当前响应为：

```json
{"status": "ok"}
```

## 配置

配置由 Pydantic Settings 读取，支持系统环境变量以及项目根目录中的 `.env` 文件。可以从示例开始创建本地配置：

```bash
cp .env.example .env
```

Windows PowerShell 可使用：

```powershell
Copy-Item .env.example .env
```

| 环境变量 | 默认值 | 说明 |
| --- | --- | --- |
| `APP_NAME` | `python-backend-foundation` | 应用名称，同时用于 OpenAPI 标题 |
| `APP_ENV` | `development` | 运行环境，可选 `development`、`test`、`production` |
| `APP_DEBUG` | `false` | 是否启用 FastAPI 调试模式 |
| `APP_API_V1_PREFIX` | `/api/v1` | v1 API 的统一路由前缀 |

修改配置后需要重启应用；配置对象在进程内会被缓存。

## 测试

```bash
uv run pytest
```

当前测试覆盖默认配置、环境变量覆盖、非法环境值校验，以及存活检查接口。

## 架构取舍与后续路线

- 使用 `src` 布局，避免从仓库根目录意外导入未安装的包，并让打包边界更明确。
- 通过 `create_app()` 集中创建 FastAPI 实例，为后续按环境注入中间件、生命周期资源和路由保留入口。
- 将配置放在 `core` 层并进行类型校验与缓存，减少散落的环境变量读取。
- 以 `/api/v1` 聚合版本化路由，便于未来扩展接口并保留兼容边界。
- 当前健康检查只表达 API 进程存活，不承诺数据库、缓存或其他外部依赖就绪。
- 后续将按实际业务需求逐步加入持久化、缓存、鉴权、可观测性、容器化与 CI，避免在基础阶段引入未被验证的复杂度。
