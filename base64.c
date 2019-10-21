#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

#define ARG_ERROR -1;
#define FILE_ERROR -2;
#define B64_TABLE "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

int b64_encode(FILE *in_file, FILE *out_file) {
  //Character buffer
  char *t;
  t = calloc(4, sizeof(char*));

  //Number of characters returned
  int n;

  //While the file can be read
  while (n = fread(t, 1, 3, in_file)) {
    //If not a full triplet can be read
    if (n != 3) {
      //If error exit
      if (ferror(in_file)) {
        fprintf(stderr, "Error in file\n");
        return FILE_ERROR;
      }
    }
    //Make bitstring (Not really a string, but I like to think of it as one for this)
    int s = 0;
    for (int i = 0; i < n; ++i) {
      //This way it only uses the last 24 bits of the 32 bit int
      s += t[i] << 8*(2-i);
    }
    //Do the appropriate shifts
    for (int i = 3; i >= (3-n); --i) {
      //Set a mask to grab the 6 bits I want at a time
      int mask = 0b111111 << 6*i;
      //Find the index of the b64 table
      int index = (s & mask) >> 6*i;
      putc(B64_TABLE[index], out_file);
    }
    if (n < 3) {
      //Print proper amount of padding when done with stream
      for (int i = 0; i < (3-n); ++i) {
        putc('=', out_file);
      }
    }
    else {
      //Remember to clean up the array when done printing triplet
      t = (char*) memset(t, 0, 3);
    }
  }
  return 0;
}

int b64_decode(FILE *in_file, FILE *out_file) {
  //Character buffer
  char *t;
  t = calloc(5, sizeof(char*));

  //Number of characters returned
  int n;

  //While the file can be read
  while (n = fread(t, 1, 4, in_file)) {
    //If not a full triplet can be read
    if (n != 4) {
      //If error exit
      if (ferror(in_file)) {
        fprintf(stderr, "Error in file\n");
        return FILE_ERROR;
      }
      //Something wrong with data
      else if (!feof(in_file)) {
        fprintf(stderr, "Error in data\n");
        return FILE_ERROR;
      }
    }

    //Make bitstring (Not really a string, but I like to think of it as one for this)
    int s = 0;
    int shift = 0;

    //Find the equal signs
    for (; shift < 4; ++shift) {
      if (t[shift] == '=') {
        break;
      }
    }
    for (int i = 0; i < shift; ++i) {
      int j = 0;
      //This way it only uses the last 24 bits of the 32 bit int
      for (; B64_TABLE[j] != t[i]; ++j) {}
      s += j << 6*(3-i);
    }
    //Do the appropriate shifts
    for (int i = 2; i >= 0; --i) {
      //Set a mask to grab the 8 bits I want at a time
      int mask = 0b11111111 << 8*i;
      //Find the index of the b64 table
      int c = (s & mask) >> 8*i;
      putc(c, out_file);
    }
    t = (char*) memset(t, 0, 4);
  }
  return 0;
}

int main(int argc, char **argv) {
  FILE *f1 = stdin, *f2 = stdout;

  if (argc > 1 && strcmp(argv[1], "-e") != 0 && strcmp(argv[1], "-d") != 0) {
    fprintf(stderr, "First argument must be '-e' or '-d'\n");
    return ARG_ERROR;
  }
  
  //If 2 files given
  if (argc == 4) {
    f1 = fopen(argv[2], "r");
    f2 = fopen(argv[3], "w");

    //Fail if file doesn't exist
    if (f1 == NULL) {
      fprintf(stderr, "%s doesn't exist! ABORTING\n", argv[2]);
      return ARG_ERROR;
    }

    if (strcmp(argv[1], "-e") == 0)
      b64_encode(f1, f2);
    else
      b64_decode(f1, f2);
  }
  //If 1 file is given
  else if (argc == 3) {
    f1 = fopen(argv[2], "r");

    //Fail if file doesn't exist
    if (f1 == NULL) {
      fprintf(stderr, "%s doesn't exist! ABORTING\n", argv[2]);
      return ARG_ERROR;
    }

    if (strcmp(argv[1], "-e") == 0)
      b64_encode(f1, stdout);
    else
      b64_decode(f1, stdout);
    putc('\n', stdout);
  }
  else {
    fprintf(stderr, "Usage: %s -e <in file> <out file>\n", argv[0]);
    fprintf(stderr, "       %s -d <in file> <out file>\n", argv[0]);
    fprintf(stderr, "       %s -e <in file>\n", argv[0]);
    fprintf(stderr, "       %s -d <in file>\n", argv[0]);
    return ARG_ERROR;
  }
  fclose(f1);
  fclose(f2);

  return 0;
}
