import React from 'react';

import { CSS } from 'config/stitches/stitches.config';

// Polymorphic Box component props
export interface IBoxProps
  extends Partial<React.AllHTMLAttributes<HTMLElement>>,
    IBoxCssProps {
  /**
   * @optional
   * @default 'div'
   * @description HTML element to render
   */
  as?: keyof HTMLElementTagNameMap;
  /**
   * @optional
   * @default {}
   * @description CSS styles
   * @example
   * <Box css={{ color: '$red', backgroundColor: '$blue' }} />
   */
  css?: CSS;
  /**
   * @description flex prop
   * @optional
   * @default false
   */
}

interface IBoxCssProps {
  /**
   * @description flex prop
   * @optional
   * @default false
   * @example
   * <Box flex />
   */
  flex?: boolean;
  /**
   * @description flex direction prop
   * @optional
   */
  fd?: CSS['flexDirection'];
  /**
   * @description flex wrap prop
   * @optional
   */
  fw?: CSS['flexWrap'];
  /**
   * @description flex align items prop
   * @optional
   * @default 'stretch'
   */
  ai?: CSS['alignItems'];
  /**
   * @description flex justify content prop
   * @optional
   * @default 'flex-start'
   * @example
   * <Box jc="center" />
   */
  jc?: CSS['justifyContent'];
  /**
   * @description margin prop
   * @optional
   */
  m?: CSS['margin'];
  /**
   * @description margin top prop
   * @optional
   * @example
   * <Box mt="10px" />
   */
  mt?: CSS['marginTop'];
  /**
   * @description margin right prop
   * @optional
   * @example
   * <Box mr="10px" />
   */
  mr?: CSS['marginRight'];
  /**
   * @description margin bottom prop
   * @optional
   * @example
   * <Box mb="10px" />
   */
  mb?: CSS['marginBottom'];
  /**
   * @description margin left prop
   * @optional
   * @example
   * <Box ml="10px" />
   */
  ml?: CSS['marginLeft'];
  /**
   * @description padding prop
   * @optional
   * @example
   * <Box p="10px" />
   */
  p?: CSS['padding'];
  /**
   * @description padding top prop
   * @optional
   * @example
   * <Box pt="10px" />
   */
  pt?: CSS['paddingTop'];
  /**
   * @description padding right prop
   * @optional
   * @example
   * <Box pr="10px" />
   */
  pr?: CSS['paddingRight'];
  /**
   * @description padding bottom prop
   * @optional
   * @example
   * <Box pb="10px" />
   */
  pb?: CSS['paddingBottom'];
  /**
   * @description padding left prop
   * @optional
   * @example
   * <Box pl="10px" />
   */
  pl?: CSS['paddingLeft'];
  /**
   * @description width prop
   * @optional
   * @example
   * <Box w="100px" />
   */
  width?: CSS['width'];
  /**
   * @description height prop
   * @optional
   * @example
   * <Box height="100px" />
   */
  height?: CSS['height'];
  /**
   * @description min background color prop
   * @optional
   * @example
   * <Box bg="red" />
   */
  bg?: CSS['backgroundColor'];
  /**
   * color prop
   * @optional
   * @example
   * <Box color="red" />
   */
  color?: CSS['color'];
}