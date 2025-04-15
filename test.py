from common.waits import wait_present


def test_one(driver_init):
    wait_present(driver_init, 'XPATH', "//span[text()='Вход']", "Страница авторизации не открыта")

