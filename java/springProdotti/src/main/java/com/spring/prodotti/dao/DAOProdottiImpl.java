package com.spring.prodotti.dao;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.spring.prodotti.entity.Prodotto;

@Repository
public class DAOProdottiImpl implements DAOProdotti {
	
	private Map<Integer, Prodotto> mappa = new HashMap<Integer, Prodotto>();

	@Override
	public void insert(Prodotto prodotto) {
		if (mappa.containsKey(prodotto.getId())) {
			throw new RuntimeException("Id già presente");
		} else {
			mappa.put(prodotto.getId(), prodotto);
		}
	}

	@Override
	public Prodotto selectById(int id) {
		Prodotto prodotto = mappa.get(id);
		if(prodotto == null) throw new RuntimeException("id inesistente");
		else
			return prodotto;
	}

}
