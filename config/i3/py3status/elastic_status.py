# -*- coding: utf-8 -*-
"""
This module will display Elasticsearch Cluster status
"""
import os

import elasticsearch


class Py3status:

    template = 'Elasticsearch: {use_ssl} {status}    {number_of_nodes}'
    url = None
    use_ssl = True
    ca_certs = None
    ssl_assert_hostname = False
    username = None
    password = None

    def elastic_status(self):
        self.es = elasticsearch.Elasticsearch(
            self.url,
            use_ssl=self.use_ssl,
            http_auth=(self.username, self.password),
            ca_certs=self.ca_certs,
            ssl_assert_hostname=self.ssl_assert_hostname
        )
        try:
            health = self.es.cluster.health()
        except Exception:
            status = '💔'
            health['number_of_nodes'] = "n/a"

        if health['status'] == 'green':
            status = '💚'
        elif health['status'] == 'yellow':
            status = '💛'
        else:
            status = '💔'

        if self.use_ssl:
            use_ssl = "🔒"
        else:
            use_ssl = "🔓"
        full_text = self.template.format(
                use_ssl=use_ssl,
                status=status,
                number_of_nodes=health["number_of_nodes"],
            )
        return {
            'full_text': full_text,
            'cached_until': self.py3.time_in(1)
        }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
