import  unittest
import unittestreport
import time
import  os
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
suite = unittest.defaultTestLoader.discover(r'./')
runner = unittestreport.TestRunner(suite,
                                   tester="盘景文",
                                   filename= f"test_report_{current_time}.html",
                                   report_dir="report",
                                   templates=1,
                                   title="测试",
                                   desc="浏览器打开测试"
                                   )
runner.run()