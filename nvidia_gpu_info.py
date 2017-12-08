import subprocess
import sys

cmd_gpu_uuid = 'nvidia-smi --query-gpu="gpu_uuid" --format=csv,noheader,nounits'
gpu_list = []


# Pull current GPU temperature
def get_gpu_temp(gpu):
    cmd = 'nvidia-smi --query-gpu="temperature.gpu" --format=csv,noheader,nounits --id={}'.format(gpu)
    rv = subprocess.check_output(cmd, shell=True).decode('utf-8').rstrip()
    return rv


# Pull current fan speed percentage
def get_gpu_fan_speed(gpu):
    cmd = 'nvidia-smi --query-gpu="fan.speed" --format=csv,noheader,nounits --id={}'.format(gpu)
    rv = subprocess.check_output(cmd, shell=True).decode('utf-8').rstrip()
    return rv


def main():
    gpu_uuid = subprocess.check_output(cmd_gpu_uuid, shell=True).decode('utf-8')
    gpu_uuid_list = gpu_uuid.split('\n')

    for gpu in gpu_uuid_list:
        if 'GPU-' in gpu:
            print('Current Temp: ', get_gpu_temp(gpu))
            print('Current Fan Speed: ', get_gpu_fan_speed(gpu))

if __name__ == '__main__':
    main()
