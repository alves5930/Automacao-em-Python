Diogo Alves, Etec de Sapopemba - 27/04/2026

Use o XAMPP para importar o DB (127_0_0_1), e o comando abaixo se nao tiver ja tiver a biblioteca instalada. 
 Ative as opções Apache e MySql com o DB (127_0_0_1) importado no PhpMyAdmin, avisando que ocorreu um erro quando importou;

- Colocar a pasta system.alves (Automatacao-em-Python) no htdocs do XAMPP;
Então deve instalar o seguinte comando no diretorio (.../htdocs/system.alves) para a inicialização funcionar quando clicar no arquivo da pasta "iniciar.bat

pip install mysql-connector-python (EXECUTE COMO ADMINISTRADOR NO CMD)

Com isso feito, entre na pasta system.alves e inicie o "iniciar.bat". 

A ideia foi para que quando clicar no arquivo iniciar.bat funcione tudo dentro do terminal automaticamente. - Caso as dependencias estiverem funcionando na sua maquina, não havera problemas.
