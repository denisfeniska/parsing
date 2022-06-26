from numpy import matrix
from yattag import Doc

doc, tag, text = Doc().tagtext()

matrix = [[y*x for y in range(1, 11)] for x in range(1, 11)]

with tag('html'):
    with tag('body'):
        # with tag('p', id='main'):
        #     text('some text')
        # with tag('a', href='/my-url'):
        #     text('some link')
        with tag('table'):
            for i in range(10):
                with tag('tr'):
                    for j in range(10):
                        with tag('td'):
                            with tag('a', href=f'http://{matrix[i][j]}.ru'):
                                text(matrix[i][j])

result = doc.getvalue()
print(result)
