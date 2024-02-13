import threading
from time import sleep

import alerter
import timer
import config_parser


def start_alert_scheduler(alert: config_parser.Alert):
    print('starting alert scheduler')
    print(alert)
    a = alerter.Alerter(alert.title, alert.message, alert.duration)
    threading.Thread(target=timer.trigger_function_every_x_seconds, args=(alert.interval, a.open_message_box_with_countdown,)).start()


if __name__ == '__main__':
    alerts = config_parser.read_alerts_from_yaml('./config.yaml')
    for alert in alerts:
        start_alert_scheduler(alert)
    print('Started all alert schedulers. Have a nice workday :)')
    sleep(60 * 60 * 9)  # sleep for the entire workday
    print('Work day finished! Closing program.')
