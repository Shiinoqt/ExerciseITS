package com.spring.universita.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.universita.dto.StudenteDTO;
import com.spring.universita.entity.Studente;
import com.spring.universita.service.StudentiService;
import com.spring.utenti.entity.Utente;

@RestController
@RequestMapping(path="/studenti")
public class StudentiController {
	private final StudentiService service;
	
	public StudentiController(StudentiService service) {
		this.service = service;
	}

	@GetMapping(path="/registra", consumes = "application/json")
	public boolean registra(@RequestBody StudenteDTO studente) {
		return service.registra(studente);
	}
	
	@GetMapping(path="/", produces = "application/json") 
	public List<StudenteDTO> listaStudenti() {
		return service.selectAll();
	}
	
	@GetMapping(path="/elimina/{matricola}", produces = "applicaiton/json")
	public String elimina(@PathVariable String matricola) {
		return service.delete(matricola);
	}
	
	@GetMapping(path="/modificaIndirizzo/{matricola}", consumes = "application/json", produces = "application/json")
	public StudenteDTO aggiornaIndirizzo(@PathVariable String matricola, @RequestBody Studente newIndirizzo) {
		return service.modificaIndirizzo(matricola, newIndirizzo);
	}
	
}
