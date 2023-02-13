HEALTH_SERVICES_LIST = [
    {
        "Node": {
            "ID": "40e4a748-2192-161a-0510-9bf59fe950b5",
            "Node": "foobar",
            "Address": "10.1.10.12",
            "Datacenter": "dc1",
            "TaggedAddresses": {
                "lan": "10.1.10.12",
                "wan": "10.1.10.12"
            },
            "Meta": {
                "instance_type": "t2.medium"
            }
        },
        "Service": {
            "ID": "redis",
            "Service": "redis",
            "Tags": ["primary"],
            "Address": "10.1.10.12",
            "TaggedAddresses": {
                "lan": {
                    "address": "10.1.10.12",
                    "port": 8000
                },
                "wan": {
                    "address": "198.18.1.2",
                    "port": 80
                }
            },
            "Meta": {
                "redis_version": "4.0"
            },
            "Port": 8000,
            "Weights": {
                "Passing": 10,
                "Warning": 1
            },
            "Namespace": "default"
        },
        "Checks": [
            {
                "Node": "foobar",
                "CheckID": "service:redis",
                "Name": "Service 'redis' check",
                "Status": "passing",
                "Notes": "",
                "Output": "",
                "ServiceID": "redis",
                "ServiceName": "redis",
                "ServiceTags": ["primary"],
                "Namespace": "default"
            },
            {
                "Node": "foobar",
                "CheckID": "serfHealth",
                "Name": "Serf Health Status",
                "Status": "passing",
                "Notes": "",
                "Output": "",
                "ServiceID": "",
                "ServiceName": "",
                "ServiceTags": [],
                "Namespace": "default"
            }
        ]
    }
]

LAN_WAN_IPV4_TAGGED_ATTRIBUTES = [
    {
        "Node": {
            "ID": "40e4a748-2192-161a-0510-9bf59fe950b5",
            "Node": "foobar",
            "Address": "10.1.10.12",
            "Datacenter": "dc1",
            "TaggedAddresses": {
                "lan_ipv4": "10.1.10.12",
                "lan": "10.1.10.12",
                "wan": "10.1.10.12",
                "wan_ipv4": "10.1.10.12"
            },
            "Meta": {
                "instance_type": "t2.medium"
            }
        },
        "Service": {
            "ID": "redis",
            "Service": "redis",
            "Tags": ["primary"],
            "Address": "10.1.10.12",
            "TaggedAddresses": {
                "lan": {
                    "address": "10.1.10.12",
                    "port": 8000
                },
                "wan": {
                    "address": "198.18.1.2",
                    "port": 80
                }
            },
            "Meta": {
                "redis_version": "4.0"
            },
            "Port": 8000,
            "Weights": {
                "Passing": 10,
                "Warning": 1
            },
            "Namespace": "default"
        },
        "Checks": [
            {
                "Node": "foobar",
                "CheckID": "service:redis",
                "Name": "Service 'redis' check",
                "Status": "passing",
                "Notes": "",
                "Output": "",
                "ServiceID": "redis",
                "ServiceName": "redis",
                "ServiceTags": ["primary"],
                "Namespace": "default"
            },
            {
                "Node": "foobar",
                "CheckID": "serfHealth",
                "Name": "Serf Health Status",
                "Status": "passing",
                "Notes": "",
                "Output": "",
                "ServiceID": "",
                "ServiceName": "",
                "ServiceTags": [],
                "Namespace": "default"
            }
        ]
    }
]

SERVICE_LIST_NOMAD = [
    {
        "Node": {
            "ID": "40e4a748-2192-161a-0510-9bf59fe950b5",
            "Node": "foobar",
            "Address": "10.1.10.12",
            "Datacenter": "dc1",
            "TaggedAddresses": {
                "lan": "10.1.10.12",
                "wan": "10.1.10.12"
            },
            "Meta": {
                "instance_type": "t2.medium"
            }
        },
        "Service": {
            "ID": '_nomad-task-86c6736f-33d2-e3b1-69a2-8189031eb599-service-01',
            "Service": "redis",
            "Tags": ["primary"],
            "Address": "10.1.10.12",
            "TaggedAddresses": {
                "lan": {
                    "address": "10.1.10.12",
                    "port": 8000
                },
                "wan": {
                    "address": "198.18.1.2",
                    "port": 80
                }
            },
            "Meta": {
                "redis_version": "4.0"
            },
            "Port": 8000,
            "Weights": {
                "Passing": 10,
                "Warning": 1
            },
            "Namespace": "default"
        },
        "Checks": [
            {
                "Node": "foobar",
                "CheckID": "service:redis",
                "Name": "Service 'redis' check",
                "Status": "passing",
                "Notes": "",
                "Output": "",
                "ServiceID": "redis",
                "ServiceName": "redis",
                "ServiceTags": ["primary"],
                "Namespace": "default"
            },
            {
                "Node": "foobar",
                "CheckID": "serfHealth",
                "Name": "Serf Health Status",
                "Status": "passing",
                "Notes": "",
                "Output": "",
                "ServiceID": "",
                "ServiceName": "",
                "ServiceTags": [],
                "Namespace": "default"
            }
        ]
    }
]
