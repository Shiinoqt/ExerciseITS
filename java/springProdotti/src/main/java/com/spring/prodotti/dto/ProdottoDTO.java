package com.spring.prodotti.dto;

public class ProdottoDTO {
	private int id;
	private String descrizione;
	
	public ProdottoDTO() {}
	
	public ProdottoDTO(int id, String descrizione) {
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
