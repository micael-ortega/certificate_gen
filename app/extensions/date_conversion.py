def convert_month(valor):
    months = ['', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
              'julho', 'agosto', 'setembro', 'outobro', 'novembro', 'dezembro']

    return months[valor]

def convert(data):
    data = data.split('-')
    month = int(data[1])

    return "{} de {} de {}".format(data[2], convert_month(month), data[0])