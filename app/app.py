import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def pagina_1():
    st.write("## Bienvenidos al sitio de modelos ML")
    st.write("Este sitio web fue creado para presentar algunos modelos de aprendizaje")
    st.write("máquina que se han entrenado previamente con un conjunto de datos.")
    st.write(" ")
    st.write(" ")
    st.write("En particular, para este sitio se han utilizado datos relacionados a ")
    st.write("tecnologías de la información, buscando predecir ciertas variables.")
    st.write(" ")
    st.write(" ")
    st.write("En la página web podrás encontrar tres modelos distintos que utilizan diferentes")
    st.write("técnicas de aprendizaje supervisado como: ")
    st.write("**- Regresión logística**")
    st.write("**- Teorema de Bayes**")
    st.write("**- Regresión lineal**")
    st.write("")
    
    
        

def pagina_2():
    st.write("### Modelo de Regresión Logística")
    st.write("#### Predicción de necesidad de conexión a internet ")
    
    with open('rLog(internet).pkl', 'rb') as f:
        modelo = pickle.load(f)


        # Define una función que tome las variables de entrada del usuario, las transforme en el formato adecuado y le pase el modelo:


        def predecir_inversion(uso_mail,computador_cant, pda_cant, celular_cant, notebooks_cant, tablet_cant,
                               pag_web, uso_celular, uso_r_sociales, especialistas_tic, per_conocimiento_tic, 
                               intranet):
            caracteristicas = pd.DataFrame({'Computador_cant': [computador_cant],
                                            'Pda_cant': [pda_cant],
                                            'Celular_cant': [celular_cant],
                                            'Notebooks_cant': [notebooks_cant],
                                            'Tablet_cant': [tablet_cant],
                                            'Pag_Web': [pag_web],
                                            'Uso_Celular': [uso_celular],
                                            'Uso_Email': [uso_mail],
                                            'Uso_R_Sociales': [uso_r_sociales],
                                            'Especialistas_tic': [especialistas_tic],
                                            'Personal_Conocimiento_tic':[per_conocimiento_tic],
                                            'Intranet': [intranet]})
            
            prediccion = modelo.predict(caracteristicas)
            return prediccion[0]


        # En la función principal, define los campos del formulario con la función 
        # `st.sidebar`, para que aparezcan en la barra lateral. 
        # Asegúrate de especificar el tipo de entrada y los valores predeterminados


        computador_cant = st.number_input('Cuantas  computadores tiene', min_value=0, max_value=1000000, value=0)
        pda_cant = st.number_input('Cuantas  PDA tiene', min_value=0, max_value=1000000, value=0)
        celular_cant = st.number_input('Cuantas celulares tiene', min_value=0, max_value=1000000, value=0)
        notebooks_cant = st.number_input('Cuantas notebooks tiene', min_value=0, max_value=1000000, value=0)
        tablet_cant = st.number_input('Cuantas tablets tiene', min_value=0, max_value=1000000, value=0)
        pag_web = st.checkbox('Tiene Páginas Web', value=False)
        uso_celular = st.checkbox('Uso de celular',value=False)
        uso_mail = st.checkbox('Uso de email',value=False)
        uso_r_sociales = st.checkbox('Uso de redes sociales',value=False)
        especialistas_tic = st.checkbox('Hay especialistas en TIC', value=False)
        per_conocimiento_tic = st.number_input('Cuantas personas con conocimientos en Tic hay', min_value=0, max_value=1000000, value=0)
        intranet = st.checkbox('Intranet', value=False)
        
        st.write("  ")
        st.write("  ")
    
        # Lamamos a la función 'inversion' con las variables de entrada del usuario y muestra el resultado en la página:
        prediccion = predecir_inversion(uso_mail,computador_cant, pda_cant, celular_cant, notebooks_cant, tablet_cant,
                               pag_web, uso_celular, uso_r_sociales, especialistas_tic, per_conocimiento_tic, 
                               intranet)

        
 
        # Crea el botón para llamar a la función en una ventana emergente
        
        if st.button("RESULTADO"):
           
           if prediccion == 0:
               st.write("Dada las actividades y caracteristicas de los equipos")
               st.write("No es necesario el Internet")
           else:  
               st.write("El Internet es una herramienta necesaria. ")




