#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

void print_python_float(PyObject *p);

/**
 * print_python_bytes - print a python list.
 * @p: a python object list
 */
void print_python_bytes(PyObject *p)
{
	size_t i, len, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 9)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %lu bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
* print_python_list - print basic info about a python list.
* @p: a python object list
*/
void print_python_list(PyObject *p)
{
	int i, size, alloc;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
		else if (!strcmp(type, "float"))
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_float - prints float number
 * @p: address of the object
 */

void print_python_float(PyObject *p)
{
	double d;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	d = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
	PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
