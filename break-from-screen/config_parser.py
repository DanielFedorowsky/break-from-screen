from dataclasses import dataclass

import yaml


@dataclass
class Alert:
    interval: int
    duration: int
    title: str
    message: str


def read_alerts_from_yaml(file_path) -> list[Alert]:
    with open(file_path, 'r') as file:
        alerts_data = yaml.safe_load(file)
        alerts_list = alerts_data.get('alerts', [])
        alerts_instances = [Alert(**alert) for alert in alerts_list]
        return alerts_instances
