# Sentinel Firewall Demo

## Start Firewall

```bash
python3 src/main.py monitor
```

## Generate Traffic

```bash
ping 8.8.8.8
```

```bash
curl https://example.com
```

## View Logs

```bash
python3 src/main.py logs
```

## Generate Report

```bash
python3 src/main.py report
```

## Show Summary

```bash
python3 src/main.py summary
```
