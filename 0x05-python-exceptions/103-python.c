#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - prints float number
 * @p: address of the object
 */

void print_python_float(PyObject *p)
{
	double p;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name), "float")
	{
		printf("  [ERROR] Invalid Float Object");

	}
}
