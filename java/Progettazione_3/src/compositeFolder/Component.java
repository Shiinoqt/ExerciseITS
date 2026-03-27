package compositeFolder;

public interface Component {
	int size();
	void printComponentName();
	void add(Component component) throws Exception;
	void remove(Component component) throws Exception;
}
