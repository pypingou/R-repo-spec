%global packname  maptools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.10
Release:          1%{?dist}
Summary:          Tools for reading and handling spatial objects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-foreign R-sp R-methods R-lattice 

BuildRequires:    R-devel tex(latex) R-foreign R-sp R-methods R-lattice 

%description
Set of tools for manipulating and reading geographic data, in particular
ESRI shapefiles; C code used from shapelib. It includes binary access to
GSHHS shoreline files. The package also provides interface wrappers for
exchanging spatial objects with packages such as PBSmapping, spatstat,
maps, RArcInfo, Stata tmap, WinBUGS, Mondrian, and others.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.10-1
- initial package for Fedora