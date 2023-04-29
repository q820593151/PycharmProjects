import  unittest
import unittestreport
suite = unittest.defaultTestLoader.discover(r'./')
runner = unittestreport.TestRunner(suite,
                                   tester="盘景文",
                                   filename="test.html",
                                   report_dir="report",
                                   templates=2,
                                   title="测试",
                                   desc="描述"
                                   )
runner.run()