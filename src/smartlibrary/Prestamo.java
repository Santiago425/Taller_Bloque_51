package smartlibrary;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class Prestamo {
    private Estudiante estudiante;
    private Ejemplar ejemplar;
    private LocalDate fechaPrestamo;
    private LocalDate fechaPrevistaDevolucion;
    private final List<Renovacion> renovaciones = new ArrayList<>();

    public Prestamo(Estudiante estudiante, Ejemplar ejemplar,
                    LocalDate fechaPrestamo, LocalDate fechaPrevistaDevolucion) {
        if (estudiante == null || ejemplar == null) {
            throw new IllegalArgumentException("Un prestamo requiere un estudiante y un ejemplar.");
        }
        this.estudiante = estudiante;
        this.ejemplar = ejemplar;
        this.fechaPrestamo = fechaPrestamo;
        this.fechaPrevistaDevolucion = fechaPrevistaDevolucion;
    }

    public void renovar(LocalDate nuevaFecha) {
        renovar(nuevaFecha, LocalDate.now());
    }

    /** Variante con fecha de renovacion explicita (util para pruebas reproducibles). */
    public void renovar(LocalDate nuevaFecha, LocalDate fechaRenovacion) {
        // 1. validar que nuevaFecha sea posterior a la fecha actual prevista
        if (nuevaFecha == null || !nuevaFecha.isAfter(fechaPrevistaDevolucion)) {
            throw new IllegalArgumentException("Renovacion invalida: la nueva fecha (" + nuevaFecha
                    + ") debe ser posterior a la fecha prevista vigente (" + fechaPrevistaDevolucion + ").");
        }
        // 2. crear la Renovacion
        Renovacion renovacion = new Renovacion(fechaRenovacion, fechaPrevistaDevolucion, nuevaFecha);
        // 3. almacenarla
        renovaciones.add(renovacion);
        // 4. actualizar fechaPrevistaDevolucion
        fechaPrevistaDevolucion = nuevaFecha;
    }

    public Estudiante getEstudiante() { return estudiante; }
    public Ejemplar getEjemplar() { return ejemplar; }
    public LocalDate getFechaPrestamo() { return fechaPrestamo; }
    public LocalDate getFechaPrevistaDevolucion() { return fechaPrevistaDevolucion; }
    /** Vista de solo lectura: nadie externo puede agregar o borrar renovaciones. */
    public List<Renovacion> getRenovaciones() { return Collections.unmodifiableList(renovaciones); }
    public int getCantidadRenovaciones() { return renovaciones.size(); }
}
