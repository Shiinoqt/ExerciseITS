package compositeFolder;

public class main {
	public static void main(String[] args) throws Exception {
		Component file1 = new File("Resume.pdf", 200);
        Component file2 = new File("Photo.png", 500);
        Component file3 = new File("ciao.txt", 10);
        
        Folder myFolder = new Folder("My Documents");
        Folder myFolder2 = new Folder("My Words");
        
        myFolder.add(file1);
        myFolder.add(file2);
        
        myFolder2.add(file3);
        
        myFolder.add(myFolder2);
        
        myFolder.printComponentName();
        myFolder2.printComponentName();
        System.out.println("Total Size: " + myFolder.size() + "KB");
	}

}
