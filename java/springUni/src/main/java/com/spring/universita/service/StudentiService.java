package com.spring.universita.service;

import java.util.List;

import org.springframework.stereotype.Service;
import com.spring.universita.mapper.StudenteMapper;
import com.spring.universita.dao.StudentiDao;
import com.spring.universita.dto.StudenteDTO;
import com.spring.universita.entity.Studente;

@Service
public class StudentiService {
	private StudentiDao dao = new StudentiDao();
	
	public boolean registra(StudenteDTO dto) {
		Studente studente = StudenteMapper.StudenteDTOAStudente(dto);
		return dao.insert(studente);
	}
	
	public StudenteDTO cercaPerMatricola(String matricola) {
		Studente studente = dao.selectByMatricola(matricola);
		
		if (studente != null) {
			return StudenteMapper.StudenteAStudenteDTO(studente);
		}
		return null;
	}
	
	public List<StudenteDTO> selectAll() {
		List<Studente> lista = dao.selectAll();
		
		return lista.stream()
				.map(studente -> StudenteMapper.StudenteAStudenteDTO(studente))
				.toList();
	}
	
	public String delete(String matricola) {
		Studente studenteEliminato = dao.delete(matricola);
		
		if (studenteEliminato != null) {
			return "Studente eliminato: " + StudenteMapper.StudenteAStudenteDTO(studenteEliminato);
		}
		return null;
	}
	
	public StudenteDTO modificaIndirizzo(String matricola, String newIndirizzo) {
	    Studente studente = dao.selectByMatricola(matricola);
	    
	    if (studente != null) {
	    	studente.setIndirizzo(newIndirizzo);
	    	dao.insert(studente);
	    	
	    	return StudenteMapper.StudenteAStudenteDTO(studente);
	    }
	    return null;
	}
}
