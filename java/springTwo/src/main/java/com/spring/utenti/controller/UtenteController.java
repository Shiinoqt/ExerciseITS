package com.spring.utenti.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.utenti.entity.Utente;
import com.spring.utenti.service.UtenteService;

@RestController
@RequestMapping(path="/utenti")
public class UtenteController {
    private final UtenteService service;

    public UtenteController(UtenteService service) {
        this.service = service;
    }
	
    @GetMapping(path="/registra", consumes = "application/json")
    public boolean registra(@RequestBody Utente utente) {
        return service.registra(utente);
    }
	
    @GetMapping(path="/cerca/{idUtente}", produces = "application/json")
    public Utente cercaPerId(@PathVariable int idUtente) {
        return service.cercaPerId(idUtente);
    }
	
    @GetMapping(path="/", produces = "application/json")
    public List<Utente> cerca() {
        return service.selectAll();
    }
    
    @GetMapping(path="/elimina/{idUtente}", produces = "application/json")
    public Utente elimina(@PathVariable int idUtente) {
    	return service.delete(idUtente);
    }
    
    @GetMapping(path="/aggiorna/{idUtente}", consumes = "application/json", produces = "application/json")
    public Utente aggiorna(@PathVariable int idUtente, @RequestBody Utente nuoviDati) {
        return service.aggiorna(idUtente, nuoviDati);
    }
}
