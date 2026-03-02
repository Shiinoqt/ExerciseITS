import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TaskDAO {
    private static final String INSERT_SQL = "INSERT INTO task (task, done) VALUES (?, ?)";
    private static final String SELECT_SQL = "SELECT id, task, done FROM task";

    public void insertItem(String task, boolean done) {
        try (Connection con = Database.getConnection();
             PreparedStatement psInsert = con.prepareStatement(INSERT_SQL)) {

            psInsert.setString(1, task);
            psInsert.setBoolean(2, done);

            int rowsAffected = psInsert.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("Task inserita con successo: " + task);
            }

        } catch (SQLException e) {
            System.err.println("Errore durante l'inserimento della task: " + e.getMessage());
            throw new RuntimeException("Database error", e);
        }
    }
}