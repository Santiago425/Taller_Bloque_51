package smartlibrary;

/**
 * Bibliotecario ES-UN Usuario.
 * Decision: NO implementa Notificable en este bloque. R13 dice que "algunos"
 * usuarios reciben notificaciones; los avisos del sistema (renovaciones,
 * reservas disponibles, vencimientos) van dirigidos a quien tiene el prestamo
 * o la reserva, es decir, al Estudiante. El bibliotecario es quien opera el
 * sistema. Si un requisito futuro lo exige, basta con agregar
 * "implements Notificable" sin tocar la jerarquia.
 */
public class Bibliotecario extends Usuario {
    private String codigoEmpleado;
    private String turno;

    public Bibliotecario(String identificacion, String nombre, String correo,
                         String codigoEmpleado, String turno) {
        super(identificacion, nombre, correo);
        this.codigoEmpleado = codigoEmpleado;
        this.turno = turno;
    }

    public String getCodigoEmpleado() { return codigoEmpleado; }
    public String getTurno() { return turno; }
}
