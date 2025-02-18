<h1>Duepay App</h1>

<h2>Descrição</h2>
<p>Aplicativo desenvolvido para auxiliar no recolhimento das notas fiscais para o portal do Duepay - aplicativo para compra de material escolar - extraindo CPF, chave de acesso, data e o valor da compra.</p>

<h2>Funcionamento</h2>

<h3>Entrada de Dados</h3>
<p>Para entrada de dados são necessário dois arquivos que serão direcionados para os seguintes diretórios:</p>
<ul>
  <li>src/input/duepay</li>
  <li>src/input/vendas</li>
</ul>
<h4>Pasta duepay</h4>
<p>Na pasta "duepay" será necessário pegar a planilha indo no portal do duepay para credenciados e realizar a exportação em excel.</p>
<p>Após o download será necessário exporta a planilha em formato .csv (separado por ,). Por fim salve o arquivo na pasta duepay.</p>

<h4>Pasta vendas</h4>
<p>Na pasta "vendas" é um arquivo .zip contendo os xml das vendas.</p>
<p><strong>IMPORTANTE: Para os XMLs será necessário conter os seguintes requisitos:</strong></p>
<ul>
  <li>&lt;cpf&gt; - para capturar o CPF</li>
  <li>&lt;dEmi&gt; - para capturar a Data</li>
  <li>&lt;infCFe&gt; id= chave de acesso - para capturar a Chave da Nota Fiscal</li>
  <li>&lt;vCFe&gt; - para capturar o valor Total da Compra</li>
</ul>

<h4>Iniciando o App</h4>

<p>Com todos os preperativos prontos execute o arquivo Main.py encontrado no seguinte diretório:</p>

<ul>
  <li>src/main.py</li>
</ul>

<p>O App possui duas funções, sendo:</p>

<ul>
  <li>Gerar planilha Duepay</li>
  <li>Realizar pesquisa</li>  
</ul>

<p>A 1° opção realizará um arquivo excel contendo a Data, CPF, Chave de Acesso e o Valor Total de cada arquivo XML</p>
<p>A 2° opção realizará uma pesquisa por CPF ou pelo valor da Nota. (Atenção na formatação dos dados)</p>

<h3>Saida de Dados</h3>
<p>Para verificar o excel gerado o app realizará uma exportação em excel para a pasta no seguinte diretório:</p>
<ul>
  <li>src/output/Duepay_Final.xlsx</li>
</ul>
