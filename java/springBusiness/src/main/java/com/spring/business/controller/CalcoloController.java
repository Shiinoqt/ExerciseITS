package com.spring.business.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring.business.dto.CalcoloDTO;
import com.spring.business.service.CalcoloServiceImpl;

@RestController
@RequestMapping("/api/calcolatrice")
public class CalcoloController {

    @Autowired
    private CalcoloServiceImpl calcoloService;

    // @Autowired
    // private StatisticheService statsService;


    @PostMapping("/esegui")
    public ResponseEntity<Double> esegui(@RequestBody CalcoloDTO dto) {
        double risultato = calcoloService.calcola(dto);
        return ResponseEntity.ok(risultato);
    }

    // Endpoint per il report complessivo 
//    @GetMapping("/report")
//    public ResponseEntity<Map<String, Integer>> getReport() {
//        return ResponseEntity.ok(statsService.getReportComplessivo());
//    }
}