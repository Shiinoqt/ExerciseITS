package com.spring.business.dto;

public class CalcoloDTO {
	private double x;
	private double y;
	private String operazione;
	
	public CalcoloDTO () {}
	
	public CalcoloDTO (double x, double y, String operazione) {
		this.x = x;
		this.y = y;
		this.operazione = operazione;
	}

	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}

	public String getOperazione() {
		return operazione;
	}

	public void setOperazione(String operazione) {
		this.operazione = operazione;
	}
	

}
