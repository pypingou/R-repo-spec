%global packname  GEOmap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.01
Release:          1%{?dist}
Summary:          Topographic and Geologic Mapping

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-01.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-geomapdata R-RPMG R-akima R-splancs 

BuildRequires:    R-devel tex(latex) R-geomapdata R-RPMG R-akima R-splancs 

%description
Set of routines for making Map Projections (forward and inverse),
Topographic Maps, Perspective plots, Geological Maps, geological map
symbols, geological databases, interactive plotting and selection of focus

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
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.01-1
- initial package for Fedora