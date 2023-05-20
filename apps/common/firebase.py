import requests


class Firebase:
    FCM_API_URL = "https://fcm.googleapis.com/fcm/send"
    SPECIALIST_FCM_SERVER_KEY = "AAAAJMtNU7A:APA91bE0753d4GC6DuNsJwlyirOr-VVH68woQW5oLJK5mTmGOmUETKKCZvGq_0vgKJA6vBUuY3iLhI7gO-UJmolf2dOjas038wPLqCx0F4L7DtuBvPJcpOs2xU6o0YAb7zIV8E-IVo5k"

    @staticmethod
    def get_headers():
        return {
            'Authorization': f'key={Firebase.SPECIALIST_FCM_SERVER_KEY}',
            'content-type': 'application/json'
        }

    @staticmethod
    def send_notification_fcm(*, fcm_tokens, title: str, body: str, data: dict):
        for fcm_token in fcm_tokens:
            if not fcm_token:
                continue
            body = {
                "to": fcm_token.fcm_token,
                "notification": {
                    "title": title,
                    "body": body,
                    'click_action': 'FLUTTER_NOTIFICATION_CLICK',
                    "content_available": True,
                    "priority": "high"
                },
                'data': {
                    'click_action': 'FLUTTER_NOTIFICATION_CLICK',
                    "notification": data,
                    "content_available": True,
                    "priority": "high"
                }
            }
            requests.post(url=Firebase.FCM_API_URL, json=body, headers=Firebase.get_headers())
