#!/usr/bin/env python3

from hc_pyconsul import ConsulCatalog

if __name__ == '__main__':

    consul_catalog = ConsulCatalog()

    for service_name, service_tags in consul_catalog.list_services().items():
        print(f'\nService: {service_name} has the following tags:\n')

        for tag_item in service_tags:
            print(f'\t- {tag_item}')
