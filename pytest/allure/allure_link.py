import allure

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='点击我看一看youtube吧')
def test_with_named_link():
    pass


@allure.issue('140', 'bug issue链接')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, '测试用例地址')
def test_with_testcase_link():
    pass