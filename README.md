# Detector de Fadiga

O programa em Python tem como objetivo detectar fadiga em motoristas durante a condução, utilizando técnicas de visão computacional para monitorar o comportamento do motorista e identificar sinais de fadiga ou sonolência. Ao capturar o vídeo da face do motorista, é feita a detecção facial por meio da biblioteca OpenCV, e em seguida, são extraídas características faciais relevantes. O programa utiliza de um banco de dados treinado com exemplos de faces e seus aspectos, possibilitando a comparação das características extraídas e a classificação do estado atual do motorista. Quando prestes a adormecer, o programa emite um alarme sonoro para alertá-lo, reduzindo riscos de acidentes e contribuindo significativamente para a segurança viária

# Utilização

1) Primeiramente instale todas as bibliotecas necessárias que estão presentes no arquivo "FadigaDetector.py"

2) Baixe os seguintes arquivos e os coloque na mesma pasta: "BancoDeRostos", "FadigaDetector.py" e "alarm.mp3"

3) Você pode mudar o alarme para um áudio de sua preferência

4) Feito tudo isso, basta rodar o código

# Observações

1) Caso o código não esteja rodando, tente trocar o valor da variável "index_webcam". Mude para números de 1 para cima.

2) Este projeto é interessante para usar em conjunto com um Raspberry Pi, instalando-o de fato no seu carro.
   


   
