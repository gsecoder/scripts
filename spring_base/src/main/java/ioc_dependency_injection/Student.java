package ioc_dependency_injection;

import java.util.*;

/**
 * @Author sf
 * @File Student
 * @Time 2021-03-27 11:00
 * @Description
 */
public class Student {
	
	private String name;
	private Address address;
	private String[] books;
	private List<String> hobbies;
	private Map<String, String> card;
	private Set<String> games;
	private String wife;
	private Properties info;

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public Address getAddress() {
		return address;
	}
	
	public void setAddress(Address address) {
		this.address = address;
	}
	
	public String[] getBooks() {
		return books;
	}
	
	public void setBooks(String[] books) {
		this.books = books;
	}
	
	public List<String> getHobbies() {
		return hobbies;
	}
	
	public void setHobbies(List<String> hobbies) {
		this.hobbies = hobbies;
	}
	
	public Map<String, String> getCard() {
		return card;
	}
	
	public void setCard(Map<String, String> card) {
		this.card = card;
	}
	
	public Set<String> getGames() {
		return games;
	}
	
	public void setGames(Set<String> games) {
		this.games = games;
	}
	
	public String getWife() {
		return wife;
	}
	
	public void setWife(String wife) {
		this.wife = wife;
	}
	
	public Properties getInfo() {
		return info;
	}
	
	public void setInfo(Properties info) {
		this.info = info;
	}

	@Override
	public String toString() {
		return "Student{" +
				       "books=" + Arrays.toString(books) +
				       '}';
	}

	public void show(){
		System.out.println("name=" + name + ", address=" + address.getAddress() + ", books=");
		for (String book:books){
			System.out.println("<<" + book + ">>\t");
		}
		System.out.println("\n爱好：" + hobbies);
		System.out.println("card: " + card);
		System.out.println("games: " + games);
		System.out.println("wife: " + wife);
		System.out.println("info: " + info);
	}
	
}
