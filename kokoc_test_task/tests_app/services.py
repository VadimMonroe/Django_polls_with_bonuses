from .models import UsersPoints


def get_test_results(request) -> tuple[int, str]:
    """Вытаскиваем результаты теста и сохраняем их в базе"""

    all_answers_list = [i for i in request.POST.values()]

    user_bonus = 0
    user_test = None
    user_inner = None

    for bonus in all_answers_list[1:]:
        bonus = bonus.split('|')
        user_bonus += int(bonus[0])
        if not user_test:
            user_test = bonus[1]
        if not user_inner:
            user_inner = bonus[2]

    user = UsersPoints.objects.get(login=user_inner)
    user.points += user_bonus

    if user.done_tests == '0':
        user.done_tests = user_test
    else:
        if user_test not in user.done_tests:
            user.done_tests += user_test
    user.save()
    return user_bonus, user_test


def save_buy_color_user_info(request, goods, users_points) -> None:
    """Сохраняем в базе купленный пользователем цвет"""

    purchased_color = request.POST.get('shop')
    tapped_good = goods.get(name=purchased_color)
    if users_points.color != purchased_color:
        if users_points.points - tapped_good.price >= 0:
            users_points.points = users_points.points - tapped_good.price
            users_points.color = purchased_color
    users_points.save()
