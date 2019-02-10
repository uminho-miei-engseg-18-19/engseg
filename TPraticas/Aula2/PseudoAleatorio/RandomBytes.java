
import java.security.SecureRandom;

// gera numero de bytes aleatorios
// RandomBytes <numero de Bytes>
public class RandomBytes {
    public static void main(String[] args) throws Exception {
        if (args.length != 1) { // valida que foi fornecido um argumento
            mensagemUso();
            System.exit(1);
        }
		
        /* Passo 1: Inicializar o Secure Random Generator */
        // Neste caso utiliza-se o algoritmo NativePRNG, que obtém números aleatórios com base no sistema operativo
        SecureRandom secureRandom = SecureRandom.getInstance("NativePRNG");
        
        /* Passo 2: método nextBytes gera número de bytes (do tamanho do array de bytes) random */
        byte[] bytes = new byte[Integer.parseInt(args[0])];
        secureRandom.nextBytes(bytes);
        
        // Imprime os bytes
        System.out.write(bytes);
        
    } 
	
	public static void mensagemUso() {
		System.out.println("RandomBytes - gera bytes aleatórios");
                System.out.println("Para obter o resultado noutro formato (por exemplo base64), adicionar | openssl enc -base64");
		System.out.println("\tSintaxe: java RandomBytes <numero de bytes>");
		System.out.println();
	}

}
