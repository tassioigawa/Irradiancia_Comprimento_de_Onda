# Irradiância (Comprimento de Onda)

O script seguiu a metodologia a seguir:
O cálculo de Irradiância no topo da atmosfera (TOA) foi realizado baseado na relação posicional estimada da Terra em relação ao Sol durante a coleta das amostras. Segundo Lorenzetti (2015), a irradiância extraterrestre para uma determinada superfície horizontal (Irradiância), na qual a normal vertical faça com o a direção do Sol um ângulo zenital é fornecida pela equação:
Irradiância no Topo da Atmosfera: 

Irradiância = Es∙E0∙cosθZ = Es∙E0∙(senδ∙senϕ+cosδcosϕ∙cosω)	(1)

Em que declinação magnética (δ) foi quantificada com base na equação expressa a seguir (IQBAL, 1983, p.7):

δ=(0,006918-0,399912 cos⁡Γ+ 0,070257 sen Γ
-0,006758 cos⁡2Γ+0,000907 sen 2Γ-0,002697 cos⁡3Γ       (2)
+0,00148 sen⁡3Γ)	                      

Em que Γ é o ângulo dia que obtido com o uso da fórmula (LORENZETTI, 2015, p.34):

Γ(rad)=2π(dn-1)/365	(3)

Dessa forma, para se calcular o horário solar foi necessário obter o valor do Horário Local Aparente utilizou-se a fórmula (IQBAL, 1983, p.13):

Horário Local Aparente = horário padrão local + 4(Ls - Lc) + Et	(4)

considerando que Ls é a longitude padrão e Lc é a longitude local, Et que é a equação do tempo. Nesse sentido, a Et foi calculada com base na seguinte fórmula (IQBAL, 1983, p.11):

Et = (0,000075 +0,001868 cos⁡Γ-0,032077 sen Γ 
- 0,014615 cos⁡2Γ-0,04089 sen 2Γ)(229,18)	(5)
 
Dessa forma, o ângulo horário solar foi obtido para ser implementado na equação da Irradiância do Topo da Atmosfera (Equação 1), conforme a seguinte equação (LORENZETTI, 2015, p.347):

ⅆω=(π/12)ⅆt	(6)

Por fim, os dados obtidos em campo foram utilizados como dados entrada para o cálculo da Irradiação do Topo da Atmosfera no momento inicial e final que as medidas foram tomadas em campo. A Irradiância por comprimento de onda foi medida com base nos dados obtidos no American Society for Testing and Materials (link de acesso: https://www.nrel.gov/grid/solar-resource/spectra-astm-e490.html)

Referências Bibliográficas

IQBAL, M. An Introduction to Solar Radiation. Ontario: Academic Press Canada, 1983. 390p. 

LORENZZETTI, J. A. Princípios físicos de sensoriamento remoto. São Paulo: Blucher, 2015.
