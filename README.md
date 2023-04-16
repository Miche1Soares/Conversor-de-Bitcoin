#  Conversor de Bitcoin

Este projeto teve como objetivo criar um conversor de moedas fiduciárias para o Bitcoin, em que haveria uma interface prática e intuitiva.

##  Tecnologias utilizadas:

1. Front-End:

- HTML5

- CSS3

- Framework Bootstrap

2. Back-End:

- Python + Flask

---

###  Página Inicial

A página inicial é constituída por:

- Uma caixa contendo a cotação do Bitcoin naquele instante em dólar, euro e real, respectivamente.

- Uma caixa com opções de seleção das moedas fiduciárias. Há, de fácil acesso, as seleções do dólar, euro ou real como também um campo onde pode ser inserido o código ISO 4217 de outra moeda desejada.

- Dois campos em que deve-se inserir a quantidade de moeda fiduciária ou Bitcoin a ser convertida.

Ao selecionar a moeda fiduciária e inserir a quantidade de conversão, pressionando o botão de Calcular, será apresentado o resultado da operação.

![fiat-bitcoin-edit](https://user-images.githubusercontent.com/80423723/232345104-093bc1c5-8d28-4a4c-bc41-7b15ae3b1fc1.gif)

Pode-se também inserir a quantidade de bitcoin a ser convertida em alguma moeda fiduciária.

![bitcoin-fiat-edit](https://user-images.githubusercontent.com/80423723/232345210-da1058ee-1f01-4ac5-818b-eb58cacef731.gif)

Ademais, a conversão usando uma moeda fiduciária qualquer, inserindo o seu respectivo código ISO 4217

![fiat-personalizada-edit](https://user-images.githubusercontent.com/80423723/232345242-037dff87-7da3-4ff4-a9f4-ddd3acd3d961.gif)

As consultas às cotações são realizadas pela API da https://www.coinapi.io/
