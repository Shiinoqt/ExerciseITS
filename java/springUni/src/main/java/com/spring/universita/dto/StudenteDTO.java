package com.spring.universita.dto;

import java.util.Objects;

public class StudenteDTO {
	private String matricola, nome, cognome, indirizzo;
	private int annoNas, annoImm;
	
	public StudenteDTO() {}
	
	public StudenteDTO(String matricola, String nome, String cognome, String indirizzo, int annoNas, int annoImm) {
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.indirizzo = indirizzo;
		this.annoNas = annoNas;
		this.annoImm = annoImm;
	}

	public String getMatricola() {
		return matricola;
	}

	public void setMatricola(String matricola) {
		this.matricola = matricola;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public String getIndirizzo() {
		return indirizzo;
	}

	public void setIndirizzo(String indirizzo) {
		this.indirizzo = indirizzo;
	}

	public int getAnnoNas() {
		return annoNas;
	}

	public void setAnnoNas(int annoNas) {
		this.annoNas = annoNas;
	}

	public int getAnnoImm() {
		return annoImm;
	}

	public void setAnnoImm(int annoImm) {
		this.annoImm = annoImm;
	}

	@Override
	public int hashCode() {
		return Objects.hash(matricola);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		StudenteDTO other = (StudenteDTO) obj;
		return Objects.equals(matricola, other.matricola);
	}
}
