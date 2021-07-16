import psutil
from get_size import Get_size


def Memory():
    svmem = psutil.virtual_memory()
    All = f"""
        {"="*39} "Informações da memoria" {"="*39}
        Total: {Get_size(svmem.total)}
        Disponível: {Get_size(svmem.available)}
        Usou: {Get_size(svmem.used)}
        Em Porcentagem: {svmem.percent}%     
    """

    return All

