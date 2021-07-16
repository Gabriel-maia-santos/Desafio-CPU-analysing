import psutil


def CPU():
    # Titulo
    cpufreq = psutil.cpu_freq()
    All = f"""
        {"="*45} "Informações da CPU" {"="*45}
        Frequencia Maxima: {cpufreq.max:.2f}Mhz
        Frequencia Minima: {cpufreq.min:.2f}Mhz
        Atual Frequencia: {cpufreq.current:.2f}Mhz
        Usando um Total de: {psutil.cpu_percent()}% da CPU
    """
    return All
