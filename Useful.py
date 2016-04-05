

def setting_plot():
    params1 = {'backend': 'pdf',
               'axes.labelsize': 14,
               'text.fontsize': 16,
               'xtick.labelsize': 16,
               'ytick.labelsize': 16,
               #'legend.draw_frame': False,
               'legend.fontsize': 12,
               'lines.markersize': 6,
               'font.size': 16,
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


