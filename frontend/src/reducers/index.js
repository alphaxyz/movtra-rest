import { combineReducers } from 'redux';
import movies from './movies';
import auth from './auth';
import profile from './profile';

export default combineReducers({
    movies,
    auth,
    profile
});