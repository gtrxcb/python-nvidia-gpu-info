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


# Pull current memory total, used, free
def get_gpu_memory(gpu):
    cmd_mem_total = subprocess.check_output('nvidia-smi --query-gpu="memory.total" --format=csv,noheader,nounits --id={}'.format(gpu), shell=True).decode('utf-8').rstrip()
    cmd_mem_used = subprocess.check_output('nvidia-smi --query-gpu="memory.used" --format=csv,noheader,nounits --id={}'.format(gpu), shell=True).decode('utf-8').rstrip()
    cmd_mem_free = subprocess.check_output('nvidia-smi --query-gpu="memory.free" --format=csv,noheader,nounits --id={}'.format(gpu), shell=True).decode('utf-8').rstrip()
    total, used, free = (cmd_mem_total, cmd_mem_used, cmd_mem_free)
    return total, used, free


def main():
    gpu_uuid = subprocess.check_output(cmd_gpu_uuid, shell=True).decode('utf-8')
    gpu_uuid_list = gpu_uuid.split('\n')

    for gpu in gpu_uuid_list:
        if 'GPU-' in gpu:
            print('Current Temp: ', get_gpu_temp(gpu))
            print('Current Fan Speed: ', get_gpu_fan_speed(gpu))
            print('Current Memory: T:{} U:{} F:{}'.format(get_gpu_memory(gpu)[0], get_gpu_memory(gpu)[1], get_gpu_memory(gpu)[2]))

if __name__ == '__main__':
    main()
