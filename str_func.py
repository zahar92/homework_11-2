def str_to_upper(string):
    """
    Возвращает строку изменяя регистр заглавными буквами
    :param string:
    :return string:
    """
    if isinstance(string, str):
        return string.upper()
    else:
        return 'Функция принимает только строки'

    
def str_to_title(string):
    """
    Возвращает строку, делая первую букву каждого слова заглавной
    :param string:
    :return string:
    """
    if isinstance(string, str):
        return string.title()
    else:
        return 'Функция принимает только строки'
