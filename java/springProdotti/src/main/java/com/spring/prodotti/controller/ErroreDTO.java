package com.spring.prodotti.controller;

public class ErroreDTO {
	private String message;
	
	public ErroreDTO() {
		// TODO Auto-generated constructor stub
	}

	public ErroreDTO(String message) {
		super();
		this.message = message;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
}
