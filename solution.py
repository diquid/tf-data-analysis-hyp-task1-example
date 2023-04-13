from statsmodels.stats.proportion import proportions_ztest

chat_id = 1234206085


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    alpha = 0.1
    _, p_val = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative="smaller")
    x = x_success/x_cnt
    y = y_success/y_cnt
    if (alpha > p_val) and (x < y):
        return True
    return False
