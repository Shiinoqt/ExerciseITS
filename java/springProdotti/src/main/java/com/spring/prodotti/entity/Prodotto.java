package com.spring.prodotti.entity;

public class Prodotto {
	private int id;
	private String descrizione;
	
	public Prodotto() {}
	
	public Prodotto(int id, String descrizione) {
		this.id = id;
		this.descrizione = descrizione;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDescrizione() {
		return descrizione;
	}

	public void setDescrizione(String descrizione) {
		this.descrizione = descrizione;
	}
}
