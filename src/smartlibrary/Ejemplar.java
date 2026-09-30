package smartlibrary;

/** Copia fisica de un Libro. Cada ejemplar corresponde a un unico libro (R10). */
public class Ejemplar {
    private String codigoInventario;
    private final Libro libro;   // 1 y solo 1, inmutable

    // Constructor de paquete: solo Libro.agregarEjemplar(...) crea ejemplares
    Ejemplar(String codigoInventario, Libro libro) {
        this.codigoInventario = codigoInventario;
        this.libro = libro;
    }

    public String getCodigoInventario() { return codigoInventario; }
    public Libro getLibro() { return libro; }
}
