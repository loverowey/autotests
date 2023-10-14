import sender_stand_request
import data

def get_track_order():
    order_response = sender_stand_request.post_new_order(data.body_order)
    order_track = order_response.json()["track"]
    return order_track
def get_params_order():
    current_params = data.parameters_order.copy()
    current_params["t"] = get_track_order()
    return current_params
def get_order_info():
    param = get_params_order()
    order_info_response = sender_stand_request.get_order_info(param)
    assert order_info_response.status_code == 200

def test_get_order_info():
    get_order_info()