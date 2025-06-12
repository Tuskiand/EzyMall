# -*- coding: utf-8 -*-
import time
import pytest
from common.readyaml import ReadYamlData
from base.removefile import remove_file
from common.dingRobot import send_dd_msg
from conf.setting import dd_msg
import warnings

yfd = ReadYamlData()

@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    # 禁用HTTPS告警，ResourceWarning
    warnings.simplefilter('ignore', ResourceWarning)
    yfd.clear_yaml_data()
    remove_file("./report/temp", ['json', 'txt', 'attach', 'properties'])

def generate_test_summary(terminalreporter):
    """生成测试结果摘要字符串"""
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    
    # 使用更可靠的方式获取测试时长
    start_time = terminalreporter._sessionstarttime if hasattr(terminalreporter, '_sessionstarttime') \
        else getattr(terminalreporter, '_session_start', time.time())
    
    # 处理不同版本的pytest时间格式
    if hasattr(start_time, 'timestamp'):
        start_time = start_time.timestamp()
    elif not isinstance(start_time, float):
        start_time = time.time()
    
    duration = time.time() - start_time

    summary = f"""
    自动化测试结果，通知如下，请着重关注测试失败的接口，具体执行结果如下：
    测试用例总数：{total}
    测试通过数：{passed}
    测试失败数：{failed}
    错误数量：{error}
    跳过执行数量：{skipped}
    执行总时长：{duration:.2f}秒
    """
    print(summary)
    return summary

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """自动收集pytest框架执行的测试结果并打印摘要信息"""
    summary = generate_test_summary(terminalreporter)
    if dd_msg:
        send_dd_msg(summary)