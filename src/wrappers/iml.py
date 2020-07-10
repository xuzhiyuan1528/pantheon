#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context


def main():
    args = arg_parser.sender_first()

    cc_repo = '/home/eric/Dev/DRL-IL/sim2real'
    send_src = path.join(cc_repo, 'run_sender.py')
    recv_src = path.join(cc_repo, 'run_receiver.py')

    if args.option == 'setup':
        return

    if args.option == 'sender':
        cmd = ['python3', send_src, args.port]
        check_call(cmd)
        return

    if args.option == 'receiver':
        cmd = ['python3', recv_src, args.ip, args.port]
        check_call(cmd)
        return


if __name__ == '__main__':
    main()
