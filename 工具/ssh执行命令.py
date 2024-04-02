# -*- coding: utf-8 -*-
__author__ = 'luointo'

import re
from io import StringIO

from paramiko.config import SSH_PORT
from paramiko.rsakey import RSAKey
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import AuthenticationException

ignore_reg = re.compile(
    r"Error: JAVA_HOME is not set and could not be found"
    r"|stty: standard input: Inappropriate ioctl for device"
    r"|tput: No value for \$TERM and no -T specified"
)


class SSH:
    def __init__(self, hostname, port=SSH_PORT, username='root', pkey=None, password=None, connect_timeout=10):
        if pkey is None and password is None:
            raise Exception('public key and password must have one is not None')
        self.client = None
        self.arguments = {
            'hostname': hostname,
            'port': port,
            'username': username,
            'password': password,
            'pkey': RSAKey.from_private_key(StringIO(pkey)) if isinstance(pkey, str) else pkey,
            'timeout': connect_timeout,
        }

    def exec_command(self, command, timeout=1800, environment=None):
        if self.arguments["username"] != 'root':
            command = "sudo " + command
        command = 'set -e\n' + command
        with self as cli:
            chan = cli.get_transport().open_session()
            chan.settimeout(timeout)
            chan.set_combine_stderr(True)
            if environment:
                str_env = ' '.join(f"{k}='{v}'" for k, v in environment.items())
                command = f'export {str_env} && {command}'
            command = f"source /etc/profile; {command}"
            chan.exec_command(command)
            out = chan.makefile("r", -1).read()
            if isinstance(out, bytes):
                out = out.decode("utf-8")

            # output filter some line match the ignore_regs
            out = "\n".join([line for line in out.split("\n") if not ignore_reg.search(line)])

            return chan.recv_exit_status(), out

    def __enter__(self):
        self.client = None
        return self.get_client()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
        self.client = None

    def get_client(self):
        if self.client is not None:
            return self.client
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy)
        self.client.connect(**self.arguments)
        return self.client


if __name__ == '__main__':
    ssh = SSH(hostname='192.168.134.194', port=22, username='root', password='tstack@123')
    command = 'kubectl get pods -n default'
    # command = 'kubectl exec -it mysql-0 -- mysql -ptstack_monitor -hproxysql-proxysql-cluste -A cloud -e "select * from performance_schema.replication_group_members;"'
    ret_code, ret_msg = ssh.exec_command(command)
    print(ret_code, ret_msg)
