#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 1 for cycle, unless 0
 */

int check_cycle(listint_t *list)
{
listint_t *rapid, *sluggish;

if (list == NULL || list->next == NULL)
{
return (0);
}

sluggish = list;
rapid = list;

while (sluggish && rapid && rapid->next)
{
if (sluggish == rapid)
{
return (1);
}

sluggish = sluggish->next;
rapid = rapid->next->next;
}
return (0);
}
