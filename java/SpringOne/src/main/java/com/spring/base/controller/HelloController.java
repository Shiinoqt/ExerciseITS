package com.spring.base.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path="/saluti")
public class HelloController {
	
	@GetMapping(path="/generici")
	public String HelloWorld() {
		return "Hello World";
	}
}
