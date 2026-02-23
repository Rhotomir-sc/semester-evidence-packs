#include <stdio.h>
#include <string.h>

#define MAX_LINE 256

typedef struct {
    char ts[32];
    char user[32];
    char ip[32];
    char action[32];
    char status[32];
} Event;

int is_suspicious_ip(const char *ip) {
    return (strcmp(ip, "203.0.113.77") == 0) || (strcmp(ip, "198.51.100.23") == 0);
}

int main(void) {
    FILE *in = fopen("evidence/artifacts/lab01_sample.log", "r");
    if (!in) {
        printf("ERROR: cannot open sample log file.\n");
        return 1;
    }

    // counts
    int total = 0;
    int login_fail = 0, login_success = 0;
    int sudo_ok = 0, sudo_blocked = 0;
    int scan_detected = 0;
    int suspicious_ip_hits = 0;

    char line[MAX_LINE];

    while (fgets(line, sizeof(line), in)) {
        Event e = {0};

        // Expected format:
        // TS user=... ip=... action=... status=...
        // We parse with sscanf. This is enough for the lab.
        int ok = sscanf(
            line,
            "%31s user=%31s ip=%31s action=%31s status=%31s",
            e.ts, e.user, e.ip, e.action, e.status
        );

        if (ok != 5) {
            // skip malformed line
            continue;
        }

        total++;

        if (is_suspicious_ip(e.ip)) suspicious_ip_hits++;

        if (strcmp(e.action, "login") == 0) {
            if (strcmp(e.status, "fail") == 0) login_fail++;
            else if (strcmp(e.status, "success") == 0) login_success++;
        } else if (strcmp(e.action, "sudo_cmd") == 0) {
            if (strcmp(e.status, "ok") == 0) sudo_ok++;
            else if (strcmp(e.status, "blocked") == 0) sudo_blocked++;
        } else if (strcmp(e.action, "scan") == 0) {
            if (strcmp(e.status, "detected") == 0) scan_detected++;
        }
    }

    fclose(in);

    // Write CSV report
    FILE *out = fopen("evidence/artifacts/lab01_report.csv", "w");
    if (!out) {
        printf("ERROR: cannot write report CSV.\n");
        return 1;
    }

    fprintf(out, "metric,value\n");
    fprintf(out, "total_events,%d\n", total);
    fprintf(out, "login_fail,%d\n", login_fail);
    fprintf(out, "login_success,%d\n", login_success);
    fprintf(out, "sudo_ok,%d\n", sudo_ok);
    fprintf(out, "sudo_blocked,%d\n", sudo_blocked);
    fprintf(out, "scan_detected,%d\n", scan_detected);
    fprintf(out, "suspicious_ip_hits,%d\n", suspicious_ip_hits);

    // Simple “IOC flag” (failed login burst >=3)
    fprintf(out, "ioc_failed_login_burst,%s\n", (login_fail >= 3) ? "true" : "false");

    fclose(out);

    printf("OK. Parsed %d events. CSV written: evidence/artifacts/lab01_report.csv\n", total);
    return 0;
}
