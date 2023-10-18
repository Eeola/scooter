import configuration
import requests
import data


def get_order_by_track(track):
    headers = data.headers.copy()
    params = {"t": track}

    return requests.get(
        configuration.URL_SERVICE + configuration.TRACK_ORDER_PATH,
        params=params,
        headers=headers
    )


def post_order(body):
    headers = data.headers.copy()

    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=headers
    )
