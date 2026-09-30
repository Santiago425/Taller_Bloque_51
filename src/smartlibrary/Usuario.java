package smartlibrary;

/**
 * Generalizacion (R12). Es abstracta porque en SmartLibrary no existe
 * un usuario "generico": todo usuario es Estudiante o Bibliotecario.
 */
public abstract class Usuario {
    private String identificacion;
    private String nombre;
    private String correo;

    public Usuario(String identificacion, String nombre, String correo) {
        this.identificacion = identificacion;
        this.nombre = nombre;
        this.correo = correo;
    }

    public String getIdentificacion() { return identificacion; }
    public String getNombre() { return nombre; }
    public String getCorreo() { return correo; }
}
