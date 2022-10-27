from unittest.mock import Mock
from pytest import fixture

from src.blog import Blog

@fixture
def posts():
    posts = [{
        'userId': 1,
        'Id': 1,
        'title': 'Titulo teste 1',
        'body': 'Conteudo do blog 1'
    }, {
        'userId': 2,
        'Id': 2,
        'title': 'Titulo teste 2',
        'body': 'Teste de conteudo do blog 2'
    }]
    return posts

def test_posts(posts):
    assert posts[0]["userId"] == 1