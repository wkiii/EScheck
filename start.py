import fire
import psutil
import subprocess
from kubernetes import client, config, watch

class Check():
    def cpu(self):
        cpu_count = psutil.cpu_count(logical=True)
        cpu_percent = psutil.cpu_percent(percpu=True)
        print(f"cpu_count: {cpu_count}")
        print(f"cpu_percent: {cpu_percent}")

    def mem(self):
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        print(f"memory_percent: {mem_percent}")

    def disk(self):
        disk = psutil.disk_usage('/')
        print(disk)

    def net(self):
        net = psutil.net_if_stats()

    def service_check(self):
        service_list = ['etcd','kubelet','docker']
        for service in service_list:
            _service = subprocess.run(f"systemctl status {service}", stdout=subprocess.PIPE, shell=True)
            service_status = str(_service.stdout,'utf-8')
            print(f"{service}'s status is f{service_status}")

    def base(self, *args, **kwargs):
        ret = subprocess.run("pwd", stdout=subprocess.PIPE, shell=True)
        ret_str = str(ret.stdout, 'utf-8')
        self.cpu()
        self.mem()
        self.disk()
        self.net()


    def nova(self, uuid, node):
        print(f"uuid: {uuid} , node: node-{node}")




if __name__ == '__main__':
    fire.Fire(Check)
