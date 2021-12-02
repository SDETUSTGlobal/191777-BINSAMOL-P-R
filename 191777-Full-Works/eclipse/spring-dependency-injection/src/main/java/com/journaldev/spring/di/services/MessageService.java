package com.journaldev.spring.di.services;
 
public interface MessageService {
 
	boolean sendMessage(String msg, String rec);
}


public class EmailService implements MessageService {
 
	public boolean sendMessage(String msg, String rec) {
		System.out.println("Email Sent to "+rec+ " with Message="+msg);
		return true;
	}
 
}
 
package com.journaldev.spring.di.services;
 
public class TwitterService implements MessageService {
 
	public boolean sendMessage(String msg, String rec) {
		System.out.println("Twitter message Sent to "+rec+ " with Message="+msg);
		return true;
	}
 
}

