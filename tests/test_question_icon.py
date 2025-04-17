from marina.components import auth_page, question_icon


def test_tab1_hints_visibility_with_pagination(driver):
    """
    Тест-кейс №1.
    Проверка отображения подсказок и пагинации после нажатия иконки вопроса на вкладке 'Картина дня'.
    Предусловие:
        - Отсутствие пагинации допускается.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке не выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Проверить, что вкладка "Картина дня" активная. - Текущая вкладка отображается, как активная и ее название
        "Картина дня".
    3. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    4. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    5. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Проверка названия активной вкладки."""
    tab_name = question_icon.check_active_tab_name(driver)
    assert tab_name == "Картина дня", "Название вкладки не соответствует 'Картина дня'."

    """3. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """4. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """5. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab2_hints_visibility_with_pagination(driver):
    """
    Тест-кейс №2.
    Проверка отображения подсказок и пагинации после нажатия иконки вопроса на вкладке 'Отчет'.
    Предусловие:
        - Отсутствие пагинации допускается.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке не выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Нажать вкладку 'Отчет'. - Активная вкладка - 'Отчет', ожидаемый подраздел 'Аудитории' загрузился.
    3. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    4. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
        наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
        наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
        подсказки отображаются на каждом элементе.
    5. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Нажать вкладку 'Отчет', проверить, что она активна и ожидаемый подраздел в ней загрузился."""
    tab_name = question_icon.check_active_tab_after_click(driver, "Отчет")
    assert tab_name == "Отчет", "Название вкладки не соответствует 'Отчет'."

    """3. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """4. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """5. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab3_hints_visibility_with_pagination(driver):
    """
    Тест-кейс №3.
    Проверка отображения подсказок и пагинации после нажатия иконки вопроса на вкладке 'Настройки'.
    Предусловие:
        - Отсутствие пагинации допускается.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке не выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Нажать вкладку 'Настройки'. - Активная вкладка - 'Настройки', ожидаемый подраздел 'Аудитории' загрузился.
    3. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    4. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
        наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
        наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии
        пагинации подсказки отображаются на каждом элементе.
    5. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Нажать вкладку 'Настройки' и проверить, что она активна и ожидаемый подраздел в ней загрузился."""
    tab_name = question_icon.check_active_tab_after_click(driver, "Настройки")
    assert tab_name == "Настройки", "Название вкладки не соответствует 'Настройки'."

    """3. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """4. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """5. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab1_sub_tabs_hints_visibility_without_pagination(driver):
    """
    Тест-кейс №4.
    Проверка отображения подсказок после нажатия иконки вопроса на каждом подразделе вкладки 'Картина дня'.
    Предусловие:
        - Наличие пагинации и ее элементы не рассматриваются.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Проверка активного статуса вкладки "Картина дня". - Активная вкладка "Картина дня".
    3. Проверить, что первый подраздел активный. - Активный подраздел 1-й.
    4. Кликнуть иконку вопроса. - - Появляется режим просмотра подсказок.
    5. Проверка отображения подсказок в зависимости от наличия контента. - Подсказки отображаются при наличии контента
        и не отображаются при его отсутствии.
    6. Выйти из режима просмотра подсказок, кликнув ESC. - Режим просмотра подсказок дезактивируется.
    7. Кликнуть на второй подраздел и проверить, что он стал активный. - Активный подраздел 2-й.
    8. Кликнуть иконку вопроса. - - Появляется режим просмотра подсказок.
    9. Проверка отображения подсказок в зависимости от наличия контента. - Подсказки отображаются при наличии контента
        и не отображаются при его отсутствии.
    10. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Проверка названия активной вкладки."""
    active_tab_name = question_icon.check_active_tab_name(driver)
    assert active_tab_name == "Картина дня", "Название вкладки не соответствует 'Картина дня'."

    """3. Находим первый подраздел и проверяем активен ли он. """
    question_icon.check_sub_tab_without_name(driver, 1)

    """4. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """5. Находим второй подраздел, если он не активен, кликаем его и проверяем активность снова. """
    question_icon.check_sub_tab_without_name(driver, 2)

    """6. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab2_sub_tabs_hints_visibility_without_pagination(driver):
    """
    Тест-кейс №5.
    Проверка отображения подсказок после нажатия иконки вопроса на каждом подразделе вкладки 'Отчет'.
    Предусловие:
        - Наличие пагинации и ее элементы не рассматриваются.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Перейти на вкладку "Отчет". - Активная вкладка - "Отчет", ожидаемый подраздел 'Аудитории' загрузился.
    3. Проверить, что отображается первый подраздел "Аудитории" и кликнуть иконку вопроса. - Активный подраздел -
        "Аудитории", отображаются подсказки при наличии контента.
    4. Выйти из режима просмотра подсказок, кликнув ESC или в "пустом" месте страницы. - Режим просмотра подсказок
        дезактивирован.
    5. Кликнуть на второй подраздел "Сюжеты" и проверить, что он отображается. - Активный подраздел - "Сюжеты".
    6. Кликнуть иконку вопроса. - Отображаются подсказки при наличии контента.
    7. Выйти из режима просмотра подсказок, кликнув ESC или в "пустом" месте страницы. - Режим просмотра подсказок
        дезактивирован.
    8. Кликнуть на третий подраздел "Индикаторы" и проверить, что он отображается. - Активный подраздел - "Индикаторы".
    9. Кликнуть иконку вопроса. - Отображаются подсказки при наличии контента.
    10. Выйти из режима просмотра подсказок, кликнув ESC или в "пустом" месте страницы. - Режим просмотра подсказок
        дезактивирован.
    """
    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Нажать вкладку 'Отчет' и проверить, что она активна и загрузился ожидаемый подраздел 'Аудитории'."""
    active_tab_name = question_icon.check_active_tab_after_click(driver, "Отчет")
    assert active_tab_name == "Отчет", "Название вкладки не соответствует 'Отчет'."

    """3. Находим подраздел "Аудитории" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Аудитории")
    assert name == "Аудитории", "Подраздел 'Аудитории' не активен."

    """4. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """5. Находим подраздел подраздел "Сюжеты" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Сюжеты")
    assert name == "Сюжеты", "Подраздел 'Сюжеты' не активен."

    """6. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """7. Находим подраздел подраздел "Индикаторы" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Индикаторы")
    assert name == "Индикаторы", "Подраздел 'Индикаторы' не активен."

    """8. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab3_sub_tabs_hints_visibility_without_pagination(driver):
    """
    Тест-кейс №6.
    Проверка отображения подсказок после нажатия иконки вопроса на каждом подразделе вкладки 'Настройки'.
    Предусловие:
        - Наличие пагинации и ее элементы не рассматриваются.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Перейти на вкладку "Настройки". - Активная вкладка - "Настройки", ожидаемый подраздел 'Аудитории' загрузился.
    3. Проверить, что отображается первый подраздел "Тематики" и кликнуть иконку вопроса. - Активный подраздел -
        "Тематики", отображаются подсказки при наличии контента.
    4. Выйти из режима просмотра подсказок, кликнув ESC или в "пустом" месте страницы. - Режим просмотра подсказок
        дезактивирован.
    5. Кликнуть на второй подраздел "Каналы" и проверить, что он отображается. - Активный подраздел - "Каналы".
    6. Кликнуть иконку вопроса. - Отображаются подсказки при наличии контента.
    7. Выйти из режима просмотра подсказок, кликнув ESC или в "пустом" месте страницы. - Режим просмотра подсказок
        дезактивирован.
    8. Кликнуть на третий подраздел "Аудитории" и проверить, что он отображается. - Активный подраздел - "Аудитории".
    9. Кликнуть иконку вопроса. - Отображаются подсказки при наличии контента.
    10. Выйти из режима просмотра подсказок, кликнув ESC или в "пустом" месте страницы. - Режим просмотра подсказок
        дезактивирован.
    """
    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Нажать вкладку 'Настройки' и проверить, что она активна и загрузился ожидаемый подраздел 'Аудитории'."""
    active_tab_name = question_icon.check_active_tab_after_click(driver, "Настройки")
    assert active_tab_name == "Настройки", "Название вкладки не соответствует 'Настройки'."

    """3. Находим подраздел подраздел "Тематики" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Тематики")
    assert name == "Тематики", "Подраздел 'Тематики' не активен."

    """4. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """5. Находим подраздел подраздел "Каналы" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Каналы")
    assert name == "Каналы", "Подраздел 'Каналы' не активен."

    """6. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """7. Находим подраздел подраздел "Аудитории" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Аудитории")
    assert name == "Аудитории", "Подраздел 'Аудитории' не активен."

    """8. Клик по иконке вопроса, проверка отображения подсказок при наличии контента и выход из режима подсказок."""
    hint_mode_invisibility = question_icon.check_hints_without_pagination(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab1_sub_tabs_hints_visibility_with_pagination(driver):
    """
    Тест-кейс №7.
    Проверка отображения подсказок после нажатия иконки вопроса в каждом подразделе вкладки 'Картина дня' с учетом
    пагинации.
    Предусловие:
        - Отсутствие пагинации допускается.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Проверить, что вкладка "Картина дня" активная. - Текущая вкладка отображается, как активная и ее название
        "Картина дня".
    3. Проверить, что первый подраздел активный. - Активный подраздел 1-й.
    4. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    5. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    6. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    7. Проверить, что второй подраздел активный. - Активный подраздел 2-й.
    8. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    9. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    10. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Проверка названия активной вкладки."""
    tab_name = question_icon.check_active_tab_name(driver)
    assert tab_name == "Картина дня", "Название вкладки не соответствует 'Картина дня'."

    """3. Находим первый подраздел и проверяем активен ли он. """
    question_icon.check_sub_tab_without_name(driver, 1)

    """4. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """5. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """6. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """7. Находим второй подраздел, если он не активен, кликаем его и проверяем активность снова. """
    question_icon.check_sub_tab_without_name(driver, 2)

    """8. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """9. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """10. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab2_sub_tabs_hints_visibility_with_pagination(driver):
    """
    Тест-кейс №8.
    Проверка отображения подсказок после нажатия иконки вопроса в каждом подразделе вкладки 'Отчет' с учетом пагинации.
    Предусловие:
        - Отсутствие пагинации допускается.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Перейти на вкладку "Отчет". - Активная вкладка - "Отчет", ожидаемый подраздел 'Аудитории' загрузился.
    3. Проверить, что отображается первый подраздел "Аудитории" - Активный подраздел - "Аудитории".
    4. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    5. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    6. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    7. Кликнуть на второй подраздел "Сюжеты" и проверить, что он отображается. - Активный подраздел - "Сюжеты".
    8. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    9. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    10. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    11. Кликнуть на третий подраздел "Индикаторы" и проверить, что он отображается. - Активный подраздел - "Индикаторы".
    12. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    13. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    14. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Нажать вкладку 'Отчет' и проверить, что она активна и загрузился ожидаемый подраздел 'Аудитории'."""
    active_tab_name = question_icon.check_active_tab_after_click(driver, "Отчет")
    assert active_tab_name == "Отчет", "Название вкладки не соответствует 'Отчет'."

    """3. Находим подраздел "Аудитории" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Аудитории")
    assert name == "Аудитории", "Подраздел 'Аудитории' не активен."

    """4. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """5. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """6. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """7. Находим подраздел подраздел "Сюжеты" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Сюжеты")
    assert name == "Сюжеты", "Подраздел 'Сюжеты' не активен."

    """8. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """9. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """10. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """11. Находим подраздел подраздел "Индикаторы" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Индикаторы")
    assert name == "Индикаторы", "Подраздел 'Индикаторы' не активен."

    """12. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """13. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """14. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."


def test_tab3_sub_tabs_hints_visibility_with_pagination(driver):
    """
    Тест-кейс №9.
    Проверка отображения подсказок после нажатия иконки вопроса в каждом подразделе вкладки 'Настройки' с учетом пагинации.
    Предусловие:
        - Отсутствие пагинации допускается.
        - Отсутствие подсказок допускается при отсутствии контента, помеченного атрибутом "data-onboarding".
        - Переключение подразделов на вкладке выполняется пользователем.
    1. Авторизоваться на сайте https://assist24.tech/app данными:
        login = "tatarstan@gmail.com"
        password = "string" - Отображается вкладка "Картина дня".
    2. Перейти на вкладку "Настройки". - Активная вкладка - "Настройки", ожидаемый подраздел 'Аудитории' загрузился.
    3. Проверить, что отображается первый подраздел "Тематики". - Активный подраздел - "Тематики".
    4. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    5. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    6. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    7. Кликнуть на второй подраздел "Каналы" и проверить, что он отображается. - Активный подраздел - "Каналы".
    8. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    9. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    10. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    11. Кликнуть на третий подраздел "Аудитории" и проверить, что он отображается. - Активный подраздел - "Аудитории".
    12. Клик по иконке вопроса. - Появляется режим просмотра подсказок.
    13. Проверка отображения подсказок в зависимости от наличия контента и независимо от наличия пагинации. В случае
      наличия пагинации проверяется отображение подсказок на каждом элементе пагинации. - Подсказки отображаются при
      наличии контента и не отображаются при его отсутствии, пагинация может отображаться либо нет. При наличии пагинации
      подсказки отображаются на каждом элементе.
    14. Выход из режима просмотра подсказок. - Режим просмотра подсказок дезактивируется.
    """

    """1. Выполнить авторизацию"""
    auth_page.execute_authorization(driver)

    """2. Нажать вкладку 'Настройки' и проверить, что она активна и загрузился ожидаемый подраздел 'Аудитории'."""
    active_tab_name = question_icon.check_active_tab_after_click(driver, "Настройки")
    assert active_tab_name == "Настройки", "Название вкладки не соответствует 'Настройки'."

    """3. Находим подраздел подраздел "Тематики" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Тематики")
    assert name == "Тематики", "Подраздел 'Тематики' не активен."

    """4. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """5. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """6. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """7. Находим подраздел подраздел "Каналы" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Каналы")
    assert name == "Каналы", "Подраздел 'Каналы' не активен."

    """8. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """9. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """10. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."

    """11. Находим подраздел подраздел "Аудитории" и проверяем активен ли он. """
    name = question_icon.check_sub_tab_with_name(driver, "Аудитории")
    assert name == "Аудитории", "Подраздел 'Аудитории' не активен."

    """12. Проверка кликабельности иконки вопроса и появление режима просмотра подсказок."""
    question_icon.check_click_question_icon(driver)

    """13. Проверяем отображение подсказок при наличии контента на каждом элементе пагинации."""
    question_icon.check_hints_with_and_without_pagination(driver)

    """14. Выходим из режима подсказок и проверяем, что данный режим не активен."""
    hint_mode_invisibility = question_icon.exit_hints_mode(driver)
    assert hint_mode_invisibility is True, "Режим подсказок активен."
