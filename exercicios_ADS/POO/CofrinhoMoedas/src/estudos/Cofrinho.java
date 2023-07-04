package estudos;

import java.util.ArrayList;

public class Cofrinho {
	private ArrayList<Moeda> listaMoedas = new ArrayList<Moeda>();
	
	public void adicionar(Moeda moeda) {
		listaMoedas.add(moeda);
	}
	
	public void remover(Moeda moeda) {
		listaMoedas.remove(moeda);
	}
	
	public void listagemMoedas() {
		for (Moeda m : listaMoedas) {
			m.info();
		}
	}
	
	public void totalConvertido() {
		double total = 0;
		for (Moeda m : listaMoedas) {
			total += m.converte();
		}
		System.out.println("Total convertido em real: " + total);
	}
}