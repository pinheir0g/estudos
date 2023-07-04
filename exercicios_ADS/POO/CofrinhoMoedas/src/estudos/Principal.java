package estudos;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		/*
		 * Objetivo desse programa é simular um cofrinho de moedas utilizando conceitos de OO
		 * Principal foco é usar herança e polimorfismo e fornecer um menu para o usuário interagir.
		 * Usuário consegue ver, adicionar, remover e converter para real as moedas do cofrinho.
		 */
		
		Cofrinho c = new Cofrinho();
		
		Scanner teclado = new Scanner(System.in);
		int opcao;
		double tipoMoeda, valor;
		Moeda moeda;
		
		menuOpcao();
		opcao = teclado.nextInt();
		
		// Loop para exibir o menu.
		while (opcao != 0) {
			
			switch (opcao) {
			
			case 1:
				tipoMoeda = 0;
				// Loop para permitir apenas opções existentes no menu.
				while (tipoMoeda > 3 || tipoMoeda <= 0) {
					menuMoeda();
					tipoMoeda = teclado.nextDouble();
				}
				
				System.out.println("Digite o valor: ");
				valor = teclado.nextDouble();
				
				moeda = null;
				
				// Verificação do tipo de moeda e criação de uma nova moeda do tipo e valor definido.
				if (tipoMoeda == 1) {
					moeda = new Real(valor);
					
				}
				else if (tipoMoeda == 2) {
					moeda = new Euro(valor);
					
				}
				else if (tipoMoeda == 3) {
					moeda = new Dolar(valor);
				}
					
				
				// adicionando a moeda no cofrinho.
				c.adicionar(moeda);
				break;
				
			case 2:
				tipoMoeda = 0;
				// Loop para permitir apenas opções existentes no menu.
				while (tipoMoeda > 3 || tipoMoeda <= 0) {
					menuMoeda();
					tipoMoeda = teclado.nextDouble();
				}
				
				System.out.println("Digite o valor: ");
				valor = teclado.nextDouble();
				
				moeda = null;
				
				// Verificação do tipo de moeda e criação de uma nova moeda do tipo e valor definido.
				if (tipoMoeda == 1) {
					moeda = new Real(valor);
					
				}
				else if (tipoMoeda == 2) {
					moeda = new Euro(valor);
				
				}
				else if (tipoMoeda == 3) {
					moeda = new Dolar(valor);
				}
				
				// Removendo moeda do cofrinho.
				c.remover(moeda);
				
				break;
				
			case 3:
				c.listagemMoedas();
				break;
				
			case 4:
				c.totalConvertido();
				break;
				
			default:
				System.out.println("Opção Inválida");
				break;
			}
			menuOpcao();
			opcao = teclado.nextInt();
			
		}
		System.out.println("Encerrando!");
		teclado.close();
	}
	
	// Foram criadas 2 funções para exibir os menus desejados e evitar repetição de código.
	
	// Menu de opções para selecionar a moeda.
	public static void menuMoeda() {
		System.out.println("-------------------");
		System.out.println("Escolha a moeda: ");
		System.out.println("1 - Real: ");
		System.out.println("2 - Euro: ");
		System.out.println("3 - Dolar: ");
		
	}
	// Menu de opções para selecionar a ação.
	public static void menuOpcao() {
		System.out.println("-------------------");
		System.out.println("COFRINHO");
		System.out.println("-------------------");
		System.out.println("1 - Adicionar Moeda");
		System.out.println("2 - Remover Moeda");
		System.out.println("3 - Listar Moedas");
		System.out.println("4 - Calcular total convertido para Real");
		System.out.println("0 - Encerrar");
		System.out.println("-------------------");
		
	}
}