"use client";
import { useUser } from '@auth0/nextjs-auth0/client';
import { redirect } from "next/navigation";
import { useEffect } from 'react';
import dynamic from 'next/dynamic';
import Hamburger from '../components/Hamburger';
import 'leaflet/dist/leaflet.css';
import { useRouter } from 'next/navigation';
import { LatLngTuple } from 'leaflet';
import GreenImpact from '../components/GreenImpact';

