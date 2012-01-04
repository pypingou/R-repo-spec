%global packname  sos4R
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.7
Release:          1%{?dist}
Summary:          An R client for the OGC Sensor Observation Service

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-XML R-RCurl R-sp R-methods R-graphics R-xtable 


BuildRequires:    R-devel tex(latex) R-XML R-RCurl R-sp R-methods R-graphics R-xtable



%description
sos4R is a client for Sensor Observation Services (SOS) as specified by
the Open Geospatial Consortium (OGC). It allows users to retrieve metadata
from SOS web services and to interactively create requests for near
real-time observation data based on the available sensors, phenomena,
observations et cetera using thematic, temporal and spatial filtering.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.7-1
- initial package for Fedora