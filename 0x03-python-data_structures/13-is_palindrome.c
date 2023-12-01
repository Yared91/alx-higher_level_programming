#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to 1st node in list
 * Return: pointer to 1st node in new list
 */

void reverse_listint(listint_t **head)
{
listint_t *past = NULL;
listint_t *now = *head;
listint_t *next = NULL;

while (now)
{
next = now->next;
now->next = past;
past = now;
now = next;
}
*head = past;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 for Success, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
listint_t *sluggish = *head, *rapid = *head, *tent = *head, *copy = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (1)
{
rapid = rapid->next->next;
if (!rapid)
{
copy = sluggish->next;
break;
}
if (!rapid->next)
{
copy = sluggish->next->next;
break;
}
sluggish = sluggish->next;
}
reverse_listint(&copy);

while (copy && tent)
{
if (tent->n == copy->n)
{
copy = copy->next;
tent = tent->next;
}
else
{
return (0);
}
}
if (!copy)
return (1);

return (0);
}
