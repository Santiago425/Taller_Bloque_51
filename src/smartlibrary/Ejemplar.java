package smartlibrary;


public class Ejemplar {
    private String codigoInventario;
    private final Libro libro;   

    Ejemplar(String codigoInventario, Libro libro) {
        this.codigoInventario = codigoInventario;
        this.libro = libro;
    }

    public String getCodigoInventario() { return codigoInventario; }
    public Libro getLibro() { return libro; }
}
