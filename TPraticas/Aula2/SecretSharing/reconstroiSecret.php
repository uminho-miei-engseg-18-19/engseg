<?php
// reconstroiSecret <codigo(s)>

if ($argc < 2) {
  print "Utilização: php reconstroiSecret <codigo(s)>\n";
  exit;
}

// XOR de todos os elementos de entrada
$xor = $argv[1];
$length = strlen($xor);
for ($n = 2; $n < $argc; $n++) {
  for ($i = 0; $i < $length; $i++) {
        $xor[$i] = intval($xor[$i]) ^ intval($argv[$n][$i]);
  }
}

$bin_str = $xor;
$chars = EXPLODE("\n", CHUNK_SPLIT(STR_REPLACE("\n", '', $bin_str), 8));
$_I = COUNT($chars);
$text_str = "";
FOR($i = 0; $i < $_I; $text_str .= CHR(BINDEC($chars[$i])), $i++  );

print "Segredo: $text_str \n"

?>
