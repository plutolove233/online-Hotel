import request from './http.js';

export function login(data) {
  console.log(data)
  return request({
    url: '/login',
    method: 'post',
    data
  });
}

export function getOrder(data) {
  console.log(data)
  return request({
    url: `/hotel/orderForm/get`,
    method: 'post',
    data
  });
}

export function checkin(data) {
  console.log(data)
  return request({
    url: `/hotel/orderForm/checkin`,
    method: 'put',
    data
  });
}

export function checkout(data) {
  console.log(data)
  return request({
    url: `/hotel/orderForm/checkout`,
    method: 'put',
    data
  });
}


export function cancelOrder(data) {
  console.log(data)
  return request({
    url: `/orderForm/cancel`,
    method: 'put',
    data
  });
}

export function getRoomType(data) {
  console.log(data)
  return request({
    url: `/roomType`,
    method: 'get',
    data
  });
}

export function getOrderByUser() {
  return request({
    url: `/user/orderForm/getList`,
    method: 'get'
  });
}

export function getHotel(data) {
  return request({
    url: `/user/query_hotel`,
    method: 'post',
    data
  });
}


export function getHotelDetail(data) {
  return request({
    url: `/user/get_hotel_detail`,
    method: 'post',
    data
  });
}


export function orderRoom(data) {
  return request({
    url: `/user/orderForm/reserve`,
    method: 'post',
    data
  });
}


export function getRoomInfo(data) {
  return request({
    url: `/roomType/${data.RoomID}`,
    method: 'get',
    data
  });
}

export function getOrderInfo(data) {
  return request({
    url: `/orderForm/getOrderInfo`,
    method: 'post',
    data
  });
}


export function getCommentInfo(data) {
  return request({
    url: `/remark/getInfo`,
    method: 'post',
    data
  });
}


export function addCommentInfo(data) {
  return request({
    url: `/remark/add`,
    method: 'post',
    data
  });
}

export function getAllRoom(data) {
  return request({
    url: `/hotel/room`,
    method: 'post',
    data
  });
}

export function getRoomDetailInfo(data) {
  return request({
    url: `/room/get_info`,
    method: 'post',
    data
  });
}

export function registerUser(data) {
  return request({
    url: `/user/register`,
    method: 'post',
    data
  });
}

export function registerHotel(data) {
  return request({
    url: `/hotel/register`,
    method: 'post',
    data
  });
}