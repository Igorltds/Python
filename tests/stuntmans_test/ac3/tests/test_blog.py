#from sys import path
#path.insert(1, '/home/home/luaa/projects/python/tests/stuntman_test/ac3')

from unittest.mock import Mock
from pytest import fixture, raises

from src.blog import Blog

class ExceptionNotFound(Exception): pass

@fixture
def posts_list():
    posts_list =[{'userId': 1, 'Id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'}
                ,{'userId': 2, 'Id': 2, 'title': 'Titulo teste 2', 'body': 'Teste de conteudo do blog 2'}]
    return posts_list


# Test blog post_by_user_id
def test_blog_posts_0(posts_list):
    blog = Mock() # Mock
    blog.posts.return_value=posts_list
    
    assert blog.posts()[0]['userId'] == 1
    assert blog.posts()[0]['Id'] == 1
    assert blog.posts()[0]['title'] == 'Titulo teste 1'
    assert blog.posts()[0]['body'] == 'Conteudo do blog 1'

def test_blog_posts_1(posts_list):
    blog = Mock() # Mock
    blog.posts.return_value=posts_list
    
    assert blog.posts()[1]['userId'] == 2
    assert blog.posts()[1]['Id'] == 2
    assert blog.posts()[1]['title'] == 'Titulo teste 2'
    assert blog.posts()[1]['body'] == 'Teste de conteudo do blog 2'


# Test post_by_user_id
def test_post_by_user_id_0(posts_list):
    blog = Mock() # Mock
    blog.post_by_user_id.return_value='0'
    assert blog.post_by_user_id() == '0'
    
def test_post_by_user_id_0_not_found(posts_list):
    blog = Mock() # Mock
    with raises(ExceptionNotFound):
        blog.post_by_user_id.side_effect=ExceptionNotFound
        blog.post_by_user_id()


def test_post_by_user_id_1(posts_list):
    blog = Mock() # Mock
    blog.post_by_user_id.return_value='1'
    assert blog.post_by_user_id() == '1'
    
def test_post_by_user_id_1_not_found(posts_list):
    blog = Mock() # Mock
    with raises(ExceptionNotFound):
        blog.post_by_user_id.side_effect=ExceptionNotFound
        blog.post_by_user_id()