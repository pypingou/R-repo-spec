%global packname  ncdf4
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Interface to Unidata netCDF (version 4 or earlier) format data files

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides a high-level R interface to data files written using
Unidata's netCDF library (version 4 or earlier), which are binary data
files that are portable across platforms and include metadata information
in addition to the data sets. Using this package, netCDF files (either
version 4 or "classic" version 3) can be opened and data sets read in
easily. It is also easy to create new netCDF dimensions, variables, and
files, in either version 3 or 4 format, and manipulate existing netCDF
files. This package replaces the former ncdf package, which only worked
with netcdf version 3 files.  For various reasons the names of the
functions have had to be changed from the names in the ncdf package.  The
old ncdf package is still available at the URL given below, if you need to
have backward compatibility. It should be possible to have both the ncdf
and ncdf4 packages installed simultaneously without a problem. However,
the ncdf package does not provide an interface for netcdf version 4 files.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora