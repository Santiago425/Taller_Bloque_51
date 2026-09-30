F="font-family='Arial,Helvetica,sans-serif'"
out=[]
B={}
def dia(x,y,dx,dy):
    # rombo relleno con punta en (x,y) que se extiende en direccion (dx,dy)
    px,py=-dy,dx
    pts=[(x,y),(x+dx*13+px*7,y+dy*13+py*7),(x+dx*26,y+dy*26),(x+dx*13-px*7,y+dy*13-py*7)]
    out.append("<polygon points='"+" ".join(f"{a},{b}" for a,b in pts)+"' fill='#333' stroke='#333'/>")
def box(name,x,y,w,attrs,meths,stereo=None,italic=False,fill="#FFF8E1"):
    hh=58 if stereo else 36
    ah=max(1,len(attrs))*19+12
    mh=max(1,len(meths))*19+12 if meths is not None else 14
    h=hh+ah+mh
    out.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{fill}' stroke='#333' stroke-width='1.5'/>")
    cy=y+22
    if stereo:
        out.append(f"<text x='{x+w/2}' y='{cy}' text-anchor='middle' {F} font-size='13'>«{stereo}»</text>"); cy+=22
    st=" font-style='italic'" if italic else ""
    out.append(f"<text x='{x+w/2}' y='{cy}' text-anchor='middle' {F} font-size='16' font-weight='bold'{st}>{name}</text>")
    out.append(f"<line x1='{x}' y1='{y+hh}' x2='{x+w}' y2='{y+hh}' stroke='#333'/>")
    for i,a in enumerate(attrs):
        out.append(f"<text x='{x+10}' y='{y+hh+21+i*19}' {F} font-size='13'>{a}</text>")
    out.append(f"<line x1='{x}' y1='{y+hh+ah}' x2='{x+w}' y2='{y+hh+ah}' stroke='#333'/>")
    for i,m in enumerate(meths or []):
        out.append(f"<text x='{x+10}' y='{y+hh+ah+21+i*19}' {F} font-size='13'>{m}</text>")
    B[name]=(x,y,w,h)
def T(x,y,s,anchor='start',size=13,bold=False,italic=False,color='#000'):
    fw=' font-weight="bold"' if bold else ''; fi=' font-style="italic"' if italic else ''
    out.append(f"<text x='{x}' y='{y}' text-anchor='{anchor}' {F} font-size='{size}' fill='{color}'{fw}{fi}>{s}</text>")
def P(pts,dash=False,marker=None,start=None):
    d="M"+" L".join(f"{a},{b}" for a,b in pts)
    da=' stroke-dasharray="7,5"' if dash else ''; me=f' marker-end="url(#{marker})"' if marker else ''; ms=f' marker-start="url(#{start})"' if start else ''
    out.append(f"<path d='{d}' fill='none' stroke='#333' stroke-width='1.5'{da}{me}{ms}/>")

box("Notificable",60,30,300,[],["+notificar(mensaje: String): void"],stereo="interface",fill="#E3F2FD")
box("Usuario",560,30,320,["- identificacion: String","- nombre: String","- correo: String"],["+getNombre(): String"],stereo="abstract",italic=True,fill="#E8F5E9")
box("Estudiante",300,300,330,["- codigoEstudiantil: String","- programaAcademico: String"],["+notificar(mensaje: String): void"],fill="#E8F5E9")
box("Bibliotecario",800,300,280,["- codigoEmpleado: String","- turno: String"],[],fill="#E8F5E9")
box("Prestamo",60,560,380,["- fechaPrestamo: LocalDate","- fechaPrevistaDevolucion: LocalDate"],["+renovar(nuevaFecha: LocalDate): void","+getRenovaciones(): List&lt;Renovacion&gt;"],fill="#FFF3E0")
box("Reserva",760,570,280,["- fechaReserva: LocalDate","- estado: String"],[],fill="#F3E5F5")
box("Renovacion",40,850,320,["- fechaRenovacion: LocalDate","- fechaAnterior: LocalDate","- nuevaFecha: LocalDate"],[],fill="#FFF3E0")
box("Ejemplar",440,870,250,["- codigoInventario: String"],[],fill="#E0F7FA")
box("Libro",820,850,340,["- isbn: String","- titulo: String","- autor: String"],["+agregarEjemplar(codigo: String): Ejemplar"],fill="#E0F7FA")

