#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context


def main():
    args = arg_parser.receiver_first()

    cc_repo = '/home/eric/Dev/DRL-IL/PCC-Uspace/'
    send_src = path.join(cc_repo, 'src/app/', 'pccclient')
    recv_src = path.join(cc_repo, 'src/app/', 'pccserver')

    if args.option == 'setup':
        return

    if args.option == 'sender':
        # cmd = [send_src, 'send', args.ip, args.port]
        # cmd = [send_src, 'send', args.ip, args.port, 
        # '--pcc-rate-control=python', '-pyhelper=loaded_client', 
        # '-pypath=/home/eric/Dev/DRL-IL/PCC-RL/src/udt-plugins/testing', 
        # '--history-len=10', '--pcc-utility-calc=linear', '--log-utility-calc-lite', 
        # '--model-path=/home/eric/Data/drl-il/icml-data/icml_paper_model']
        # check_call(cmd, env={'LD_LIBRARY_PATH': '/home/eric/Dev/DRL-IL/PCC-Uspace/src/core/'})
        cmd = [send_src, 'send', args.ip, args.port, 
        '--pcc-rate-control=python', '-pyhelper=shim', 
        '-pypath=/home/eric/Dev/DRL-IL/PCC-RL/src/udt-plugins/training/', 
        '--history-len=10', '--pcc-utility-calc=linear', '--log-utility-calc-lite']
        check_call(cmd, env={'LD_LIBRARY_PATH': '/home/eric/Dev/DRL-IL/PCC-Uspace/src/core/'})
        return

    if args.option == 'receiver':
        cmd = [recv_src, 'recv', args.port]
        check_call(cmd, env={'LD_LIBRARY_PATH': '/home/eric/Dev/DRL-IL/PCC-Uspace/src/core/'})
        return


if __name__ == '__main__':
    main()
