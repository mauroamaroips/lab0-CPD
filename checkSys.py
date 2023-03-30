# Computação Paralela e Distribuída 2020/2021
# Aluno: Mauro Amaro
# Número: 202000905
# Turma:
#############################################
import platform, subprocess


def get_processor_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep name | cut -d ' ' -f 3-8"
        return str(subprocess.check_output(command, shell=True)).strip("b'\\n")
    return ""


if __name__ == '__main__':
    print(get_processor_info())

# Além disso, e para este código, inclua comentários indicando (pesquise…):

# a. O que faz o import?
# Resposta: Em Python, o import é usado para importar módulos, que são arquivos que contém definições de classes
# funções e variáveis.

# b. Quais são algumas funcionalidades dos módulos importados?
# Resposta: Algumas das funcionalidades que os módulos importados disponibilizam são:
# - Acesso a bibliotecas de funções que implementam algoritmos específicos;
# - Definição de classes, funções e variáveis que podem ser reutilizadas em outros programas;
# - Possibilidade de estender a funcionalidade de um programa existente adicionando novos módulos ou bibliotecas de terceiros;
# - Entre outros.

# c. O que faz a função str()?
# Resposta: Em Python, a função 'str()' é usada para converter um objeto em uma string.

# d. O que faz o método strip()?
# Resposta: Em Python, o método 'strip()' é usado para remover os espaçoes em branco no início e no final de uma string.
# É retornada uma nova string com todos os espaços em branco removidos.