package estudos;

public class Dolar extends Moeda {
	
	
	public Dolar(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Dolar: " + valor);
	}
	
	@Override
	public double converte() {
		return valor * 4.5;
	}

	@Override
	public int hashCode() {
		return super.hashCode();
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		return true;
	}
}