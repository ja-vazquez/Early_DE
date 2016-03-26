

def setting_plot():
    params1 = {'backend': 'pdf',
               'axes.labelsize': 16,
               'text.fontsize': 18,
               'xtick.labelsize': 18,
               'ytick.labelsize': 18,
               #'legend.draw_frame': False,
               'legend.fontsize': 12,
               'lines.markersize': 6,
               'font.size': 18,
               'text.usetex': True}
    return params1



def colour(x):
    if x==1: return 'red'
    if x==2: return 'blue'
    if x==3: return 'green'
    if x==4: return 'cyan'
    if x==5: return 'magenta'
    if x==6: return 'black'
    if x==7: return 'green'
    if x==8: return 'yellow'
    if x==9: return 'purple'
    if x>9: return 'black'
    print("Increased colouring")


