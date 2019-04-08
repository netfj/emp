from os import path
from tempfile import gettempdir

a = path.join(gettempdir(), '_doc2docx')

print(a)

