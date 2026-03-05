package com.spring.universita.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.spring.universita.entity.Studente;

public class StudentiDao {
	private Map<String, Studente> mappa = new HashMap<>();

	public boolean insert(Studente utente) {
		if(mappa.containsKey(utente.getMatricola()))
			return false;
		
		mappa.put(utente.getMatricola(), utente);
		return true;
	}

	public Studente selectByMatricola(String matricola) {
		return mappa.get(matricola);
	}
	
	public List<Studente> selectAll(){
		return new ArrayList<>(mappa.values());
	}
	
	public Studente delete(String matricola) {
		Studente utente = mappa.remove(matricola);
		return utente;
	}
}
