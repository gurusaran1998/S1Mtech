#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

int buf;
sem_t m;

void *pass_fn1(void *arg) {
	int temp;
	sem_wait(&m);
    	temp = buf;
        printf("The passed value is %d.\n", temp);
    	sem_post(&m);
        return((void *)0);
}

void  main() {

	pthread_t tid;
	sem_init(&m,0,1);
	sem_wait(&m);
	printf("Enter the number you want to pass:");
	scanf("%d", &buf);
    	sem_post(&m);
	pthread_create(&tid, NULL, pass_fn1, NULL);
	sleep(1);
	exit(0);
}
