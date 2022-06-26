<<<<<<< HEAD
from numpy import matrix
=======
>>>>>>> 9cbf7ab3053d3f31937fc254294a0f456cbca17e
from yattag import Doc

doc, tag, text = Doc().tagtext()

<<<<<<< HEAD
matrix = [[y*x for y in range(1, 11)] for x in range(1, 11)]
=======
>>>>>>> 9cbf7ab3053d3f31937fc254294a0f456cbca17e

with tag('html'):
    with tag('body'):
        # with tag('p', id='main'):
        #     text('some text')
        # with tag('a', href='/my-url'):
        #     text('some link')
        with tag('table'):
<<<<<<< HEAD
            for i in range(10):
                with tag('tr'):
                    for j in range(10):
                        with tag('td'):
                            text(matrix[i][j])

result = doc.getvalue()
print(result)
=======
            with tag('tr'):
                with tag('td'):
                    text(matr[i][j])

result = doc.getvalue()
print(result)
>>>>>>> 9cbf7ab3053d3f31937fc254294a0f456cbca17e
