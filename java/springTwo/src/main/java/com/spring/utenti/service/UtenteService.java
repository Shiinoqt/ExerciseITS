package com.spring.utenti.service;

import com.spring.utenti.mapper.*;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;

import com.spring.utenti.dao.DAOUtenteMappa;
import com.spring.utenti.dto.UtenteDTO;
import com.spring.utenti.entity.Utente;

@Service
public class UtenteService {
	private DAOUtenteMappa dao = new DAOUtenteMappa();
	
	public boolean registra(UtenteDTO dto) {
		Utente utente = Mapper.daUtenteDTOUtente(dto);
		
		return dao.insert(utente);
	}
	
	public UtenteDTO cercaPerId(int id) {
		Utente utente = dao.selectById(id);
		if(utente != null) {
			return Mapper.daUtenteAUtenteDTO(utente);
		} else { return null; }
	}
	
	public List<UtenteDTO> selectAll(){
		List<Utente> lista = dao.selectAll();
		
		return lista.stream()
				.map(utente -> Mapper.daUtenteAUtenteDTO(utente))
				.collect(Collectors.toList());
	}
	
	public UtenteDTO aggiorna(Integer idUtente, Utente nuoviDati) {
		Utente esistente = dao.selectById(idUtente);

	    if (esistente != null) {
	    	esistente.setNome(nuoviDati.getNome());
	        esistente.setCognome(nuoviDati.getCognome());
	        
	        return Mapper.daUtenteAUtenteDTO(esistente);
	    }
	    return null;
	}
	
	public UtenteDTO delete(Integer idUtente) {
	    Utente utenteEliminato = dao.delete(idUtente);
	    
	    if (utenteEliminato != null) {
	        return Mapper.daUtenteAUtenteDTO(utenteEliminato);
	    }
	    return null;
	}
}
