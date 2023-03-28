exe: matrix_module.o random_module.o main.o
	gfortran matrix_module.o random_module.o main.o -o exe

matrix_module.o: matrix_module.f90
	gfortran -c matrix_module.f90

random_module.o: random_module.f90
	gfortran -c random_module.f90

main.o: main.f90
	gfortran -c main.f90

.PHONY: clean

clean:
	rm *.o
	rm *.mod
