# test_api.py
import requests
import sys

def test_httpbin():
    try:
        resp = requests.get('https://httpbin.org/get', timeout=5)
        assert resp.status_code == 200
        print('✅ 接口测试通过！状态码:', resp.status_code)
        return True
    except Exception as e:
        print('❌ 接口测试失败:', e)
        return False

if __name__ == "__main__":
    if test_httpbin():
        sys.exit(0)
    else:
        sys.exit(1)
