#include <Python.h>

/**
 * print_python_list_info - print basic info about a python list.
 * @p: a python object list
 */

void print_python_list_info(PyObject *p)
{
        int size, alloc, i;
        PyObject *obj;

        size = Py_SIZE(p);
        alloc = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);

        for (i = 0; i < size; i++)
        {
                printf("Element %d: ", i);
                obj = PyList_GetItem(p, i);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}

/**
 * print_python_bytes - print a python list.
 * @p: a python object list
 */
void print_python_bytes(PyObject *p)
{
    unsigned char i, size;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    if (((PyVarObject *)p)->ob_size > 10)
        size = 10;
    else
        size = ((PyVarObject *)p)->ob_size + 1;

    printf("  first %d bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size-1))
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
    int size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocates = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %d: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
    }
}