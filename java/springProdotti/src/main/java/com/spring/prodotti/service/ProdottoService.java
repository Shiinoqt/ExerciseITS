package com.spring.prodotti.service;

import com.spring.prodotti.dto.ProdottoDTO;

public interface ProdottoService {
	
	public void carica(ProdottoDTO prodotto);
	public ProdottoDTO cercaPerId(int id);
}