def pagina_3():
    st.write("### Modelo de Algoritmo Bayesiano")
    st.write("#### Predicción de contar con un empleado especialista en TIC's")
    
    with open('baye(especialista).pkl', 'rb') as f:
        modelo = pickle.load(f)


        # Define una función que tome las variables de entrada del usuario, las transforme en el formato adecuado y le pase el modelo:


        def predecir_inversion(ba_fija,ba_movil,inv_tic,uso_mail,computador_cant, pda_cant,
                               celular_cant, notebooks_cant, tablet_cant,
                               pag_web, uso_celular, uso_r_sociales, intranet):
            caracteristicas = pd.DataFrame({'Inversion_Tic': [inv_tic],
                                            'Computador_cant': [computador_cant],
                                            'Pda_cant': [pda_cant],
                                            'Celular_cant': [celular_cant],
                                            'Notebooks_cant': [notebooks_cant],
                                            'Tablet_cant': [tablet_cant],
                                            'Internet_ba_Fija': [ba_fija],
                                            'Internet_ba_Movil': [ba_movil],
                                            'Pag_Web': [pag_web],
                                            'Uso_Celular': [uso_celular],
                                            'Uso_Email': [uso_mail],
                                            'Uso_R_Sociales': [uso_r_sociales],
                                            'Intranet': [intranet]})
            
            prediccion = modelo.predict(caracteristicas)
            return prediccion[0]


        # En la función principal, define los campos del formulario con la función 
        # `st.sidebar`, para que aparezcan en la barra lateral. 
        # Asegúrate de especificar el tipo de entrada y los valores predeterminados


        inv_tic = st.checkbox('Hizo inversiones en TICs', value=False)
        computador_cant = st.number_input('Cuantas  computadores tiene', min_value=0, max_value=1000000, value=0)
        pda_cant = st.number_input('Cuantas  PDA tiene', min_value=0, max_value=1000000, value=0)
        celular_cant = st.number_input('Cuantas celulares tiene', min_value=0, max_value=1000000, value=0)
        notebooks_cant = st.number_input('Cuantas notebooks tiene', min_value=0, max_value=1000000, value=0)
        tablet_cant = st.number_input('Cuantas tablets tiene', min_value=0, max_value=1000000, value=0)
        ba_fija = st.checkbox('Tiene banda ancha fija', value=False)
        ba_movil = st.checkbox('Tiene banda ancha movil', value=False)
        pag_web = st.checkbox('Tiene Páginas Web', value=False)
        uso_celular = st.checkbox('Uso de celular',value=False)
        uso_mail = st.checkbox('Uso de email',value=False)
        uso_r_sociales = st.checkbox('Uso de redes sociales',value=False)
        intranet = st.checkbox('Intranet', value=False)
        
        st.write("  ")
        st.write("  ")
    
        # Lamamos a la función 'inversion' con las variables de entrada del usuario y muestra el resultado en la página:
        prediccion = predecir_inversion(ba_fija,ba_movil,inv_tic,uso_mail,computador_cant, pda_cant,
                               celular_cant, notebooks_cant, tablet_cant,
                               pag_web, uso_celular, uso_r_sociales, intranet)

        
 
        # Crea el botón para llamar a la función en una ventana emergente
        
        if st.button("RESULTADO"):
        
           if prediccion == 0:
               st.write("Dada las actividades y segun las herramientas que dispone")
               st.write("No necesita Especialistas en TIC's")
           else:  
               st.write("La empresa deberia contar con un Especialistas en TIC's")



