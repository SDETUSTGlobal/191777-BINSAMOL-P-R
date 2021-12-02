package dataTable;   
import java.util.List;  
import org.openqa.selenium.By;   
import org.openqa.selenium.WebDriver;   
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;  
import cucumber.annotation.en.Given;   
import cucumber.annotation.en.Then;   
import cucumber.annotation.en.When;   
import cucumber.table.DataTable;  
public class StepLogin {   
   WebDriver driver = null;  
   @Given("User is on the Home Page$")   
   public void goTosmartbearssoftware() {
	   System.setProperty("webdriver.chrome.driver","E://Sel_jars//chromedriver_win32//chromedriver.exe");
       WebDriver driver = new ChromeDriver();
       
      driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx");   
   }   
      
   @When("User enters Credentials to LogIn$")   
   public void enterData(DataTable table){   
      //Initialize data table   
	   List<List<String>> data = table.raw(); 
         
        
        
      driver.findElement(By.id("ctl00_MainContent_username")).sendKeys("Tester");    
      driver.findElement(By.id("ctl00_MainContent_password")).sendKeys("test");
      driver.findElement(By.id("ctl00_MainContent_login_button")).click();
        
         
   }   
      
   @Then("^User Login should be successful$")   
   public void User_Login_should_be_successful() {
if(driver.getCurrentUrl().equalsIgnoreCase("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Login.aspx")) 
         System.out.println("Test Pass");   
      else {   
         System.out.println("Test Failed");   
      }   
      driver.close();   
   }   
}
