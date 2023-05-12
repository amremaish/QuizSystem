FIREBASE_INFO = {
    'driver': {
        'new_order': {
            'title': 'QuizSystem',
            'body': 'you have received a new order with order number {order_number}'
        }
    },
    'restaurant': {
        'order_driver_status': {
            'title': 'QuizSystem',
            'body': 'The driver changed the order status with number {order_number}'
        }
    }
}
FIREBASE_DRIVER_INFO = FIREBASE_INFO.get('driver')
FIREBASE_REST_INFO = FIREBASE_INFO.get('restaurant')

# print(FIREBASE_DRIVER_INFO.get('new_order').get('body').format(order_number='12'))
