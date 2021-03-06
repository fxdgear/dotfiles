# -*- coding: utf-8 -*-
"""
This module will produce a ratio of running to all docker containers
"""
import docker
import subprocess
import sys


class Py3status:

    template = '[ 🐳 {version} ][  {running}/{total} ][  {images} ][  {managers}/{nodes} ]'

    def __init__(self):
        self.client = docker.from_env()

    def docker_status(self):
        containers = self._get_container()
        images = self._get_images()
        swarm = self._get_swarm()
        version = self._get_version()
        full_text = self.template.format(
                version=version,
                running=containers["running"],
                total=containers["total"],
                images=images["images"],
                managers=swarm.get("managers"),
                nodes=swarm.get("nodes")
            )
        return {
            'full_text': full_text,
            'cached_until': self.py3.time_in(1)
        }

    def _get_info(self):
        return self.client.info()


    def _get_container(self):
        info = self._get_info()
        total_containers = info['Containers']
        running_containers = info['ContainersRunning']
        return {"running": running_containers, "total": total_containers}


    def _get_version(self):
        info = self._get_info()
        return info['ServerVersion']


    def _get_images(self):
        info = self._get_info()
        return {"images": info["Images"]}


    def _get_swarm(self):
        info = self._get_info()
        try:
            if not bool(info["Swarm"]['Cluster']['ID']):
                return {}
        except KeyError:
            return {}
        return {"managers": info["Swarm"]["Managers"], "nodes": info["Swarm"]["Nodes"]}


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
