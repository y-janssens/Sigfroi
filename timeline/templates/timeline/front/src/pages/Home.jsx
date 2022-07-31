import { observer } from 'mobx-react';
import YearSelector from '../components/YearSelector';
import css from '../style/styles.module.css';
import SelectedYear from '../components/SelectedYear';

const Home = observer(() => {
    return (
        <div className={css['timeline-container']}>
            <div className={css['timeline-header']}>Chronologie Générale</div>
            <YearSelector />
            <SelectedYear />
        </div>
    );
});
export default Home;
