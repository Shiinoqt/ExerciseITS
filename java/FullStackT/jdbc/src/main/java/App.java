import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class App {
    private static final String URL = "jdbc:postgresql://localhost:5432/biblioteca";
    private static final String USER = "postgres";
    private static final String PSW = "postgres";
    private static final String INSERT_SQL = "INSERT INTO libro (titolo, autore, prezzo) VALUES (?, ?, ?)";
    private static final String SELECT_SQL = "SELECT id, titolo, autore, prezzo FROM libro";
    private static final String DELETE_SQL = "DELETE FROM LIBRO WHERE id = ?";

    public void insertItem(String titolo, String autore, double prezzo) {
        try (Connection con = DriverManager.getConnection(URL, USER, PSW);
             PreparedStatement psInsert = con.prepareStatement(INSERT_SQL)) {

            psInsert.setString(1, titolo);
            psInsert.setString(2, autore);
            psInsert.setDouble(3, prezzo);

            int rowsAffected = psInsert.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("Libro inserito con successo: " + titolo);
            }

        } catch (SQLException e) {
            System.err.println("Errore durante l'inserimento del libro: " + e.getMessage());
            throw new RuntimeException("Database error", e);
        }
    }

    public void getItems() {
        try (Connection con = DriverManager.getConnection(URL, USER, PSW);
             PreparedStatement psSelect = con.prepareStatement(SELECT_SQL)) {

            try (java.sql.ResultSet rs = psSelect.executeQuery()) {
                while (rs.next()) {
                    int id = rs.getInt("id");
                    String titolo = rs.getString("titolo");
                    String autore = rs.getString("autore");
                    double prezzo = rs.getDouble("prezzo");

                    System.out.println(id + " | " + titolo + " | " + autore + " | " + prezzo + "€");
                }
            }
        } catch (SQLException e) {
            System.err.println("Errore nel recupero dei dati: " + e.getMessage());
        }
    }

    public void deleteItem(int id) {
        try (Connection con = DriverManager.getConnection(URL, USER, PSW);
             PreparedStatement psDelete = con.prepareStatement(DELETE_SQL)) {

            psDelete.setInt(1, id);

            int rowsAffected = psDelete.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("Successo: Libro con ID " + id + " rimosso.");
            } else {
                System.out.println("Avviso: Nessun libro trovato con ID " + id);
            }

        } catch (SQLException e) {
            System.err.println("Errore durante la rimozione del libro: " + e.getMessage());
            throw new RuntimeException("Database error", e);
        }
    }

    public static void main(String[] args) {
//        try (Connection con = DriverManager.getConnection(URL, USER, PSW)) {
//
//            try (PreparedStatement psInsert = con.prepareStatement(insertSql)) {
//                psInsert.setString(1, "The Great Gatsby");
//                psInsert.setString(2, "F. Scott Fitzgerald");
//                psInsert.setDouble(3, 15.99);
//
//                int righe = psInsert.executeUpdate();
//                System.out.println(righe);
//            }
//
//            String selectSql = "Select id, titolo, autore, prezzo from libro";
//            try (PreparedStatement psSelect = con.prepareStatement(selectSql)) {
//                java.sql.ResultSet rs = psSelect.executeQuery();
//                while (rs.next()) {
//                    int id = rs.getInt("id");
//                    String titolo = rs.getString("titolo");
//                    String autore = rs.getString("autore");
//                    double prezzo = rs.getDouble("prezzo");
//                    System.out.println(id + " - " + titolo + " - " + autore + " - " + prezzo);
//                }
//            }
//
//
//        } catch (SQLException e) {
//            // It's helpful to print the full error to see what went wrong
//            System.err.println("Errore JDBC: " + e.getMessage());
//            e.printStackTrace();
//        }
        App app = new App();

        LibroDao librodao = new LibroDao();
//        librodao.insertItem("Informatica", "Bobby", 9.99);
        System.out.println(librodao.getItems());

        app.getItems();
    }
}