#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints PyListObject data
 * @p: PyObject input
 */

void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
printf("[*] Python list info\n");
printf("  [ERROR] Invalid List Object\n");
return;
}

Py_ssize_t size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}

/**
 * print_python_bytes - prints PyBytesObject data
 * @p: PyObject input
 */

void print_python_bytes(PyObject *p)
{
Py_ssize_t size = PyBytes_GET_SIZE(p);
char *string = PyBytes_AsString(p);

if (!PyBytes_CheckExact(p))
{
printf("[.] bytes object info\n");
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);
printf("  first %d bytes:", (size > 10) ? 10 : (int)size);
for (int i = 0; i < ((size > 10) ? 10 : (int)size); i++)
{
printf(" %02x", (unsigned char)string[i]);
}
printf("\n");
}

/**
 * print_python_float - prints PyFloatObject data
 * @p: PyObject input
 */

void print_python_float(PyObject *p)
{
if (!PyFloat_Check(p))
{
printf("[.] float object info\n");
printf("  [ERROR] Invalid Float Object\n");
return;
}

double value = PyFloat_AS_DOUBLE(p);
printf("[.] float object info\n");
printf("  value: %f\n", value);
}
