import streamlit as st
### colocar um titulo
# st.title("imune ao conhecimento")
# ### escreve
# st.write("testando... esquerda ou direita")
# ### cria uma barra lateral
# st.sidebar.title("barra lateral")

###criando a lista
# nomes ficticios,qualquer semelhança é conhecidencia

# nomes = ["eshillyn","joão","keita","cacau"]
# # ## cria a caixinha na barra lateral
# st.sidebar.selectbox("escolhe um nome:",nomes)

# ## COLOCA O VIDEO NA PAGINA DO SITE
# st.video("https://www.youtube.com/watch?v=ec12XRzMH28")


st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolha o carro ideal para você!")
carros = ["gol", "BMW", "corsa", "jeep"]
opçao = st.sidebar.selectbox("selecione o modelo do carro :",carros)



st.title("cris automovel - aluguel de carros")

st.image(f"{opçao}.png")
st.markdown(f"##voce alugou o modelo : {opçao}")
st.markdown("---")

dias = st.text_input(f"por quantos dias o {opçao} foi alugado?")
km = st.text_input(f"quantos km voce rodou com o {opçao}?")


if opçao == "BMW":
    diaria = 550

elif opçao == "corsa":
    diaria = 450

elif opçao == "gol":
    diaria = 250

elif opçao == "jeep":
    diaria = 500

if st.button("calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km *0.15
    aluguel_total = total_dias+total_km

    st.warning(f"voce alugou o {opçao} por  {dias} dias e rodou {km}km. O valor total a pagar é r${aluguel_total:.2f}")        
