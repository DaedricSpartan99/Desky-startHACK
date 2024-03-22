import * as React from "react";
import styled from "styled-components";

import { 
  Text,
  Flex,
  Button,
  Box, 
  Image, 
  Badge ,
  HStack,
  Spacer,
  Stack
} from '@chakra-ui/react'

export default function WorkplaceEntry({property}) {

  var category;
  var location;
  var price;
  var per;
  var convertible;

  if (property.category == 'coworking') {

    category = 'Coworking';
    price = property.starting_price;
    location = '3,2km from center';
    per = 'month';
    convertible = '';

  } else if (property.category == 'farm') {

    category = 'Farm';
    price = 25;
    location = property.city_name;
    per = 'night';
    convertible = 'Convertible in 2h of work';
  }


const Div = styled.div`
  display: flex;
  scale: 0.9;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  display: flex;
  min-height: 238px;
  max-width: 682px;
  padding: 5px 26px 21px 80px;
  @media (max-width: 991px) {
    padding: 0 20px;
  }
  background: white;
  border-radius: 10px;
`;

const Img = styled.img`
  inset: 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
  object-position: center;
`;

const Div1 = styled.div`
  max-width: 100px;
  max-height: 100px;
  max-width: 30%;
  border-radius: 10px;
`;

const Div2 = styled.div`
  position: relative;
  display: flex;
  width: 339px;
  max-width: 100%;
  gap: 20px;
`;

const Div3 = styled.div`
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  flex-basis: 0;
  width: fit-content;
`;

const Div4 = styled.div`
  display: flex;
  margin-bottom: 5px;
  gap: 4px;
  @media (max-width: 991px) {
    padding-right: 20px;
  }
`;

const Img2 = styled.img`
  aspect-ratio: 1.06;
  object-fit: auto;
  object-position: center;
  width: 18px;
  fill: #aa3267;
  stroke-width: 1px;
  stroke: #aa3267;
  border-color: rgba(170, 50, 103, 1);
  border-style: solid;
  border-width: 1px;
`;

const Img3 = styled.img`
  aspect-ratio: 1.06;
  object-fit: auto;
  object-position: center;
  width: 18px;
  fill: #aa3267;
  stroke-width: 1px;
  stroke: #aa3267;
  border-color: rgba(170, 50, 103, 1);
  border-style: solid;
  border-width: 1px;
`;

const Img4 = styled.img`
  aspect-ratio: 1.06;
  object-fit: auto;
  object-position: center;
  width: 18px;
  fill: #aa3267;
  stroke-width: 1px;
  stroke: #aa3267;
  border-color: rgba(170, 50, 103, 1);
  border-style: solid;
  border-width: 1px;
`;

const Img5 = styled.img`
  aspect-ratio: 1.06;
  object-fit: auto;
  object-position: center;
  width: 18px;
  fill: #aa3267;
  stroke-width: 1px;
  stroke: #aa3267;
  border-color: rgba(170, 50, 103, 1);
  border-style: solid;
  border-width: 1px;
`;

const Img6 = styled.img`
  aspect-ratio: 1.06;
  object-fit: auto;
  object-position: center;
  width: 18px;
  fill: linear-gradient(90deg, #ac396b 60%, #d192ae 61%, #fff 62%);
  stroke-width: 1px;
  stroke: #aa3367;
  border-color: rgba(170, 51, 103, 1);
  border-style: solid;
  border-width: 1px;
`;

const Div5 = styled.div`
  color: #3c3c3b;
  margin-top: 11px;
  font: 600 20px Montserrat, sans-serif;
`;

const Div6 = styled.div`
  color: #878787;
  margin-bottom: 5px;
  font: 400 19px Montserrat, sans-serif;
`;

const Img7 = styled.img`
  aspect-ratio: 1.09;
  object-fit: auto;
  object-position: center;
  width: 24px;
  fill: #aa3267;
  stroke-width: 0.39px;
  stroke: #aa3267;
  border-color: rgba(170, 50, 103, 1);
  border-style: solid;
  border-width: 0px;
  margin: auto 0;
`;

const Div7 = styled.div`
  position: relative;
  display: flex;
  margin-top: 15px;
  align-items: start;
  gap: 20px;
  justify-content: space-between;
`;

const Div8 = styled.div`
  display: flex;
  margin-top: 4px;
  flex-direction: column;
`;

const Div9 = styled.div`
  color: #878787;
  font: 400 17px Montserrat, sans-serif;
`;

const Div10 = styled.div`
  display: flex;
  margin-top: 16px;
  gap: 20px;
  @media (max-width: 991px) {
    padding-right: 20px;
  }
`;

const Img8 = styled.img`
  aspect-ratio: 0.95;
  object-fit: auto;
  object-position: center;
  width: 22px;
  fill: #3c3c3c;
  stroke-width: 0.16px;
  stroke: #3c3c3c;
  border-color: rgba(60, 60, 60, 1);
  border-style: solid;
  border-width: 0px;
`;

const Img9 = styled.img`
  aspect-ratio: 1.25;
  object-fit: auto;
  object-position: center;
  width: 25px;
  margin: auto 0;
`;

const Img10 = styled.img`
  aspect-ratio: 0.45;
  object-fit: auto;
  object-position: center;
  width: 10px;
  align-self: start;
`;

const Img11 = styled.img`
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
  width: 22px;
  align-self: start;
`;

const Div11 = styled.div`
  display: flex;
  gap: 10px;
  font-size: 16px;
  color: #878787;
  font-weight: 400;
`;

const Img12 = styled.img`
  aspect-ratio: 1;
  object-fit: auto;
  object-position: center;
  width: 19px;
  fill: #008d36;
`;

const Div12 = styled.div`
  font-family: Montserrat, sans-serif;
`;

const Div13 = styled.div`
  position: relative;
  display: flex;
  margin-top: 20px;
  gap: 20px;
  justify-content: space-between;
`;

const Div14 = styled.div`
  align-self: start;
  display: flex;
  margin-top: 6px;
  flex-direction: column;
`;

const Div15 = styled.div`
  display: flex;
  gap: 6px;
  color: #3c3c3b;
`;

const Div16 = styled.div`
  font: 700 19px Montserrat, sans-serif;
`;

const Div17 = styled.div`
  flex-grow: 1;
  flex-basis: auto;
  font: 400 16px Montserrat, sans-serif;
`;

const Div18 = styled.div`
  color: #878787;
  margin-top: 6px;
  font: 400 14px Montserrat, sans-serif;
`;

const Div19 = styled.div`
  align-items: center;
  display: flex;
  font-size: 23px;
  color: #fff;
  font-weight: 400;
  white-space: nowrap;
  justify-content: center;
  @media (max-width: 991px) {
    white-space: initial;
  }
`;

const Div20 = styled.div`
  disply: flex;
  flex-direction: column;
  font-family: Montserrat, sans-serif;
  position: relative;
  fill: #aa3267;
  overflow: hidden;
  aspect-ratio: 3.62;
  justify-content: center;
  padding: 6px 31px;
  @media (max-width: 991px) {
    white-space: initial;
    padding: 0 20px;
  }
`;

const Div21 = styled.div`
  position: relative;
`;

  const Stars = () => {
    return (
      <Div4>
              <Img2
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/b658f72c8223834617a62a1b418dec262b91cfb3eeda85de55d342946cf37aef?"
              />
              <Img3
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/584fd31479ad4278dc1ed456cfc5dbd1d0f127c8ba68413ec7fa7097a126b2b0?"
              />
              <Img4
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/7ba4a3ab271949d227ac915f69e2403c3aa9ab11785997e6eaffc8ad57848726?"
              />
              <Img5
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/2c8630fd0ddfd64c138de836701425c0dc28913bcae8949c55b37e74ceef745b?"
              />
              <Img6
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/10bde4072e4066fbbc5e3be15db1dc7540a65804d8b41c9ca6c834a316f43ae3?"
              />
      </Div4>
    );
  }

  const Cuoricino = () => {
    return (
      <Img7
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/ff17923eaf25fccdc88863b3bfb21ef0443631e7996e15ffe774d3e541ebba68?"
          />
    );
  }

  const Icone = () => {
    return (
      <Div10>
              <Img8
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/30d16949c7c61a4c4908a1bddce1f1e2a796fca4f420f05a0eb41a700f1e7060?"
              />
              <Img9
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/1586362bb4a36adc90231fcd50a71efe8be170fcfdb00a832eb8f3ef6a8951ad?"
              />
              <Img10
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/db8bcb86641eef516aa5fb74958d0eac6ffd9ed8cb132d4a34865131f13ebac2?"
              />
              <Img11
                loading="lazy"
                src="https://cdn.builder.io/api/v1/image/assets/TEMP/66e252d8b35703fc644fbdf90806791e3f7d868c1112b2dae153a528a5d788b2?"
              />
            </Div10>
    );
  }

  const NotBusy = () => {
    return (
      <Flex placement='right'>
        <HStack> 
          <Img12
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/621ab10b0cee7f0848145d42aebe193263c1095cdbb087b96e0a94a04689c2bf?"
          />
          <Text>
            Not busy
          </Text>
        </HStack>
      </Flex>
    );
  }

  return (
    <Div>
    <HStack>
      <Box
        h='260px' minW='250px' maxW='250px' borderWidth='1px' borderRadius='lg' overflow='hidden'
      >
        <Image
          h='100%'
          ml='auto'
          mr='auto'
          display='block'
          borderRadius='lg' 
          fit='cover'
          fallbackSrc='https://via.placeholder.com/150'
          loading="lazy"
          src={property.image_url}
        />
      </Box>
      <Box>
        <Stars/>    
        <HStack>
          <Flex>
            <Stack>
              <Div5>{property.title}</Div5>
              <Div6>{category}</Div6>
            </Stack>
          </Flex>
          <Cuoricino/>
        </HStack>
        <Flex  alignItems='center'>
          <Div9>{location}</Div9>
          <Spacer/>
          <NotBusy/> 
        </Flex>
        <Icone/>
        <Flex>
          <HStack>
            <Flex> 
              <Stack>
                <HStack>
                  <Div16>{price}€</Div16>
                  <Div17>/ {per}</Div17>
                </HStack>
                <Div18>{convertible}</Div18>
              </Stack>
            </Flex>
            <Button
              colorScheme='#AA3267'
              size='md'
            >
              BOOK
            </Button>
          </HStack>
        </Flex>
      </Box>
    </HStack>
    </Div>
  );
}



