import re
RE_EMAIL = re.compile(r'^([a-zA-Z0-9_-]+)@([a-zA-Z0-9]+\.[a-zA-Z0-9]+)$')


def email_parse(email):
    dict_parse = {}
    try:
        valid_email = RE_EMAIL.match(email)
        if valid_email is None:
            return ValueError(f'wrong email: {email}')
        else:
            dict_parse['username'] = valid_email[0]
            dict_parse['domain'] = valid_email[1]
            return dict_parse
    except Exception as e:
        print(f'global error: {e}')


if __name__ == '__main__':
    print(email_parse('someone@ya.com'))
    print(email_parse('1_3_5@rambler.ru'))
    print(email_parse('o-lga_123@mail1.ru'))
    print(email_parse('-123@mail.ru'))
    print(email_parse('olga-123@.ru'))
    print(email_parse('wrong/wrong.com'))

