package com.spring.prodotti.mapper;

import com.spring.prodotti.dto.ProdottoDTO;
import com.spring.prodotti.entity.Prodotto;

public class Mapper {
	public static Prodotto daDTOAEntity(ProdottoDTO dto) {
		return new Prodotto(dto.getId(), dto.getDescrizione());
	}
	public static ProdottoDTO daEntityADTO(Prodotto entity) {
		return new ProdottoDTO(entity.getId(), entity.getDescrizione());
	}
}
