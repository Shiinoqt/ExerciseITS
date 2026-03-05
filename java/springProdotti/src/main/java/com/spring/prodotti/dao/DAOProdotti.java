package com.spring.prodotti.dao;

import com.spring.prodotti.entity.Prodotto;

public interface DAOProdotti {
	public void insert(Prodotto prodotto);
	public Prodotto selectById(int id);
	
}
