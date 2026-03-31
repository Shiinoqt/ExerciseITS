package com.spring.aop.interceptors;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class SupporterAdvice {

	@Before("execution (* com.spring.aop.entity.Artista.perform(..))")
	public void filtro() {

		System.out.println("parte lo show della band di supporto in attesa dello show principale");
		
		long start = System.currentTimeMillis();
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("applausi alla band di supporto !!!!!!!!!!!!");
		long end = System.currentTimeMillis();
		System.out.println("lo show di supporto è durato " + (end - start) + " ms.");
			
			
	}
	
}
