# **WB-Datadict Mod**
Modificação estética e funcional do plugin para MySQL Workbench "Wb Datadict".


### **Motivação:**

Foi proposto à equipe encontrar uma forma de criar um dicionário de dados através do MySQL Workbench. Primeiro pesquisamos dentro do programa e identificamos uma maneira de exportar as tabelas, a qual não se enquadrava no formato do dicionário de dados. Após pesquisa, encontramos <a href="https://gitlab.com/luis-felipe/wb-datadict">um plugin</a> que consegue executar corretamente essa função, entretanto estava datado, então realizamos algumas modificações.


<!-- ### **Plugin Original:**

Observamos que o plugin original não supria os requisitos propostos, pois as tabelas estavam desorganizadas, o campo de comentário não era editável, o índice era de difícil leitura e a compreensão do banco era complexa devido à grande extensão da página.


### **Modificações:**

I) Tradução para português;

II) Estilização da página;

III) Organização das tabelas;

IV) Habilitar a edição das descrições (comentários);

V) Adição de menus "Dropdown" e formatação do índice.
 -->

### **Estilização da página**

O visual e disposição de elementos do dicionário gerado pelo plugin original eram distorcidas e traziam certa dificuldade ao ato de visualizar múltiplas tabelas de um determinado banco de dados. Portanto, optamos por modificar o visual do template padrão e produzir uma nova interface que nos agradasse mais.

<div align="center">
  
**Figura 1** - Página gerada pelo plugin original. 

![image](https://user-images.githubusercontent.com/84246094/134051416-7b7e600d-c7bb-483d-a86e-8cedb1461431.png)

**Figura 2** - Página gerada pelo mod.
  
![image](https://user-images.githubusercontent.com/84246094/136258715-9dbc1af1-b3c5-4bd8-9973-9245b5f515ca.png)

</div>


### **Organização das tabelas**

Algumas das colunas presentes nas tabelas geradas continham informações que raramente são referidas dessa forma (no ambiente de trabalho onde nos encontramos pelo menos) e que certamente seriam documentadas na descrição se um dia fossem, tornando-as de certa forma redundantes. Entretanto, apenas removê-las não é a solução mais elegante, então estudamos a possibilidade de adicionar e excluir estas colunas de forma dinâmica no futuro.

<div align="center">

**Figura 3 -** Tabela gerada pelo plugin original.
  
![image](https://user-images.githubusercontent.com/84246094/134051824-0254e966-2699-416b-a01c-775e24c04127.png)

**Figura 4** - Tabela gerada pelo mod. 
  
![image](https://user-images.githubusercontent.com/84246094/136258887-c7276d1e-40e2-46e9-8015-583d36ef28bc.png)
  
</div>


### **Habilitar a edição das descrições (comentários)**

Anteriormente não era possível editar ou corrigir os comentários extraídos de cada coluna depois que o documento fosse gerado. Esse fator provavelmente visa evitar assincronia entre o dicionário de dados e o schema do banco, porém, torna muito mais laboriosa qualquer alteração que se fizer necessária.

<div align="center">

**Figura 5** - Coluna de comentário gerada pelo plugin original (estático).

![image](https://user-images.githubusercontent.com/84246094/134052404-ba7e2911-b8a8-492b-9c47-3f0c104b2d16.png)

**Figura 6** - Coluna de descrição gerada pelo mod (editável).

![image](https://user-images.githubusercontent.com/84246094/136259297-c24c5708-65a6-4161-bd25-0b86d12a633e.png)
  
</div> 


### **Adição de menus "Dropdown" e formatação do índice**

Para facilitar a visualização e apresentação dos elementos do dicionário, adicionamos menus minimizáveis aos mesmos e definimos uma formatação diferente para o índice.

<div align="center">
  
**Figura 7** - Menus gerados pelo mod.

![image](https://user-images.githubusercontent.com/84246094/136259500-0ed70057-b8d3-44e8-9cdd-0e96c2b35d42.png)

</div>  


### **Instalação:**

- Baixar o arquivo <a href="https://github.com/Iah-Uch/WB-DataDict-Mod/blob/main/DataDict-Mod.py">DataDict-Mod.py</a> para o tema claro ou <a href="https://github.com/Iah-Uch/DataDict-Mod/blob/main/DataDict-Mod-DT.py">DataDict-Mod-DT.py</a> para o tema escuro;
- Ao abrir o MySQL Workbench navegue até **Scripting → Install Plugin/Module…** e selecione o arquivo do plugin modificado.

<div align="center">
  
![image](https://user-images.githubusercontent.com/84246094/134054621-f3ad05f7-f5a8-4474-b9d8-ce8c9133ecf8.png)

</div>    
  
  
### **Criando o Dicionário de Dados:**

- Abra o schema do banco de dados desejado; navegue até **Tools → Catalog → Gerar Dicionário de Dados** e salve o arquivo com extensão **".html"**.

<div align="center"> 
  
![image](https://user-images.githubusercontent.com/84246094/136260519-c87e92ac-700c-4553-b240-7b964cf2d692.png)

</div>    


### **Contribuintes:**
- <a href="https://github.com/oguialmeida">Guilherme Gomes</a>
- <a href="https://github.com/Iah-Uch">Iãh Uchôa</a>
- <a href="https://github.com/JP-Barbaresco">João Pedro Barbaresco</a>
- <a href="https://github.com/LucasEvanglg">LucasEvanglg</a>


### **Tecnologias utilizadas:**

- Python;
- HTML;
- Javascript;
- MySQL Workbench Plugin Library;
