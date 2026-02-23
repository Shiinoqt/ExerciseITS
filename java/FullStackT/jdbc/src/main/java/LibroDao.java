import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class LibroDao {
    private static final String INSERT_SQL = "INSERT INTO libro (titolo, autore, prezzo) VALUES (?, ?, ?)";
    private static final String SELECT_SQL = "SELECT id, titolo, autore, prezzo FROM libro";

    public static List<LibroDTO> getItems() {
        List<LibroDTO> libri = new ArrayList<>();

        try (Connection con = Database.getConnection();
             PreparedStatement psSelect = con.prepareStatement(SELECT_SQL)) {
            ResultSet rs = psSelect.executeQuery();
            while(rs.next()) {
                LibroDTO l = new LibroDTO(rs.getInt("id"), rs.getString("titolo"), rs.getString("autore"),rs.getDouble("prezzo"));
                libri.add(l);
            }
        } catch (SQLException e) {
            System.err.println("Errore nel recupero dei dati: " + e.getMessage());
        }

        return libri;
    }

    public void insertItem(String titolo, String autore, double prezzo) {
        try (Connection con = Database.getConnection();
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

    public void printBooks() {
        List<LibroDTO> libri = LibroDao.getItems();

    }
}
