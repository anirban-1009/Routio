import React, { useState } from "react";
import { RxHamburgerMenu, RxCross1 } from "react-icons/rx";

const Hamburger = () => {
    // State to manage the visibility of the navigation dialog
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const [isMenuOpen, setIsMenuOpen] = useState(true);

    // Function to handle opening the dialog
    const handleOpenDialog = () => {
        setIsDialogOpen(true);
        setIsMenuOpen(false);
    };

    // Function to handle closing the dialog
    const handleCloseDialog = () => {
        setIsDialogOpen(false);
        setIsMenuOpen(true)
    };

    return (
        <div>
            {isMenuOpen && (
                <div className="absolute top-4 h-12 w-12 ml-4 rounded-full z-10" id="modal-root">
                    <div className="absolute top-2 left-0 cursor-pointer" onClick={handleOpenDialog}>
                        <RxHamburgerMenu className="w-8 h-8 text-black" />
                    </div>
                </div>
            )}

            {/* Navigation dialog */}
            {isDialogOpen && (
                <div className="nav-links fixed top-0 bottom-0 right-0 m-auto left-0 w-[20rem] h-[31rem] z-10 bg-white text-black">
                    {/* Close button */}
                    <div className="absolute right-0 top-0 cursor-pointer" onClick={handleCloseDialog}>
                        <RxCross1 className="close-icon h-8 w-8 mt-7 mr-9" />
                    </div>

                    {/* Navigation links */}
                    <ul className="flex justify-center h-full items-center text-3xl ">
                        <div className="flex flex-col items-start gap-8">
                        <li><a href="/profile">Profile</a></li>
                        <li><a href="/report">Report</a></li>
                        <li><a href="/schedule">Schedule</a></li>
                        </div>
                    </ul>
                </div>
            )}
        </div>
    );
};

export default Hamburger;
