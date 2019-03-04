# Máquina Virtual

**Nota**: À medida que o semestre for decorrendo, poderá ser adicionado software à máquina virtual, pelo que terão de ir fazendo update da mesma. Desse modo, será melhor guardarem os vossos trabalhos no exterior da máquina virtual, podendo para isso recorrer à diretoria partilhada com o sistema *host*.

A máquina virtual disponibilizada (Debian 9.7 Stretch 64 bits) tem os seguintes utilizadores/password:
+ root / root
+ user / user

O utilizador *user* tem privilégios sudo, devendo utilizar este utilizador para efetuar as fichas de trabalho das aulas TP.

Esta VM usa  o *MATE  Desktop Environment*. Tem instalado as seguintes packages e aplicações que deverão ser necessárias durante este semestre:
+ eVotUM Cripto-py
+ Oracle JDK 9
+ Python 2 e 3
+ PHP 7
+ openssl
+ IDE PyCharm community
+ IDE atom
+ tor
+ secure-delete
+ curl
+ torbrowser-launcher
+ gdb
+ docker
+ WebGoat (sobre docker)

Adicionalmente, no utilizador user, na diretoria Tools, estão instalados:
+ ssh-audit (https://github.com/arthepsy/ssh-audit)
+ kali-anonsurf (https://github.com/Und3rf10w/kali-anonsurf.git)
+ GDB-Peda (https://github.com/longld/peda.git)

Pode fazer download do ficheiro **.ova** da máquina virtual em https://meocloud.pt/link/f188f15b-7145-4e11-b59e-6a64f61084a6/CSI.EngSeg.ova/ .

## Instalação da VM

  1. Instale  a última versão do OracleVM VirtualBox incluindo o  Extention Pack
  2. descarregue o ficheiro .ova
  3. Importe esse ficheiro no Virtual Box; menu   `File >> Import Appliance`
  4. No comando `Start`  faça o `boot` da máquina.
