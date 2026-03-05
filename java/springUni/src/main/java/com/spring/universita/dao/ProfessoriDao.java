package com.spring.universita.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.spring.universita.entity.Professore;

public class ProfessoriDao {

	private Map<Integer, Professore> mappa = new HashMap<>();

	public boolean insert(Professore utente) {
		if(mappa.containsKey(utente.getId()))
			return false;
		
		mappa.put(utente.getId(), utente);
		return true;

	}
	public List<Professore> selectAll(){
		return new ArrayList<>(mappa.values());
	}

	public Professore selectById(Integer idUtente) {
		return mappa.get(idUtente);
	}
	
	public Professore delete(Integer idUtente) {
		Professore utente = mappa.remove(idUtente);
		return utente;
	}
}
