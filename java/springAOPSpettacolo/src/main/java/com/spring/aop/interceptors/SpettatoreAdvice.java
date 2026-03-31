package com.spring.aop.interceptors;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class SpettatoreAdvice {

	@Around("execution (* com.spring.aop.entity.Artista.perform(..))")
	public void filtro(ProceedingJoinPoint jp) {
		// pre-processing
		System.out.println("gli spettatori prendono posto");
		System.out.println("gli spettatori spengono i cellulari");
		long start = System.currentTimeMillis();
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		try {
			// chiamo il metodo target o il prossimo advice
			jp.proceed();
			
			// post- processing
			
			// lo show è terminato con successo
			System.out.println("applausi!!!!!!!!!!!!");
			long end = System.currentTimeMillis();
			System.out.println("lo show è durato " + (end - start) + " ms.");
			
			
		} catch (Throwable e) {
			// post-processing con errore
			System.out.println("c'è stato un problema, show interrotto");
		}
	}
	
}
