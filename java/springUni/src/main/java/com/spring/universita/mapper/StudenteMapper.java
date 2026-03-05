package com.spring.universita.mapper;

import com.spring.universita.entity.Studente;
import com.spring.universita.dto.StudenteDTO;

public class StudenteMapper {
	public static Studente StudenteDTOAStudente(StudenteDTO dto) {
		return new Studente(dto.getMatricola(), dto.getNome(), dto.getCognome(), dto.getIndirizzo(), dto.getAnnoNas(), dto.getAnnoImm());
	}
	
	public static StudenteDTO StudenteAStudenteDTO(Studente studente) {
		return new StudenteDTO(studente.getMatricola(), studente.getNome(), studente.getCognome(), studente.getIndirizzo(), studente.getAnnoNas(), studente.getAnnoImm());
	}
}

