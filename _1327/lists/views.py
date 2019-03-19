import paramiko

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def lists_index(request):
	if not request.user.is_superuser:
		raise PermissionDenied

	lists = []
	command_lists = '/usr/lib/mailman/bin/list_lists -b'
	command_members = '/usr/lib/mailman/bin/list_members'
	try:
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.WarningPolicy)
		client.connect(hostname = settings.LISTS_HOSTNAME, username=settings.LISTS_USERNAME, key_filename=settings.LISTS_KEY_FILENAME, password=settings.LISTS_KEY_PASSWORD)
		_stdin, stdout, stderr = client.exec_command(command_lists)
		lists = stdout.read().decode("utf-8").split('\n')
		lists = [l for l in lists if l]
		print(stderr.read())

		lists_with_members = {}
		for l in lists:
			_stdin, stdout, stderr = client.exec_command("{} {}".format(command_members, l))
			members = stdout.read().decode("utf-8").split('\n')
			members = [m for m in members if m]
			print(stderr.read())
			lists_with_members[l] = members
	finally:
		client.close()

	print(lists_with_members)

	return render(request, 'lists_index.html', {
		'lists_with_members': lists_with_members,
	})
