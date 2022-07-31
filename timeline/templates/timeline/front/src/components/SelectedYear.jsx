import { useMemo, useEffect } from 'react';
import { observer } from 'mobx-react';
import { state } from '../state';
import css from '../style/styles.module.css';
import EventItem from './EventItem';

const SelectedYear = observer(() => {
    const { events, selectedYear, selectedItem } = state;

    const year = useMemo(() => {
        const items = [];
        events.map((item) => {
            if (item.name === 0) {
                items.push(item);
            } else if (item.year === selectedYear) {
                items.push(item);
            }
            return item;
        });
        return items;
    }, [events, selectedYear]);

    useEffect(() => {
        if (year.length > 1 && selectedItem.length < 1) {
            state.setSelectedItem(year[1]);
        }
    }, [year, selectedYear, selectedItem]);

    return (
        <div className={css['years-container']}>
            <div className={css['year-items-container']}>
                {year.map((item, index) => {
                    return <EventItem key={item.id} year={year} item={item} index={index} />;
                })}
            </div>
        </div>
    );
});

export default SelectedYear;
