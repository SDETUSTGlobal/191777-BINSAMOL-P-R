package sel1;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class DemoWeborder {

	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver","D://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.navigate().to("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
		driver.findElement(By.xpath("/html/body/form/div[3]/input[1]")).sendKeys("Tester");
		driver.findElement(By.xpath("/html/body/form/div[3]/input[2]")).sendKeys("test");
		driver.findElement(By.xpath("/html/body/form/div[3]/input[3]")).click();
		driver.close();
		
	}

}
