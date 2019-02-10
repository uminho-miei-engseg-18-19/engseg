<?php
// genSharedSecret <segredo> <num de entidades a partilhar>

if ($argc != 3) {
  print "Utilização: php genSharedSecret <segredo> <num de entidades a partilhar>\n";
  exit;
}

// transforma a string de entrada numa string em binário, caracter a caracter
$txt_str = $argv[1];
$len = STRLEN($txt_str); 
$bin = ''; 
FOR($i = 0; $i < $len; $i++ ) 
{ 
  $bin .= STRLEN(DECBIN(ORD($txt_str[$i]))) < 8 ? STR_PAD(DECBIN(ORD($txt_str[$i])), 8, 0, STR_PAD_LEFT) : DECBIN(ORD($txt_str[$i])); 
} 

// print "Segredo em binário: $bin \n";

// Gera n codigos que permitem, quando todos juntos, gerar o segredo inicial
//     n = <num de entidades a partilhar>
$characters = '01';
$length = strlen($bin);
$charactersLength = strlen($characters);
for ($n = 0; $n < $argv[2] - 1; $n++) {
  $randomString = '';
  for ($i = 0; $i < $length; $i++) {
      $randomString .= $characters[rand(0, $charactersLength - 1)];
  }
  $codigos[$n] = $randomString;

  print "Codigo $n: $randomString \n";
}

$xor = $bin;
for ($n = 0; $n < $argv[2] - 1; $n++) {
  for ($i = 0; $i < $length; $i++) {  
	$xor[$i] = intval($xor[$i]) ^ intval($codigos[$n][$i]);
  }
}

print "Codigo $argv[2]: $xor \n";



?>
