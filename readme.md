# 接口自动化测试框架

基于 Python + pytest + allure 的接口自动化测试框架

## 项目结构

```
pythonproject/
├── base/           # 基础类
├── common/         # 公共方法
├── conf/          # 配置文件
├── data/          # 测试数据
├── report/        # 测试报告
├── testcase/      # 测试用例
├── conftest.py    # pytest配置文件
├── environment.xml # 测试环境配置
├── run.py         # 运行入口
└── requirements.txt # 项目依赖
```

## 环境准备

1. Python 3.7+
2. 安装依赖包
```bash
pip install -i https://pypi.doubanio.com/simple -r requirements.txt
```

## 快速开始

1. 配置测试环境信息
- 修改 `conf/setting.py` 中的环境配置
- 配置 `environment.xml` 以自定义测试报告环境信息

2. 编写测试用例
```yaml
baseInfo:
  api_name: 接口名称
  url: /api/path
  method: post
  header:
    Content-Type: application/json
    token: ${get_extract_data(token)}
  
testCase:
  - title: 测试用例标题
    request:
      json:
        key: value
    extract:
      token: $.data.token
    validate:
      - eq: [status_code, 200]
      - contains: [$.message, "success"]
```

3. 运行测试
```bash
python run.py
```

## 测试报告

支持两种测试报告格式：
- Allure Report
- TMReport

可在 `conf/setting.py` 中设置 `REPORT_TYPE` 选择报告类型：
```python
REPORT_TYPE = 'allure'  # 或 'tm'
```

## 关键特性

1. 接口请求支持类型
- GET：params 参数
- POST：
  - form-data：data 参数
  - json：json 参数
  - files：文件上传

2. 数据提取与关联
- 支持提取响应数据用于后续接口
- 使用 `${get_extract_data(key)}` 语法引用

3. 断言支持
- 状态码断言
- 响应内容断言
- JSON响应断言

4. 钉钉通知
- 支持测试结果推送到钉钉群
- 在 `conf/setting.py` 中配置 `dd_msg` 开启/关闭通知

## 注意事项

1. Content-Type 对应关系：
- form-data: `application/x-www-form-urlencoded`
- json: `application/json`
- files: `multipart/form-data`

2. 运行环境建议：
- 推荐使用本地 Python 环境
- 也可使用项目虚拟环境，但需注意版本兼容性

## 维护说明

1. 测试用例管理
- 遵循 pytest 用例编写规范
- 用例文件必须以 `test_` 开头
- 测试类必须以 `Test` 开头
- 测试方法必须以 `test_` 开头

2. 配置文件说明
- `conf/setting.py`: 框架配置
- `environment.xml`: 报告环境配置
- `conftest.py`: pytest 钩子函数配置

## 常见问题

1. 运行报错检查项：
- Python 版本是否符合要求
- 依赖包是否完整安装
- 配置文件是否正确

2. 测试报告问题：
- Allure 是否正确安装
- 报告目录权限是否正确

## 技术支持

如有问题请提交 Issue 或联系相关开发人员。