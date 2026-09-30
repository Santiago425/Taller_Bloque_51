package smartlibrary;

import java.time.LocalDate;


public class Renovacion {
    private final LocalDate fechaRenovacion;
    private final LocalDate fechaAnterior;
    private final LocalDate nuevaFecha;

    Renovacion(LocalDate fechaRenovacion, LocalDate fechaAnterior, LocalDate nuevaFecha) {
        this.fechaRenovacion = fechaRenovacion;
        this.fechaAnterior = fechaAnterior;
        this.nuevaFecha = nuevaFecha;
    }

    public LocalDate getFechaRenovacion() { return fechaRenovacion; }
    public LocalDate getFechaAnterior() { return fechaAnterior; }
    public LocalDate getNuevaFecha() { return nuevaFecha; }

    @Override
    public String toString() {
        return "Renovacion[realizada=" + fechaRenovacion + ", anterior=" + fechaAnterior
                + ", nueva=" + nuevaFecha + "]";
    }
}
