if ! 'rm -r */*.pyc'; then
	echo 'No hay pyc para borrar'
else
	echo 'Se borraron los pyc'
fi 2>/dev/null

if ! 'rm -r ./proyectos/*'; then
	echo 'No hay proyectos para borrar'
else
	echo 'Se borraron los proyectos'
fi 2>/dev/null

if ! './setup.py' 'genpot'; then
	echo 'No se pudo generar pot'
else
	echo 'Se genero pot'
fi 2>/dev/null

if ! './setup.py' 'fix_manifest'; then
	echo 'No se pudo arreglar el manifest'
else
	echo 'Se arreglo el manifest'
fi 2>/dev/null

if ! './setup.py' 'dist_xo'; then
	echo 'Hubo un error al generar el .XO'
else
	echo 'Se genero el .XO en la carpeta ./dist/'
fi 2>/dev/null
