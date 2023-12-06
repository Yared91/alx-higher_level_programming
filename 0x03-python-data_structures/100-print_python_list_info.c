/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject list
 */

#include <stdio.h>

struct timespec;

#include <Python.h>
#include <time.h>

void print_python_list_info(PyObject *p)
{
PyListObject *list_obj;
int alloc, size;

if (!PyList_Check(p))
{
printf("This isn't a Python list!\n");
return;
}

list_obj = (PyListObject *)p;
alloc = list_obj->allocated;
size = PyList_Size(list_obj);

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (int i = 0; i < size; i++)
{
printf("Element %d:", i);
PyObject *element = PyList_GetItem(list_obj, i);
Py_TYPE(element)->tp_name(element);
printf("\n");
}

printf("\n");
}
