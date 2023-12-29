//Basic hashtable program for beginners
import java.util.Enumeration;
import java.util.Hashtable;
public class Main
{
	public static void main(String[] args) {
		Hashtable<String,String> phonebook = new Hashtable<>();
		phonebook.put("1BY22MC013","Deena");
		phonebook.put("1BY22MC001","abc");
		phonebook.put("1BY22MC002","def");
		phonebook.put("1BY22MC003","hij");
		Enumeration<String> keys = phonebook.keys();
		System.out.println("The hashtable contains"+ phonebook);
		    while(keys.hasMoreElements())
		    {
		        String key = keys.nextElement();
		        System.out.println("Key:" + key + " value:" + phonebook.get(key));
		    }
		    
	}
	
}
