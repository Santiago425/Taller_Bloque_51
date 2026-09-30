package smartlibrary;

import java.time.LocalDate;


public class Main {
    public static void main(String[] args) {
        Estudiante estudiante = new Estudiante("1001", "Santiago Campoverde",
                "santiago@campusucc.edu.co", "EST-2026-001", "Ingenieria de Software");
        Bibliotecario bibliotecario = new Bibliotecario("2001", "Laura Gomez",
                "laura.gomez@ucc.edu.co", "EMP-015", "Manana");

        Libro libro = new Libro("978-0134685991", "Effective Java", "Joshua Bloch");
        Ejemplar ejemplar = libro.agregarEjemplar("EJ-0001");
        libro.agregarEjemplar("EJ-0002");

        Prestamo prestamo = new Prestamo(estudiante, ejemplar,
                LocalDate.of(2026, 9, 24), LocalDate.of(2026, 10, 8));

        System.out.println("=== PRUEBA 1: renovacion valida ===");
        System.out.println("Libro: " + libro.getTitulo() + " | ejemplares: " + libro.getEjemplares().size());
        System.out.println("Prestamo de " + prestamo.getEstudiante().getNombre()
                + " (atendido por " + bibliotecario.getNombre() + "), ejemplar "
                + prestamo.getEjemplar().getCodigoInventario());
        System.out.println("Fecha prevista inicial: " + prestamo.getFechaPrevistaDevolucion());

        prestamo.renovar(LocalDate.of(2026, 10, 15));
        estudiante.notificar("Su prestamo fue renovado.");
        System.out.println("Nueva fecha prevista: " + prestamo.getFechaPrevistaDevolucion());
        System.out.println("Cantidad de renovaciones: " + prestamo.getCantidadRenovaciones());
        System.out.println("Historial: " + prestamo.getRenovaciones());

        System.out.println();
        System.out.println("=== PRUEBA 2: renovacion invalida (fecha anterior a la vigente) ===");
        try {
            prestamo.renovar(LocalDate.of(2026, 10, 10));
            System.out.println("ERROR: se acepto una renovacion invalida");
        } catch (IllegalArgumentException e) {
            System.out.println("Rechazada correctamente -> " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== PRUEBA 3: renovacion invalida (misma fecha vigente) ===");
        try {
            prestamo.renovar(LocalDate.of(2026, 10, 15));
            System.out.println("ERROR: se acepto una renovacion invalida");
        } catch (IllegalArgumentException e) {
            System.out.println("Rechazada correctamente -> " + e.getMessage());
        }

        System.out.println();
        System.out.println("Estado final: fecha prevista = " + prestamo.getFechaPrevistaDevolucion()
                + ", renovaciones = " + prestamo.getCantidadRenovaciones());
    }
}
