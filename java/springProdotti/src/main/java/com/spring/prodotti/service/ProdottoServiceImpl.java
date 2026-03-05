package com.spring.prodotti.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.spring.prodotti.dao.DAOProdotti;
import com.spring.prodotti.dto.ProdottoDTO;
import com.spring.prodotti.entity.Prodotto;
import com.spring.prodotti.mapper.Mapper;

@Service
public class ProdottoServiceImpl implements ProdottoService {
	
	@Autowired
	private DAOProdotti dao;

	@Override
	public void carica(ProdottoDTO dto) {
		Prodotto prodotto = Mapper.daDTOAEntity(dto);
		dao.insert(prodotto);
	}

	@Override
	public ProdottoDTO cercaPerId(int id) {
		Prodotto trovato = dao.selectById(id);
		return Mapper.daEntityADTO(trovato);
	}

}
