%global packname  ncdf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.6
Release:          1%{?dist}
Summary:          Interface to Unidata netCDF data files

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a high-level R interface to Unidata's netCDF data
files, which are portable across platforms and include metadata
information in addition to the data sets. Using this package netCDF files
can be opened and data sets read in easily. It is also easy to create new
netCDF dimensions, variables, and files, or manipulate existing netCDF
files. This interface provides considerably more functionality than the
old "netCDF" package for R, and is not compatible with the old "netCDF"
package for R. Release 1.2 (2005-01-24) adds better support for character
variables, and miscellaneous bug fixes.  Release 1.3 (2005-03-27) is for
miscellaneous bug fixes, and improves the documentation.  Release 1.4
(2005-06-27) improves the efficiency, and adds small bug fixes. Release
1.5 (2006-02-27) adds support for byte variables, plus small bug fixes.
Release 1.6 (2006-06-19) adds various bug fixes, plus support for making
dimensions WITHOUT dimvars (coordinate variables), although I think this
is a bad idea in general.  ALSO, the default behavior for put.var.ncdf
with unlimited variables and NO specified start and count parameters has
changed!  Before, the default was to append to the end of the existing
variable.  Now, the default is to assume a start of 1 along each
dimension, and a count of the current length of each dimension.  This
really can be ambiguous when using an unlimited dimension. I always
specify both start and count when writing to a variable with an unlimited
dimension, and suggest you do as well.  I may require this in a future
release, as it seems to cause people problems.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.6-1
- initial package for Fedora