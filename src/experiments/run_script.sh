# Nepal to AWS India
python ./experiments/test.py local --schemes "aurora iml indigo pcc bbr" --uplink-trace /home/eric/Dev/DRL-IL/pantheon/third_party/indigo/env/0.57mbps-poisson.trace --downlink-trace /home/eric/Dev/DRL-IL/pantheon/third_party/indigo/env/0.57mbps-poisson.trace --prepend-mm-cmds "mm-delay 28 mm-loss uplink 0.0477" --extra-mm-link-args "--uplink-queue=droptail --uplink-queue-args=packets=14" --run-time 3

# Bottleneck buffer = BDP
python ./experiments/test.py local --schemes "aurora iml indigo pcc bbr" --uplink-trace /home/eric/Dev/DRL-IL/pantheon/third_party/indigo/env/12mbps.trace --downlink-trace /home/eric/Dev/DRL-IL/pantheon/third_party/indigo/env/12mbps.trace --prepend-mm-cmds "mm-delay 30" --extra-mm-link-args "--uplink-queue=droptail --uplink-queue-args=bytes=90000" --run-time 3


python ./experiments/test.py local --schemes "aurora indigo pcc" --prepend-mm-cmds "mm-delay 30" --extra-mm-link-args "--uplink-queue=droptail --uplink-queue-args=bytes=90000" --run-time 3

