time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_part in time.split(','):
    for component in time_part.split():
        if 'h' in component:
            hours = int(component.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in component:
            minutes = int(component.replace('m', ''))
            total_minutes += minutes
        elif 's' in component:
            seconds = int(component.replace('s', ''))
            total_minutes += seconds // 60

print(f"Общее количество минут: {total_minutes}")