def bot(n,f=.5): x,y,w,h=B[n]; return (x+w*f,y+h)
def top(n,f=.5): x,y,w,h=B[n]; return (x+w*f,y)
# Generalizacion
ub=bot("Usuario"); P([top("Estudiante",.62),(top("Estudiante",.62)[0],250),(ub[0],250)]); P([top("Bibliotecario"),(top("Bibliotecario")[0],250),(ub[0],250),(ub[0],ub[1]+2)],marker="tri")
# Realizacion
nb=bot("Notificable"); P([top("Estudiante",.2),(top("Estudiante",.2)[0],230),(nb[0],230),(nb[0],nb[1]+2)],dash=True,marker="tri")
T(nb[0]+8,215,"«realiza»",size=12,italic=True)
# Estudiante -> Prestamo
s=bot("Estudiante",.2); e=top("Prestamo",.6)
P([s,(s[0],500),(e[0],500),(e[0],e[1]-1)],marker="arr")
T(s[0]+6,s[1]+18,"1"); T(e[0]+6,e[1]-8,"0..*"); T((s[0]+e[0])/2-10,492,"solicita",'middle',italic=True)
# Estudiante -> Reserva
s=bot("Estudiante",.8); e=top("Reserva",.4)
P([s,(s[0],520),(e[0],520),(e[0],e[1]-1)],marker="arr")
T(s[0]+6,s[1]+18,"1"); T(e[0]+6,e[1]-8,"0..*"); T((s[0]+e[0])/2+20,512,"realiza",'middle',italic=True)
# Prestamo <>-- Renovacion
s=bot("Prestamo",.3); e=top("Renovacion",.4)
s=(e[0],s[1]); P([(s[0],s[1]+26),(e[0],e[1])]); dia(s[0],s[1],0,1)
T(s[0]+12,s[1]+22,"1"); T(e[0]+6,e[1]-8,"0..*"); T(s[0]+8,780,"historial",italic=True)
# Prestamo -> Ejemplar
s=bot("Prestamo",.8); e=top("Ejemplar",.5)
P([s,(s[0],820),(e[0],820),(e[0],e[1]-1)],marker="arr")
T(s[0]+6,s[1]+18,"0..*"); T(e[0]+8,e[1]-8,"1"); T(e[0]-10,812,"presta",'middle',italic=True)
# Reserva -> Libro
s=bot("Reserva",.5); e=top("Libro",.4)
P([s,(s[0],800),(e[0],800),(e[0],e[1]-1)],marker="arr")
T(s[0]+6,s[1]+18,"0..*"); T(e[0]+8,e[1]-8,"1"); T(s[0]+8,780,"reserva",italic=True)
# Libro <>-- Ejemplar
x,y,w,h=B["Ejemplar"]; lx=B["Libro"][0]
P([(lx-26,y+45),(x+w,y+45)]); dia(lx,y+45,-1,0)
T(lx-30,y+38,"1",'end'); T(x+w+8,y+38,"1..*"); T((lx+x+w)/2,y+65,"tiene",'middle',italic=True)

W,H=1200,1060
svg=f"""<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}'>
<defs>
<marker id='tri' viewBox='0 0 20 20' refX='19' refY='10' markerWidth='18' markerHeight='18' orient='auto' markerUnits='userSpaceOnUse'><path d='M1,1 L19,10 L1,19 Z' fill='white' stroke='#333' stroke-width='1.5'/></marker>
<marker id='arr' viewBox='0 0 20 20' refX='19' refY='10' markerWidth='14' markerHeight='14' orient='auto' markerUnits='userSpaceOnUse'><path d='M1,2 L19,10 L1,18' fill='none' stroke='#333' stroke-width='2'/></marker>
<marker id='dia' viewBox='0 0 28 16' refX='1' refY='8' markerWidth='28' markerHeight='16' orient='auto-start-reverse' markerUnits='userSpaceOnUse'><path d='M1,8 L14,1 L27,8 L14,15 Z' fill='#333' stroke='#333'/></marker>
</defs>
<rect width='100%' height='100%' fill='white'/>
<text x='{W-20}' y='{H-15}' text-anchor='end' {F} font-size='12' fill='#666'>SmartLibrary – Diagrama de clases (Bloque 5)</text>
{chr(10).join(out)}
</svg>"""
open("../clases.svg","w").write(svg)
