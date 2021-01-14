/* create a "file" in /proc */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/init.h> 
#include <linux/uaccess.h>
#define MAX_buff_SIZE 1024
#define NAME "buffer"


/* This structure hold information about the /proc file */

static struct proc_dir_entry *proc_file;

/* The buff used to store character for this module  */

static char procfs_buff[MAX_buff_SIZE];

/*The size of the buff */

static unsigned long procfs_buff_size = 0;

/* This function is called then the /proc file is read */

static ssize_t proc_file_read(struct file *file, char *buff, size_t buff_length, loff_t *offset)
{
	static int flag = 0; 
	if(flag) {
	printk(KERN_INFO "read : END\n");
		flag = 0;
		return 0;
	}
	printk(KERN_INFO "reading from (/proc/%s):\n",NAME);
	flag = 1;
	return  sprintf(buff, procfs_buff);
}
/* This function is called with the /proc file is written */
static ssize_t proc_file_write(struct file *file,const char *buff, size_t count, loff_t *offset)
{
        /* get buff size */
        procfs_buff_size = count;
        if (procfs_buff_size > MAX_buff_SIZE ) {
                procfs_buff_size = MAX_buff_SIZE;
        }
        /* write data to the buff */
        if ( copy_from_user(procfs_buff, buff, procfs_buff_size) ) {
                return -EFAULT;
        }
        return procfs_buff_size;
}

static struct file_operations fops_struct = {
	.read = proc_file_read,
	.write = proc_file_write,
};

/* This function is executed when the module is inserted*/
static int __init Lab7_init(void)
{
        /* create the /proc file */
        proc_file = proc_create(NAME, 0644, NULL, &fops_struct);
        if (proc_file == NULL) {
                remove_proc_entry(NAME, NULL);
                printk(KERN_ALERT "Error: Could not initialize /proc/%s\n",
                         NAME);
                return -ENOMEM;
        }

        printk(KERN_INFO "/proc/%s created\n", NAME);
        return 0;       
}

/* This function is called when the module is unloaded */

static void __exit Lab7_exit(void)
{
        remove_proc_entry(NAME, NULL);
        printk(KERN_INFO "/proc/%s removed\n", NAME);
}

module_init(Lab7_init);
module_exit(Lab7_exit);