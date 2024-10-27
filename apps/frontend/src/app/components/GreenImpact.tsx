import React, {useState} from "react";
import { RxCross1 } from "react-icons/rx";

interface GreenImpactProps {
    distance?: number;
    fuel?: number;
    carbon_emission?: number;
}

const GreenImpact: React.FC<GreenImpactProps> = ({distance = 0.0, fuel=0.0, carbon_emission=0.0}) => {
    
    const [isDialogOpen, setDialogOpen] = useState(false);

    const toggleDialog = () => {
        setDialogOpen(!isDialogOpen)
    }

    return (
        isDialogOpen ? (
            <div className="absolute top-0 right-4">
                <div className="flex flex-col h-auto w-60 mt-24 gap-4 text-sm p-6 bg-[#AFE0B1] text-[#054A29] rounded-2xl">
                    <div className="flex justify-between pb-4">
                        <p className="text-xl font-normal">Green Impact</p>
                        <RxCross1 className="h-7 w-7 cursor-pointer" onClick={toggleDialog}/>
                    </div>
                    <div className="flex flex-col gap-4">
                        <div className="flex justify-between">
                            <span>Distance Travelled</span>
                            <span>{distance}km</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Fuel Consumption</span>
                            <span>{fuel}L</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Type of Fuel</span>
                            <span>Petrol</span>
                        </div>
                        <div className="flex justify-between">
                            <span>Carbon Emission (CO2e)</span>
                            <span>{carbon_emission}</span>
                        </div>
                    </div>

                </div>
            </div>
        ) :
        (
            <div className='absolute top-0 right-4'>
              <img src='Green.svg' className=' h-12 w-12 z-10 mt-24 cursor-pointer' onClick={toggleDialog}/>
            </div>
        )
    );

};
export default GreenImpact;