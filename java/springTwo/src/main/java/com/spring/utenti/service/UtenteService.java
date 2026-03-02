package com.spring.utenti.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;

import com.spring.utenti.dao.DAOUtenteMappa;
import com.spring.utenti.entity.Utente;

@Service
public class UtenteService {
	private DAOUtenteMappa dao = new DAOUtenteMappa();
	
	public boolean registra(Utente utente) {
		return dao.insert(utente);
	}
	
	public Utente cercaPerId(int id) {
		return dao.selectById(id);
	}
	
	public List<Utente> selectAll(){
		return new ArrayList<>(dao.selectAll());
	}
	
	public Utente aggiorna(Integer idUtente, Utente nuoviDati) {
		Utente esistente = dao.selectById(idUtente);
	    if (esistente != null) {
	    	esistente.setNome(nuoviDati.getNome());
	        esistente.setCognome(nuoviDati.getCognome());
	        return esistente;
	    }
	    return null;
	}
	
	public Utente delete(Integer idUtente) {
		return dao.delete(idUtente);
	}
}
