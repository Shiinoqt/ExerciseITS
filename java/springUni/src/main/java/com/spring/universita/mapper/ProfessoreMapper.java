package com.spring.universita.mapper;

import com.spring.universita.dto.ProfessoreDTO;
import com.spring.universita.entity.Professore;

public class ProfessoreMapper {
	public static Professore ProfessoreDTOAProfessore(ProfessoreDTO dto) {
		return new Professore(dto.getId(),dto.getNome(),dto.getCognome(),dto.getMateria());
	}
	
	public static ProfessoreDTO ProfessoreAProfessoreDTO(Professore professore) {
		return new ProfessoreDTO(professore.getId(),professore.getNome(),professore.getCognome(),professore.getMateria());
	}
}
