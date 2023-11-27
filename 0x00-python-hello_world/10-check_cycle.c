#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 1 for cycle, unless 0
 */

int check_cycle(listint_t *list)
{
listint_t *rapid = 0, *sluggish = 0;

if (!list || !list->next)
{
return (0);
}

rapid = list->next;
sluggish = list->next->next;

while (sluggish != NULL && rapid != NULL && rapid->next != NULL)
{
sluggish = sluggish->next;
rapid = rapid->next->next;

if (sluggish == rapid)
{
return (1);
}
}

return (0);
}
