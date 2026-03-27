package compositeFolder;

import java.util.ArrayList;
import java.util.List;

public class Folder implements Component {
    private String folderName;
    private List<Component> components = new ArrayList<>();

    public Folder(String name) {
        this.folderName = name;
    }

    @Override
    public int size() {
        int totalSize = 0;
        for (Component component : components) {
            totalSize += component.size();
        }
        return totalSize;
    }

    @Override
    public void printComponentName() {
    	System.out.println("Dir: [" + this.folderName + "]");
        
        for (Component child : components) {
            child.printComponentName();
        }
    }

    @Override
    public void add(Component component) {
        components.add(component);
    }

    @Override
    public void remove(Component component) {
        components.remove(component);
    }
}