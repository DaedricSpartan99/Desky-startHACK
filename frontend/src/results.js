import { useState, useEffect } from 'react'
import SearchBar from './searchbar'
import './results.css'
import { VStack, HStack, Flex, Box, Image, StackDivider } from '@chakra-ui/react'
import ScrollableFeed from 'react-scrollable-feed'

import { useSelector, useDispatch } from 'react-redux'
import searchStore from './redux/search_store'
import { setLocation } from './redux/slices/search'
import { search } from './database'

import WorkplaceEntry from './workplace_entry';

import logo_image from './assets/results/logo.png'
import inno_image from './assets/results/inno.png'
import filters_image from './assets/results/filters.png'
import suggest_image from './assets/results/suggest.png'
import dx_image from './assets/dx.png'
import sx_image from './assets/results/static-map.png'

function IconFilter({src, onClick}) {
  return (
    <Box boxSize='sm' onClick={onClick}>
      <Image src={src} alt='' />
    </Box>
  );
}

export default function Results() {

  const [results, setResults] = useState([]);

  const location = useSelector((state) => state.searchSlice.location, 
    (left, right) => left === right,
    searchStore.getState());

  const dispatch = useDispatch()

  function confirm(input) {
    if (input) {
      // update redux
      dispatch(setLocation(input));
    }
  }

  useEffect(() => {

    console.log("Search changed: ", location)

    // fetch results
    search(location).then((resp) => {
       if (!resp.ok) {
        return Promise.reject(resp);
      }
      
     return resp.json();

    }).then((data) => {

      console.log("Fetched data: ", data)
      setResults(data)

    }).catch((err) => {
      console.error("Could not fetch search data from server: ", err)
    })

  },[location]);

  function all_filter_cb() {
  }

  function bar_filter_cb() {
  }

  function coworking_filter_cb() {
  }

  function farm_filter_cb() {
  }


  //<SearchBar confirm={confirm}/>
  return (
    <div id="background-div">
      <div id="left-container">
        <img id="image-logo" src={logo_image} />
        <img id="image-inno" src={inno_image} />
        <SearchBar defaultValue={location} confirm={confirm}/>
        <img id="image-filters" src={filters_image} />
        {/*<HStack
          divider={<StackDivider borderColor='gray.200' />}
          spacing={2}
          orientation='vertical'
        >
            <IconFilter src='/results/tutti-filter.png' onClick={all_filter_cb}/>
            <IconFilter src='/results/bar-filter.png' onClick={bar_filter_cb}/>
            <IconFilter src='/results/coworking-filter.png' onClick={coworking_filter_cb}/>
            <IconFilter src='/results/farm-filter.png' onClick={farm_filter_cb}/>
        </HStack>*/}
        <ScrollableFeed>
          {results ? results.map((entry) => <WorkplaceEntry property={entry} /> ) : null}
          <img id="suggest" src={suggest_image} />
        </ScrollableFeed>
      </div>
      <div id="right-container">
        <img id="right-image" src={dx_image} />
        <img id="right-map" src={sx_image} />
      </div>
    </div>
  );
}
