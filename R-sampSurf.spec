%global packname  sampSurf
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Sampling Surface Simulation for Areal Sampling Methods

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-sp R-raster R-rasterVis R-gpclib 


BuildRequires:    R-devel tex(latex) R-methods R-sp R-raster R-rasterVis R-gpclib



%description
This package provides the base classes and routines for sampling surface
simulation useful in the comparison of different areal sampling methods in
forestry, ecology and natural resources.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora