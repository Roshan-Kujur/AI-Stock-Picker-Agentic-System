from crewai.tools import tool
import os
import requests



@tool("Send Push Notification")
def send_push_notification(message: str) -> str:
    """
    Use this tool to send a push notification to the user.
    Args:
        message: The message to be sent as a push notification to the user.
    Returns:
        A string indicating the status of the push notification.
    """
    topic = "scout-rnk-58_alerts"
    ntfy_url = f"https://ntfy.sh/{topic}"

    selection = requests.post(
            ntfy_url,
            data=message.encode("utf-8"),
            headers={
                "Title": "The Stk",
                "Priority": "default",
            },
            timeout=15,
        )
    selection.raise_for_status()
    return f"Push notification sent with API response code: {selection}"


# @tool("Send Push Notification")
# def send_push_notification(message: str) -> str:
#     """
#     Use this tool to send a push notification to the user.
#     Args:
#         message: The message to be sent as a push notification to the user.
#     Returns:
#         A string indicating the status of the push notification.
#     """
#     pushover_user_key = os.getenv("PUSHOVER_USER_KEY")
#     pushover_token_key = os.getenv("PUSHOVER_TOKEN_KEY")
#     pushover_url = "https://api.pushover.net/1/messages.json"
#     payload = {"user": pushover_user_key, "token": pushover_token_key, "message": message}
#     result = requests.post(pushover_url, data=payload).status_code
#     return f"Push notification sent with API response code: {result}"