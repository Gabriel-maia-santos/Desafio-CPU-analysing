import psutil
from get_size import Get_size


def Disk():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        All = f"""
        {"="*40} "Informações do Disco", {"="*40}
        Hd utilizado: {partition.device}
        Endereço: {partition.mountpoint}
        Typo do systema do arquivo: {partition.fstype}
        """
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        All2 = f"""
        Tamanho Total: {Get_size(partition_usage.total)}
        Usando: {Get_size(partition_usage.used)}
        Espaço Livre: {Get_size(partition_usage.free)}"
        Porcentagem: {partition_usage.percent}%"
        """
    return All + All2
    
