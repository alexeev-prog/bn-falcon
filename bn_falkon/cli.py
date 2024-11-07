import os
import click
from bn_falkon.utils.customization import LineLoader
from bn_falkon.utils.file_handler import FileHandler


@click.group()
def cli():
	"""BlazingNet Falcon - Network Security Toolkit"""
	pass


@cli.group()
def scan():
	"""Commands related to scanning"""
	pass


@cli.command()
def run_html():
	results = {
		0: {
			'title': 'Example 1',
			'rows': ['IP', 'MAC', 'HOSTNAME', "CVE"],
			'columns': ['121.232.34.11', '00:00:00:00:00', 'server@linux', "CVE-2023-03-02.223-HTML"]
		},
		1: {
			'title': 'Example 2',
			'rows': ['IP', 'MAC', 'HOSTNAME', "CVE"],
			'columns': ['121.232.34.11', '00:00:00:00:00', 'server@linux', "CVE-2023-03-02.223-HTML"]
		}
	}
	FileHandler.generate_report('127.0.0.1', results, 'report.html')
