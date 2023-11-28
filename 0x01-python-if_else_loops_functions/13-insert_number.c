#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: input of head of singly linked list
 * @number: number input
 * Author - Tolulope Fakunle
 * Return: NULL for failure, pointer to new node for Success
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;

if (node == NULL || node->n >= number)
{
new->next = node;
*head = new;
return (new);
}

while (node && node->next && node->next->n < number)
node = node->next;

new->next = node->next;
node->next = new;

return (new);
}
