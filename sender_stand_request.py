import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.header_order)
def get_order_info(param):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
                        params=param)


