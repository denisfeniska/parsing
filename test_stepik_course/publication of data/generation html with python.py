from yattag import Doc

doc, tag, text = Doc().tagtext()


with tag('html'):
    with tag('body'):
        # with tag('p', id='main'):
        #     text('some text')
        # with tag('a', href='/my-url'):
        #     text('some link')
        with tag('table'):
            with tag('tr'):
                with tag('td'):
                    text(matr[i][j])

result = doc.getvalue()
print(result)