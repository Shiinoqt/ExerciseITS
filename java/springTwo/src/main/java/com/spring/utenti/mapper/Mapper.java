package com.spring.utenti.mapper;

import com.spring.utenti.dto.UtenteDTO;
import com.spring.utenti.entity.Utente;

public class Mapper {
	public static Utente daUtenteDTOUtente(UtenteDTO dto) {
		return new Utente(dto.getIdUtente(), dto.getNome(), dto.getCognome(), dto.getMail(), dto.getTelefono());
	}
	
	public static UtenteDTO daUtenteAUtenteDTO(Utente utente) {
		return new UtenteDTO(utente.getIdUtente(), utente.getNome(), utente.getCognome(), utente.getMail(), utente.getTelefono());
	}
}