def pagina_4():
    st.write("### Modelo de Regresión Lineal")
    st.write("#### Predicción del valor de Inversion en TIC's")
    
    with open('rLineal(Valor_inv).pkl', 'rb') as f:
        modelo = pickle.load(f)


        # Define una función que tome las variables de entrada del usuario, las transforme en el formato adecuado y le pase el modelo:


        def predecir_inversion(uso_mail,computador_cant, pda_cant, celular_cant, notebooks_cant, tablet_cant,
                               pag_web, uso_celular, uso_r_sociales, especialistas_tic,  
                               intranet,ba_fija,ba_movil,per_uso_inter,m_tic,h_tic):
            caracteristicas = pd.DataFrame({'Computador_cant': [computador_cant],
                                            'Pda_cant': [pda_cant],
                                            'Celular_cant': [celular_cant],
                                            'Notebooks_cant': [notebooks_cant],
                                            'Tablet_cant': [tablet_cant],
                                            'Personal_q_uso_Internet': [per_uso_inter],
                                            'Internet_ba_Fija': [ba_fija],
                                            'Internet_ba_Movil': [ba_movil],
                                            'Pag_Web': [pag_web],
                                            'Uso_Celular': [uso_celular],
                                            'Uso_Email': [uso_mail],
                                            'Uso_R_Sociales': [uso_r_sociales],
                                            'Especialistas_tic': [especialistas_tic],
                                            'Mujeres_Conocimiento_tic':[m_tic],
                                            'Hombres_Conocimiento_tic':[h_tic],
                                            'Intranet': [intranet]})
            
            prediccion = modelo.predict(caracteristicas)
            return prediccion[0]


        # En la función principal, define los campos del formulario con la función 
        # `st.sidebar`, para que aparezcan en la barra lateral. 
        # Asegúrate de especificar el tipo de entrada y los valores predeterminados


        computador_cant = st.number_input('Cuantas  computadores tiene', min_value=0, max_value=1000000, value=0)
        pda_cant = st.number_input('Cuantas  PDA tiene', min_value=0, max_value=1000000, value=0)
        celular_cant = st.number_input('Cuantas celulares tiene', min_value=0, max_value=1000000, value=0)
        notebooks_cant = st.number_input('Cuantas notebooks tiene', min_value=0, max_value=1000000, value=0)
        tablet_cant = st.number_input('Cuantas tablets tiene', min_value=0, max_value=1000000, value=0)
        per_uso_inter = st.number_input('Cuantas personas usan internet', min_value=0, max_value=1000000, value=0)
        ba_fija = st.checkbox('Tiene banda ancha fija', value=False)
        ba_movil = st.checkbox('Tiene banda ancha movil', value=False)
        pag_web = st.checkbox('Tiene Páginas Web', value=False)
        uso_celular = st.checkbox('Uso de celular',value=False)
        uso_mail = st.checkbox('Uso de email',value=False)
        uso_r_sociales = st.checkbox('Uso de redes sociales',value=False)
        especialistas_tic = st.checkbox('Hay especialistas en TIC', value=False)
        m_tic = st.number_input('Cuantas mujeres con conocimientos en Tic hay', min_value=0, max_value=1000000, value=0)
        h_tic = st.number_input('Cuantas hombres con conocimientos en Tic hay', min_value=0, max_value=1000000, value=0)
        intranet = st.checkbox('Intranet', value=False)
        
        st.write("  ")
        st.write("  ")
    
        # Lamamos a la función 'inversion' con las variables de entrada del usuario y muestra el resultado en la página:
        prediccion = predecir_inversion(uso_mail,computador_cant, pda_cant, celular_cant, notebooks_cant, tablet_cant,
                               pag_web, uso_celular, uso_r_sociales, especialistas_tic,  
                               intranet,ba_fija,ba_movil,per_uso_inter,m_tic,h_tic)

        
 
        # Crea el botón para llamar a la función en una ventana emergente
        
        if st.button("RESULTADO"):
        
           if prediccion == 0:
              
               st.write("No realiza inversiones TIC's")
           else:  
               st.write('La inversion en TICs es de :', prediccion )







def main():
    paginas = {
        "Home": pagina_1,
        "Modelo 1": pagina_2,
        "Modelo 2": pagina_3,
        "Modelo 3": pagina_4,
        # Agrega más páginas aquí
    }
    eleccion = st.sidebar.selectbox("Seleccione un Modelo", list(paginas.keys()))
    pagina = paginas[eleccion]
    pagina()

if __name__ == "__main__":
    main()

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.markdown("---")

image = Image.open("2.png")
st.sidebar.image(image, caption="", width=250)
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.markdown("---")


image = Image.open("1.png")
st.sidebar.image(image, use_column_width=False, width=170)

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.markdown("---")
st.sidebar.write("ML © 2023 - C. Flores & J. Lescano")


#para ejecutar el codigo
#.\env\Scripts\activate
#streamlit run app.py