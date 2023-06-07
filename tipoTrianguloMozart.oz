local
  proc{Triangulo Lado1 Lado2 Lado3}
     if Lado1==Lado2 then
	if Lado2==Lado3 then
	   {Browse 'Es un tiangulo equilatero'}
	elseif Lado2\=Lado3 then
	   {Browse 'Es un triangulo isosceles'}
	end
     else
	if Lado2\=Lado3 then
	   if Lado1\=Lado3 then
	      {Browse 'Es un triangulo escaleno'}
	   end
	end
	if Lado2==Lado3 then
	   {Browse 'Es un triangulo isosceles'}
	elseif Lado1==Lado3 then
	   {Browse 'Es un triangulo isosceles'}
	end
	
     end
  end
in
	{Triangulo 3 3 3}   
end