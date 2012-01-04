%global packname  lubridate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          Make dealing with dates a little easier

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-plyr R-stringr 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-plyr R-stringr 


%description
Lubridate makes it easier to work with dates and times by providing
functions to identify and parse date-time data, extract and modify
components of a date-time (years, months, days, hours, minutes, and
seconds), perform accurate math on date-times, handle time zones and
Daylight Savings Time. Lubridate has a consistent, memorable syntax, that
makes working with dates fun instead of frustrating.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora