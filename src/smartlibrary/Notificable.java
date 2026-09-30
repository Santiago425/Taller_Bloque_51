package smartlibrary;

/**
 * Contrato de comportamiento (R13): quien implemente esta interfaz
 * se compromete a poder recibir un mensaje del sistema.
 * No define COMO se entrega (consola, correo, SMS...).
 */
public interface Notificable {
    void notificar(String mensaje);
}
