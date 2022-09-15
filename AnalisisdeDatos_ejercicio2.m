% Se importan los valores por columna del archivo de excel con readvars para leer variables 
% T es una variable para la altura y T1 para la talla de calzado
T = readvars('Estadística de Tallas (Anónimo) (Respuestas).xlsx','Range','A2:A201')
T1 = readvars('Estadística de Tallas (Anónimo) (Respuestas).xlsx','Range','B2:B201')
% Dnest y Dntalla son variables para hacer el cálculo de la distribución
% normal (cálculo de Mu y sigma)
Dnest = fitdist(T,'Normal')
Dntalla = fitdist(T1,'Normal')
% La variable "y" y "y1" realiza el cálculo de la función Gaussiana (f(x) = a e^{- {
% \frac{^2 }{ 2 c^2} } } )
y=normpdf(T,Dnest.mu,Dnest.sigma);
% Se grafica la función Gaussiana para cada caso
plot(T,y)
% Se toman los datos de mu y sigma de talla y estatura con Dntalla.mu,
% Dntalla.sigma, Dnest.mu y Dnest.sigma
y1=normpdf(T1,Dntalla.mu,Dntalla.sigma);
plot(T1,y1)
%Se obtiene el histograma con la función "histogram" tanto para estatura
%(T) como para talla (T1)
histogram(T)
histogram(T1)

%Se introducen los datos de estatura y talla pero clasificado por sexos,
%para esta división se usaron filtros en excel para facilitar la tarea.
Femest= readvars('Estadística de Tallas (Anónimo) (Respuestas).xlsx','Range','E2:E100');
Femtalla= readvars('Estadística de Tallas (Anónimo) (Respuestas).xlsx','Range','F2:F100');
Masest = readvars('Estadística de Tallas (Anónimo) (Respuestas).xlsx','Range','I2:I100');
Mastalla = readvars('Estadística de Tallas (Anónimo) (Respuestas).xlsx','Range','J2:J100');

%Cálculo de la probabilidad que un número al azar se encuentre dentro de la variación estandar  
proba_alt = normcdf(167.025+2*9.50823,165.699,8.65879 ) - normcdf(167.025-2*9.50823,168.351,10.5439)

proba_cal = normcdf(25.7425+2*1.91593 ,25.4753,1.74477 ) - normcdf(25.7425-2*1.9534 ,26.0097,2.12463)