package com.spring.business.service;

import com.spring.business.dto.CalcoloDTO;
import org.springframework.stereotype.Service;

@Service 
public class CalcoloServiceImpl implements CalcoloService {

    @Override
    public double calcola(CalcoloDTO calcolo) { 
        String op = calcolo.getOperazione().toLowerCase();
        double x = calcolo.getX();
        double y = calcolo.getY();

        return switch (op) {
            case "somma" -> sum(x, y); 
            case "sottrazione" -> subtract(x, y); 
            case "moltiplicazione" -> multiply(x, y); 
            case "divisione" -> divide(x, y);
            default -> throw new IllegalArgumentException("Operazione non supportata");
        };
    }

    public double sum(double a, double b) { 
    	return a + b; 
    }
    public double subtract(double a, double b) { 
    	return a - b; 
    }
    public double multiply(double a, double b) { 
    	return a * b;
    }

    public double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("Divisione per zero non permessa"); 
        }
        return a / b;
    }
}