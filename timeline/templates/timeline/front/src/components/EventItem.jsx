import { useCallback, useMemo } from 'react';
import { observer } from 'mobx-react';
import { state } from '../state';
import css from '../style/styles.module.css';
import ItemDetails from './ItemDetails';

const EventItem = observer(({ year, item, index }) => {
    const { selectedItem, colors, selectedColor } = state;

    const selected = useMemo(() => {
        const selection = selectedItem.id === item.id;
        return selection;
    }, [selectedItem, item]);

    const handleSelect = useCallback(() => {
        state.setSelectedItem(item);
    }, [item]);

    const focusItem = useMemo(() => {
        if (!selected) {
            return null;
        }
        return <ItemDetails item={item} />;
    }, [item, selected]);

    const color = useMemo(() => {
        return selected ? selectedColor : colors[index];
    }, [index, colors, selected, selectedColor]);

    const style = useMemo(() => {
        if (index === 0) {
            return `${css['timeline-slot']} ${css['slot-first']} ${css['year-item']}`;
        }
        if (index === year.length - 1) {
            return `${css['timeline-slot']} ${css['slot-last']} ${css['year-item']}`;
        }
        return `${css['timeline-slot']} ${css['year-item']}`;
    }, [index, year]);

    return (
        <>
            <div onClick={handleSelect} style={{ backgroundColor: color }} className={style}>
                {item.date}
            </div>
            {focusItem}
        </>
    );
});
export default EventItem;
