F="font-family='Arial,Helvetica,sans-serif'"
o=[]
def comp(x,y,w,h,name,classes,fill):
    o.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{fill}' stroke='#333' stroke-width='1.5'/>")
    
    ix,iy=x+w-44,y+12
    o.append(f"<rect x='{ix}' y='{iy}' width='30' height='36' fill='white' stroke='#333'/>")
    o.append(f"<rect x='{ix-7}' y='{iy+7}' width='14' height='7' fill='white' stroke='#333'/>")
    o.append(f"<rect x='{ix-7}' y='{iy+22}' width='14' height='7' fill='white' stroke='#333'/>")
    o.append(f"<text x='{x+w/2-15}' y='{y+26}' text-anchor='middle' {F} font-size='12'>«component»</text>")
    o.append(f"<text x='{x+w/2-15}' y='{y+48}' text-anchor='middle' {F} font-size='17' font-weight='bold'>{name}</text>")
    o.append(f"<line x1='{x}' y1='{y+64}' x2='{x+w}' y2='{y+64}' stroke='#333' stroke-dasharray='3,3'/>")
    for i,c in enumerate(classes):
        o.append(f"<text x='{x+18}' y='{y+90+i*22}' {F} font-size='14'>▪ {c}</text>")
def dep(pts,label,lx,ly,anchor='middle'):
    d="M"+" L".join(f"{a},{b}" for a,b in pts)
    o.append(f"<path d='{d}' fill='none' stroke='#333' stroke-width='1.5' stroke-dasharray='8,5' marker-end='url(#arr)'/>")
    for i,l in enumerate(label.split('|')):
        o.append(f"<text x='{lx}' y='{ly+i*16}' text-anchor='{anchor}' {F} font-size='12.5' fill='#222'>{l}</text>")

W,H=1180,760
o.append(f"<rect x='20' y='20' width='{W-40}' height='{H-60}' fill='none' stroke='#555' stroke-width='1.5'/>")
o.append(f"<text x='36' y='46' {F} font-size='14' font-weight='bold'>«subsystem» SmartLibrary — vista funcional</text>")
comp(70,80,400,190,"Gestión de Usuarios",["Usuario (abstracta)","Estudiante, Bibliotecario","«interface» Notificable"],"#E8F5E9")
comp(710,80,400,190,"Gestión de Catálogo",["Libro","Ejemplar"],"#E0F7FA")
comp(70,470,400,190,"Gestión de Préstamos",["Prestamo","Renovacion"],"#FFF3E0")
comp(710,470,400,190,"Gestión de Reservas",["Reserva"],"#F3E5F5")
dep([(160,470),(160,272)],"«use»|identificar al estudiante|y notificarle",170,380,'start')
dep([(1020,470),(1020,272)],"«use»|consultar el libro|reservado",1030,380,'start')
dep([(470,500),(710,250)],"«use» ejemplar|disponible",482,440,'end')
dep([(710,500),(470,250)],"«use» estudiante|a notificar",698,440,'start')
dep([(470,600),(708,600)],"«use» ¿hay reserva pendiente|al devolver el ejemplar?",590,628,'middle')

svg=f"""<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>
<defs><marker id='arr' viewBox='0 0 20 20' refX='19' refY='10' markerWidth='14' markerHeight='14' orient='auto' markerUnits='userSpaceOnUse'><path d='M1,2 L19,10 L1,18' fill='none' stroke='#333' stroke-width='2'/></marker></defs>
<rect width='100%' height='100%' fill='white'/>
{chr(10).join(o)}
<text x='{W-24}' y='{H-12}' text-anchor='end' {F} font-size='12' fill='#666'>Flecha punteada = dependencia funcional «use» (el origen necesita información del destino)</text>
</svg>"""
open("../componentes.svg","w").write(svg)
