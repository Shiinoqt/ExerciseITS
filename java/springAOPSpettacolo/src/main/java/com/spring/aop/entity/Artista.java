package com.spring.aop.entity;

import java.util.Random;

import org.springframework.stereotype.Component;

@Component
public class Artista {

	private String nome;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public void perform() {
		if(new Random().nextBoolean())
			System.out.println(nome + " sta eseguendo la sua performance");
		else
			throw new RuntimeException();
	}
}
