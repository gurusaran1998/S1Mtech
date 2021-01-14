#include <stdio.h>
#include <semaphore.h>
#include <pthread.h>

int buf;
sem_t full, mutex;

void *multiplication (void *args) {

    int temp;
    sem_wait(&full);
    temp=buf;
    sem_post(&mutex);

    sem_wait(&full);
    buf=buf* temp;
    sem_post(&mutex);

}

int main() {

    pthread_t tid;
    sem_init(&full, 0, 0);

    sem_init(&mutex, 0, 1);

    pthread_create(&tid, NULL, multiplication, NULL);

    for (int i=0 ; i<2 ; i++) {
        sem_wait(&mutex);
        printf("Enter the number:");
        scanf("%d", &buf);
        sem_post(&full);
    }

    sem_wait(&mutex);
   printf("The product is %d\n",buf);
}
