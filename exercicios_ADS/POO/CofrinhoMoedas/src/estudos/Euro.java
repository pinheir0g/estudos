package estudos;

public class Euro extends Moeda  {
	
	
	public Euro(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Euro: " + valor);
	}

	@Override
	public double converte() {
		return valor * 5.5;
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