from django.shortcuts import render

# Create your views here.
def color_generation(request):

    def hex_converter(number):
        hex_number = str(hex(number)).replace('0x', '')
        if len(hex_number) == 1:
            hex_number = '0' + hex_number
        return hex_number

    def red_attempt(red_par):
        return "#%s0000" % hex_converter(red_par)

    red_shades = ["#%s0000" % hex_converter(red_par) for red_par in range(255,5,-5)]
    green_shades = ["#00%s00" % hex_converter(green_par) for green_par in range(255,5,-5)]
    blue_shades = ["#0000%s" % hex_converter(blue_par) for blue_par in range(255,5,-5)]
    gray_shades = ["#" + hex_converter(color_par) * 3 for color_par in range(255,5,-5)]

    shades = zip(red_shades, green_shades, blue_shades, gray_shades)

    return render(request, 'ex03/table.html', {'shades': shades})
