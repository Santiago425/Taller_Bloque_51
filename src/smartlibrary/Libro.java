package smartlibrary;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class Libro {
    private String isbn;
    private String titulo;
    private String autor;
    private final List<Ejemplar> ejemplares = new ArrayList<>();

    public Libro(String isbn, String titulo, String autor) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.autor = autor;
    }

    /** El todo controla la creacion de la parte. */
    public Ejemplar agregarEjemplar(String codigoInventario) {
        Ejemplar ejemplar = new Ejemplar(codigoInventario, this);
        ejemplares.add(ejemplar);
        return ejemplar;
    }

    public List<Ejemplar> getEjemplares() { return Collections.unmodifiableList(ejemplares); }
    public String getIsbn() { return isbn; }
    public String getTitulo() { return titulo; }
    public String getAutor() { return autor; }
}
