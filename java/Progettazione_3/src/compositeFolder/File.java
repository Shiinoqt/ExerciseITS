package compositeFolder;

public class File implements Component {
	private String filename;
	private int size;

	public File(String fileName, int size) {
		this.filename = fileName;
		this.size = size;
	}

	public String getFilename() {
		return filename;
	}

	public void setFilename(String filename) {
		this.filename = filename;
	}

	public int getSize() {
		return size;
	}

	public void setSize(int size) {
		this.size = size;
	}

	@Override
	public int size() {
		return getSize();
	}

	@Override
	public void printComponentName() {
		System.out.println("File: " + this.filename + " (" + this.size + "KB)");
	}

	@Override
	public void add(Component component) throws Exception{
		if (this instanceof File) {
			throw new Exception("Cannot do this operation");
		}
	}

	@Override
	public void remove(Component component) throws Exception {
		if (this instanceof File) {
			throw new Exception("Cannot do this operation");
		}
	}
}
