public class TaskDTO {
    private int id;
    private String task;
    private boolean done;

    public TaskDTO(int id, String task, boolean done) {
        this.done = false;
        this.id = id;
        this.task = task;
    }

    public TaskDTO(String task, boolean done) {
        this.done = false;
        this.task = task;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTask() {
        return task;
    }

    public void setTask(String task) {
        this.task = task;
    }

    public boolean isDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }

    @Override
    public String toString() {
        return "TaskDTO{" +
                "id=" + id +
                ", task='" + task + '\'' +
                ", done=" + done +
                '}';
    }
}
