def test_blog_posts(posts):
    try:
        from blogm.views import posts as solution_posts
    except Exception as e:
        raise AssertionError(
            'При импорте списка `posts` из файла `blogm/views.py` '
            f'произошла ошибка: {e}') from e
    assert solution_posts == posts, (
        'Убедитесь, что список с постами `posts` из файла `blogm/views.py` '
        'соответствуют списку из задания.')
