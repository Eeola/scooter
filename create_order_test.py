# Юлия Пилецкая, 9-я когорта - Финальный проект. Инженер по тестрованию плюс
import sender_stand_request
import data


def positive_assert():
    body = data.order_body.copy()

    order_response = sender_stand_request.post_order(body)
    track = order_response.json()["track"]
    response = sender_stand_request.get_order_by_track(track)

    assert response.status_code == 200


# checklist 1 -  successful order creation
def test_create_and_get_order_by_track():
    positive_assert()

