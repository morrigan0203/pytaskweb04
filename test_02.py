from testpage import OperationsHelper
from addpost import OperationsAddPost
from contactpage import OperationsContactUsHelper
import logging
import yaml


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()

    test_page.enter_username("test")
    test_page.enter_pass("test")
    test_page.click_login_btn()
    msg = test_page.get_msg()
    assert "401" == msg


def test_step2(browser):
    logging.info("Test2 starting")
    test_page = OperationsHelper(browser)
    username = testdata["username"]
    test_page.enter_username(username)
    test_page.enter_pass(testdata["password"])
    test_page.click_login_btn()
    auth_msg = test_page.get_auth_text()
    assert f'Hello, {username}' == auth_msg


def test_step3(browser):
    logging.info("Test3 starting")
    add_post = OperationsAddPost(browser)
    add_post.add_post()
    title = "Title3"
    add_post.post_content(title=title, descr="Description3", content="Content3")
    title_new = add_post.find_post()
    assert title == title_new


def test_step4(browser):
    logging.info("Test4 starting")
    add_post = OperationsAddPost(browser)
    add_post.go_to_site()
    add_post.add_post()
    title = "Title4"
    add_post.post_content(title=title, descr="Description4")
    title_new = add_post.find_post()
    assert title == title_new


def test_step5(browser):
    logging.info("Test5 starting")
    add_post = OperationsAddPost(browser)
    add_post.go_to_site()
    add_post.add_post()
    title = "Title5"
    add_post.post_content(title=title, content="Content5")
    title_new = add_post.find_post()
    assert title == title_new


def test_step6(browser):
    logging.info("Test6 starting")
    add_post = OperationsAddPost(browser)
    add_post.go_to_site()
    add_post.add_post()
    title = "Title6"
    add_post.post_content(title=title)
    title_new = add_post.find_post()
    assert title == title_new


def test_step_7(browser):
    logging.info("Test7 starting")
    contact = OperationsContactUsHelper(browser)
    contact.open_contact_us_page()
    contact.fill_contact_us(your_name="Name7", your_email="name7@email.com", content="Content7")
    assert "Form successfully submitted" == contact.get_alert_msg(3)


def test_step_8(browser):
    logging.info("Test8 starting")
    contact = OperationsContactUsHelper(browser)
    contact.open_contact_us_page()
    contact.fill_contact_us(your_name="Name8", your_email="name8@email.com")
    assert "Form successfully submitted" == contact.get_alert_msg(3)


def test_step_9(browser):
    logging.info("Test9 starting")
    contact = OperationsContactUsHelper(browser)
    contact.open_contact_us_page()
    contact.fill_contact_us(your_name="Name9", content="Content9")
    assert "Form successfully submitted" == contact.get_alert_msg(3)


def test_step_10(browser):
    logging.info("Test10 starting")
    contact = OperationsContactUsHelper(browser)
    contact.open_contact_us_page()
    contact.fill_contact_us(your_name="Name10")
    assert "Form successfully submitted" == contact.get_alert_msg(3)


def test_step_11(browser):
    logging.info("Test11 starting")
    contact = OperationsContactUsHelper(browser)
    contact.open_contact_us_page()
    contact.fill_contact_us(your_name="Name11", your_email="Email11")
    assert contact.check_alert_not_present(3)
    assert contact.check_email_label_red()

